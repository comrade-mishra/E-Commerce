from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def prd_render(request):
    return render(request, 'pages/products.html')