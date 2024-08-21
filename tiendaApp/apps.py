from django.apps import AppConfig


class TiendaappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tiendaApp'

#clase para enviar un mail
class CorreoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'correo'