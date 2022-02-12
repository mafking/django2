from django.shortcuts import render,redirect
from .models import Post
from django.utils import timezone

# Create your views here.
def index(request):
	post=Post.objects.filter(published__lte=timezone.now())
	return render(request,'blog/index.html',{'post':post})
