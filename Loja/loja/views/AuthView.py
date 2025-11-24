from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from loja.forms.AuthForm import LoginForm
def login_view(request):
    print("login view")
    loginForm = LoginForm()
    print("login view1")
    message = None
    if request.user.is_authenticated:
        print("login view2")
        return redirect('/')
    print("login view2b")
    if request.method == 'POST':
        print("login view3")
        username = request.POST['username']
        password = request.POST['password']
        loginForm = LoginForm(request.POST)
        print("login view3b")   
        if loginForm.is_valid():
            print("login view4")
            user = authenticate(username=username, password=password)
            print("login view4b")
            if user is not None:
                print("login view5")
                login(request, user)
                return redirect('/')
            else:
                message = {'type': 'danger', 'text': 'Dados de usuário incorretos'}
    context = {'form': loginForm, 'message': message,'title': 'Login', 'button_text': 'Entrar', 'link_text': 'Registrar', 'link_href': '/register'}
    return render(request, template_name='auth/auth.html', context=context, status=200)