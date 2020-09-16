from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import TimelineForm
from django.contrib import messages
from.models import Timeline,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")

def timelines(request):
    keyword=request.GET.get("keyword")
    if keyword:
        timelines=Timeline.objects.filter(title__contains=keyword)
        return render(request,"timelines.html",{"timelines":timelines})
    timelines=Timeline.objects.all()
    return render(request,"timelines.html",{"timelines":timelines})

@login_required(login_url="user:login")
def dashboard(request):
    timelines=Timeline.objects.filter(author=request.user)
    context={"timelines":timelines}
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addtimeline(request):
    form= TimelineForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Timeline has saved")
        return redirect("/timelines/dashboard")

    return render(request,"addtimeline.html",{"form":form})

def detail(request,id):
    timeline=get_object_or_404(Timeline,id=id)
    comments=timeline.comments.all()
    return render(request,"detail.html",{"timeline":timeline,"comments":comments})
@login_required(login_url="user:login")
def updatetimeline(request,id):
    timeline=get_object_or_404(Timeline,id=id)
    form=TimelineForm(request.POST or None,request.FILES or None,instance=timeline)
    if form.is_valid():
        timeline=form.save(commit=False)
        timeline.author=request.user
        timeline.save()
        messages.success(request,"Timeline has updated")
        return redirect("/timelines/dashboard")

    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def deletetimeline(request,id):
    timeline=get_object_or_404(Timeline,id=id)
    timeline.delete()
    messages.success(request,"Timeline has deleted")
    return redirect("/timelines/dashboard")


def comment(request,id):
    timeline= get_object_or_404(Timeline,id=id)

    if request.method=="POST":
        comauthor=request.POST.get("comauthor")
        comcontent=request.POST.get("comcontent")
        

        newcomment=Comment(comauthor=comauthor ,comcontent=comcontent)
        newcomment.timeline=timeline

        newcomment.save()
    return redirect("/timelines/timeline/" +str(id))