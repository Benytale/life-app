from django.contrib import admin
from .models import User, Video, Like, Follow, Earning

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Like)
admin.site.register(Follow)
admin.site.register(Earning)
