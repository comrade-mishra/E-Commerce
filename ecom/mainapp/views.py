from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def products(request):
    return render(request, 'pages/products.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about-us.html')

def team(request):
    return render(request, 'pages/team.html')

def blog(request):
    return render(request, 'pages/blog.html')

def testes(request):
    return render(request, 'pages/testimonials.html')

def terms(request):
    return render(request, 'pages/terms.html')

def details(request):
    return render(request, 'pages/product-details.html')

def blog_details(request):
    return render(request, 'pages/blog-details.html')

