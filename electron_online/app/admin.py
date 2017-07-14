from django.contrib import admin
from .models import App
from .models import Version

class AppAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = App


class VersionAdmin(admin.ModelAdmin):
    list_display = ['version']

    class Meta:
        model = Version


admin.site.register(App, AppAdmin)
admin.site.register(Version, VersionAdmin)

