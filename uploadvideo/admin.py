from django.contrib import admin
from .models import VideoModel,EmbedVideo
from embed_video.admin import AdminVideoMixin
# Register your models here.

admin.site.register(VideoModel)

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(EmbedVideo, MyModelAdmin)