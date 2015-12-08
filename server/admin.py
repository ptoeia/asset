from django.contrib import admin
from server.models import Machine
admin.site.register(Machine)

# Register your models here.
class serveradmin(admin.ModelAdmin):
    list_display = ('ip','name')

