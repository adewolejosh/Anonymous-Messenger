from django.shortcuts import render
from .forms import AmaForm
from .models import Text
# from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def home(request):
    template_name = 'home.html'

    if request.method == 'POST':
        form = AmaForm(request.POST)
        if form.is_valid():
            form.save()
            note = form.cleaned_data['note']
            messages.success(request, 'Your message has been sent')
            return render(request, template_name, {form: 'form'})
        # send_mail('Anonymous', {{ note }}, settings.EMAIL_HOST_USER, ['adewole.josh@gmail.com'])
        else:
            messages.error(request, 'An error occured')
            return render(request, template_name, {'form': form})

    return render(request, template_name)


@login_required()
def adminS(request):
    template_name = 'adminDSBD.html'
    textings = Text.objects.all()
    return render(request, template_name, {'textings': textings})
