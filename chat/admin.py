from django.contrib import admin
from .models import Chat_message, Messenger_message


class Chat_messageAdmin(admin.ModelAdmin):
    list_display = ("pk","author", "text", "timestamp") 
    search_fields = ("text",) 
    list_filter = ("timestamp",) 
    empty_value_display = "-пусто-" 


class Messenger_messageAdmin(admin.ModelAdmin):
    list_display = ("pk","author", "companion", "text", "timestamp") 
    search_fields = ("text",) 
    list_filter = ("timestamp",) 
    empty_value_display = "-пусто-" 

admin.site.register(Chat_message, Chat_messageAdmin) 
admin.site.register(Messenger_message, Messenger_messageAdmin)    