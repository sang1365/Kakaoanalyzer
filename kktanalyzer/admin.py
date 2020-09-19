from django.contrib import admin

from django.contrib import admin
from .models import chat_data
from .models import chat_title


class kdataAdmin(admin.ModelAdmin):
    search_fields = ['subject']


class ktitleAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(chat_data, kdataAdmin)
admin.site.register(chat_title, ktitleAdmin)