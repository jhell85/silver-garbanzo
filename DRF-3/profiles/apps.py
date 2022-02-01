from django.apps import AppConfig

# this must be modified when using signals in django as well as __init__.py
class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    def ready(self):
        import profiles.signals