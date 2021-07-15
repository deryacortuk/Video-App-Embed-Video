from django.db import models
from .validator import file_size
from embed_video.fields import EmbedVideoField

# Create your models here.

class VideoModel(models.Model):

    username = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    caption = models.CharField(max_length=150)
    video = models.FileField(upload_to="video/%y",validators=[file_size])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.caption
    
    class Meta:
        ordering = ['-created_date']

class EmbedVideo(models.Model):

    title = models.CharField(max_length=150)
    username = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ["-created_date"]
