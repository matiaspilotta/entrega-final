from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *

# Create your views here.




def inicio(request):
    if request.user.is_authenticated:
        usuario = request.user
        avatar = Avatar.objects.filter(user=usuario).last()
        avatar_url = avatar.imagen.url if avatar is not None else ""
    else:
        avatar_url = ""

    return render(request, "core/inicio.html", context={"avatar_url": avatar_url})


def nosotros(request):
 

    return render(request, "core/nosotros.html")

def post(request):
 

    return render(request, "core/post.html")




def login(request):

    if request.user.is_authenticated:
        return render(
            request,
            "core/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "core/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "core/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "core/login.html",
                {"form": formulario}
            )



def logout(request):
    pass


from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView

def registro(request):

    if request.method == "GET":
        return render(
            request,
            "core/registro.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "core/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "registro.html",
                {"form": formulario}
            )

@login_required
def editar_perfil(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""


    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "core/editar_perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("core:inicio")


@login_required
def editar_perfil(request):

    usuario = request.user
    avatar = Avatar.objects.filter(user=usuario).last()
    avatar_url = avatar.imagen.url if avatar is not None else ""


    if request.method == "GET":


        valores_iniciales = {
            "email": usuario.email,
            "first_name": usuario.first_name,
            "last_name": usuario.last_name
        }


        formulario = UserEditionFormulario(initial=valores_iniciales)
        return render(
            request,
            "core/editar_perfil.html",
            context={"form": formulario, "usuario": usuario, "avatar_url": avatar_url}
            )
    else:
        formulario = UserEditionFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            usuario.email = informacion["email"]

            usuario.set_password(informacion["password1"])

            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.save()
        return redirect("core:inicio")


@login_required
def crear_avatar(request):

    usuario = request.user

    if request.method == "GET":
        formulario = UserAvatarFormulario()
        return render(
            request,
            "core/crear_avatar.html",
            context={"form": formulario, "usuario": usuario}
        )
    else:
        formulario = UserAvatarFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Avatar(user=usuario, imagen=informacion["imagen"])
            modelo.save()
            return redirect("core:inicio")



from django.contrib.auth.models import User
from .models import Post, Perfil

def mostrar_profile(request, user_id):
    user = User.objects.get(id=user_id)
    todos_los_posts = Post.objects.filter(autor=user).all()
    perfil = Perfil.objects.filter(usuario=user).first()
    avatar = Avatar.objects.filter(user=user).first()
    avatar_url = avatar.imagen.url if avatar is not None else ""
    contexto = {"posts": todos_los_posts, "perfil": perfil, "avatar_url": avatar_url}

    return render(request, "core/profile.html", context=contexto)