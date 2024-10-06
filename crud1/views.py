from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import user_model
from .forms import user_form

# Create your views here.
def homepage(request):
    data = user_model.objects.all()
    return render(request, 'homepage.html', {'data': data})

def add_user(request):
    if request.method == 'POST':
        add = user_form(request.POST)
        if add.is_valid():
            user = user_model(
                name=add.cleaned_data['name'],
                email=add.cleaned_data['email'],
                password=add.cleaned_data['password'],
                textbox=add.cleaned_data['textbox']
                )
            user.save()
            return redirect('/home/')

    else:
        add = user_form()
        
    # form.order_fields(field_order= ['name', 'email', 'password'])
    return render(request, 'add_user.html', {'add': add})

def delete_user(request, user_id):
    dlt = get_object_or_404(user_model, id=user_id)

    if request.method == 'POST':
        dlt.delete()
        return redirect('/home/')
    
    return render(request, 'delete_user.html', {'dlt': dlt})


def update_user(request, user_id):
    user = get_object_or_404(user_model, id=user_id)

    if request.method == 'POST':
        update_user = user_form(request.POST)
        if update_user.is_valid():
            user.name = update_user.cleaned_data['name']
            user.email = update_user.cleaned_data['email']
            user.password = update_user.cleaned_data['password']
            user.textbox = update_user.cleaned_data['textbox']
            user.save()

            return redirect('/home/')
    else:
        # Pre-fill the form with the existing user's data
        initial_data = {
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'repassword': user.password,
            'textbox': user.textbox,
        }
        update_user = user_form(initial=initial_data)

    return render(request, 'update_user.html', {'update_user': update_user, 'user': user})