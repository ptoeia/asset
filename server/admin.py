from django.contrib import admin
from server.models import Servers
admin.site.register(Servers)

# Register your models here.
class serveradmin(admin.ModelAdmin):
    list_display = ('ip','name')

