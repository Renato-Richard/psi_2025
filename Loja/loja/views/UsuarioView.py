from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Usuario
from loja.forms.UserUsuarioForm import UserUsuarioForm, UserForm
def list_usuario_view(request, id=None):
    # carrega somente usuarios, não inclui os admin
    usuarios = Usuario.objects.filter(perfil=2)
    context = {
        'usuarios': usuarios
    }
    return render(request, template_name='usuario/usuario.html', context=context, status=200)
def edit_usuario_view(request):
    print("edit_usuario_view 0")
    print(request.user)
    usuario = Usuario.objects.filter(user=request.user)
    print("edit_usuario_view 1")
    print(usuario)
    usuarioForm = UserUsuarioForm(instance=usuario)
    print("edit_usuario_view 2") 
    userForm = UserForm(instance=request.user)
    print("edit_usuario_view 3")
    context = {
        # 'usuarioForm': usuarioForm,
        'userForm': userForm
    }
    return render(request, template_name='usuario/usuario-edit.html', context=context, status=200)