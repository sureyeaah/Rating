from django.contrib import admin
from django.apps import apps

# register all models
app = apps.get_app_config('rating')

for mode_name, model in app.models.items():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
