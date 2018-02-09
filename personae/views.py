from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PersonaForm
from .models import Persona


@login_required
def user_profile(request):
    return render(request, 'personae/user_profile.html', {
        'personae': request.user.personae.filter(is_deleted=False)
    })


@login_required
def create_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            persona = Persona(name=form.cleaned_data['name'], user=request.user)
            persona.save()
            return redirect('user_profile')
    else:
        form = PersonaForm()

    return render(request, 'personae/create_persona.html', {
        'form': form,
    })
