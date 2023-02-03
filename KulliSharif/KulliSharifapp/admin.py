from django.contrib import admin
from django.contrib.auth.models import Group
from .models import  *
# Register your models here.
# admin.site.register(Events)
admin.site.register(Projects)
admin.site.register(Videos)
admin.site.register(Books)

@admin.register(Events)

class EventsAdmin(admin.ModelAdmin):
    list_display=['id','title_english','title_urdu','detail_english','detail_urdu']


admin.site.site_header="Khanqah Kullishrif"
admin.site.unregister(Group)
