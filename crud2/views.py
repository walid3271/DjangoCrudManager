from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import user_model
from .forms import user_form

# Create your views here.
def homepage(request):
    data = user_model.objects.all()

    if request.method == 'POST':
        if 'add_user' in request.POST:
            add_form = user_form(request.POST)
            if add_form.is_valid():
                user = user_model(
                    name=add_form.cleaned_data['name'],
                    email=add_form.cleaned_data['email'],
                    password=add_form.cleaned_data['password'],
                    textbox=add_form.cleaned_data['textbox']
                )
                user.save()
                return JsonResponse({'message': 'User added successfully!'}, status=200)
            else:
                return JsonResponse({'errors': add_form.errors}, status=400)

        if 'update_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(user_model, id=user_id)
            update_form = user_form(request.POST)
            if update_form.is_valid():
                user.name = update_form.cleaned_data['name']
                user.email = update_form.cleaned_data['email']
                user.password = update_form.cleaned_data['password']
                user.textbox = update_form.cleaned_data['textbox']
                user.save()
                return JsonResponse({'message': 'User updated successfully!'}, status=200)
            else:
                return JsonResponse({'errors': update_form.errors}, status=400)

        if 'delete_user' in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(user_model, id=user_id)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully!'}, status=200)

    else:
        add_form = user_form()
        update_form = user_form()

    return render(request, 'homepage.html', {'data': data, 'add_form': add_form, 'update_form': update_form})
