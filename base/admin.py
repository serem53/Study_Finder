from django.contrib import admin

# Register your models here.
from .models import Room,Topic,Message,User
# user model already registered by default
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(User)