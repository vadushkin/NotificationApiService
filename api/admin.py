from django.contrib import admin
from .models import Client, Mailing, Message, Operator, Tag


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = (
        'pk', 'start_datetime', 'text', 'finish_datetime')
    search_fields = ('start_datetime',)
    list_filter = ('text',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk', 'phone_number', 'operator', 'tag')
    search_fields = ('phone_number',)
    list_filter = ('operator',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('pk', 'datetime', 'status', 'mailing')
    search_fields = ('datetime',)
    list_filter = ('status',)


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'code')
    search_fields = ('name',)
    list_filter = ('code',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
