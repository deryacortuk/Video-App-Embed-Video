from django.shortcuts import redirect, render,get_object_or_404
from .forms import VideoForm,EmbedVideoForm
from .models import VideoModel,EmbedVideo
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"index.html")

@login_required(login_url="user:login")
def videoadd(request):
    form = VideoForm(request.POST, request.FILES )

    if form.is_valid():
        video = form.save(commit=False)
        video.username = request.user
        video.save()

        messages.success(request,"video is added successfully")
        return redirect("video:dashboard")
    return render(request,"videoadd.html",{"form":form})

@login_required(login_url="user:login")
def videoupdate(request,id):
    qr = get_object_or_404(VideoModel,id=id)
    form  =VideoForm(request.POST, request.FILES, instance=qr)

    if form.is_valid():
        newvideo = form.save(commit=False)
        qr.username = request.user

        newvideo.save()
        
        messages.success(request,"video is updated")
        return redirect("video:dashboard")
    return render(request,"update.html",{"form":form})


@login_required(login_url="user:login")
def dashboard(request):
    videos = VideoModel.objects.filter(username = request.user)
    return render(request,"dashboard.html",{"videos":videos})
   

@login_required(login_url="user:login")
def deletevideo(request,id):
    video = get_object_or_404(VideoModel,id=id)

    video.delete()

    messages.success(request,"video is deleted")

    return redirect("video:dashboard")

@login_required(login_url="user:login")
def embedded(request):
    videos = EmbedVideo.objects.filter(username=request.user)
    return render(request,'embed.html',{"videos":videos})
