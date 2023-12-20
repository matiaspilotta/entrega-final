
from django.urls import path 
from .views import (
    inicio,
    login,
    logout,
    registro,
    editar_perfil,
    crear_avatar,
    mostrar_profile,
    nosotros,
    post,
    
)


app_name = "core"

urlpatterns = [
    path('inicio/', inicio, name="inicio"),
    
    path('nosotros/', nosotros, name="nosotros"),
    path('post/', post, name="post"),
    path('registro/', registro, name="registro"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path("editar-perfil", editar_perfil, name="editar-perfil"),
    path("crear-avatar", crear_avatar, name="crear-avatar"),
    path("profile/<user_id>", mostrar_profile, name="profile"),
 
 
]
