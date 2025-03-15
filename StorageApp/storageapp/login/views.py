from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Перевірка на статус "суперкористувач"
            if user.is_superuser:
                return redirect('/products/')
        else:
            return render(request, "login/login.html", {"error": "Неправильний логін або пароль"})
    else:
        return render(request, "login/login.html")

def exit_view(request):
    logout(request)  # Вихід користувача
    return redirect('/')  # Перенаправлення на головну сторінку