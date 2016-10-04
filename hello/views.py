from django.shortcuts import render, redirect, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "post.html")

def create(request):
    if request.method=="POST":
        context = {
            "nama":request.POST["nama"],
            "pass":request.POST["pass"]
        }
    return render(request, "post.html", context)