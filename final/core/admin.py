from django.contrib import admin

from . import models

# Register your models here.



admin.site.register(models.Avatar)
admin.site.register(models.Perfil)
admin.site.register(models.Usuario)


admin.site.register(models.Post)
admin.site.register(models.Comentario)



