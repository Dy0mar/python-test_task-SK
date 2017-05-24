from django.contrib import auth
from django.shortcuts import render, redirect
from django.template.context_processors import csrf


def login(request):
    context = {}
    context.update(csrf(request))

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect(request.POST.get('return_path', '/'))
        else:
            context['login_error'] = 'User not found'
            return render(request, 'loginout/login.html', context)
    else:
        return_path = request.META.get('HTTP_REFERER', '/')
        context['return_path'] = return_path
        return render(request, 'loginout/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
