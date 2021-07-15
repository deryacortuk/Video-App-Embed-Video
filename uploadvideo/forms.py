from django import forms
from .models import VideoModel,EmbedVideo

class VideoForm(forms.ModelForm):

    class Meta:
        model = VideoModel

        fields =["caption","video"]
    
class EmbedVideoForm(forms.ModelForm):
    class Meta:

        model = EmbedVideo
        fields=["title","url"]
    