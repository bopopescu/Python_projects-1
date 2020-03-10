from django.template.response import TemplateResponse

def home(request):
    return TemplateResponse(request, "home.html")

def about(request):
    return TemplateResponse(request, "about.html")

def page1(request):
    return TemplateResponse(request, "page1.html")

