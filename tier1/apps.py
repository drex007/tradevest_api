from django.apps import AppConfig


class Tier1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tier1"

    # def ready(self):
    #     from . import models

    #     models.start()
