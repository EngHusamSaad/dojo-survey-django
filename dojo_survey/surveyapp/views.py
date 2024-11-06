from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    return render(request,"index.html")
 


def addnew(request):
    if request.method =="POST":
        name=request.POST["name"]
        location=request.POST["location"]
        lang=request.POST["lang"]
        comment=request.POST["comment"]
        
        data={
            "name":name,
            "location":location,
            "lang":lang,
            "comment":comment 
        }
        return render (request,"result.html",data)
    
# def result(request):
#     # return HttpResponse("Hellllllll")
#     return render (request,"result.html")
        
        
