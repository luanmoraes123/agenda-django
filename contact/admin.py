from django.contrib import admin
from contact.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'picture'

    search_fields = 'id', 'first_name', 'email'
