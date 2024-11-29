from django.shortcuts import render, get_object_or_404, redirect
from .models import hamroguff
from .forms import hamroguffform,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

def index(request):
    return render(request, 'index.html')

def hamroguff_list(request):
    guffs = hamroguff.objects.all().order_by('-created_at')
    return render(request, 'hamroguff_list.html', {'guffs': guffs})  # Corrected the context key

@login_required
def hamroguff_create(request):
    if request.method == "POST":
        form = hamroguffform(request.POST, request.FILES)  # Assigned form instance to 'form'
        if form.is_valid():
            guff_instance = form.save(commit=False)  # Changed variable name
            guff_instance.user = request.user 
            guff_instance.save()
            return redirect('hamroguff_list')
    else:
        form = hamroguffform()
    
    return render(request, 'hamroguff_form.html', {'form': form})  # Added 'form' to context

@login_required
def hamroguff_edit(request, hamroguff_id):
    guff = get_object_or_404(hamroguff, pk=hamroguff_id, user=request.user)  # Renamed instance to `guff`
    if request.method == 'POST':
        form = hamroguffform(request.POST, request.FILES, instance=guff)
        if form.is_valid():
            guff_instance = form.save(commit=False)  # Renamed instance to avoid conflict
            guff_instance.user = request.user
            guff_instance.save()
            return redirect('hamroguff_list')
    else:
        form = hamroguffform(instance=guff)

    return render(request, 'hamroguff_form.html', {'form': form})  # Added 'form' to context

@login_required
def hamroguff_delete(request, hamroguff_id):
    guff = get_object_or_404(hamroguff, pk=hamroguff_id, user=request.user)  # Renamed instance to `guff`
    if request.method == 'POST':
        guff.delete()
        return redirect('hamroguff_list')
    return render(request, 'hamroguff_confirm_delete.html', {'hamroguff': guff})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('hamroguff_list')
    
    else:
        form = UserRegistrationForm()


    return render(request, 'registration/register.html', {'form': form})
