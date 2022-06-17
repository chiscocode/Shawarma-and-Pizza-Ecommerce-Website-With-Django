from django.shortcuts import render
from products.models import Product,Category
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def home(request):
    newest_products = Product.objects.all()
    #pagination
    paginator = Paginator(newest_products, 3)
    page = request.GET.get('page')
    productpage = paginator.get_page(page)
    context={'newest_products':productpage}
    return render(request,'home.html',context)

def menu(request):
    newest_products = Product.objects.all()
    #pagination
    paginator = Paginator(newest_products, 6)
    page = request.GET.get('page')
    productpage = paginator.get_page(page)
    context={'newest_products':productpage}
    return render(request,'menu.html',context)

def about(request):
    return render(request,'about.html')

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return render(request,'emailsent.html')
    context={'form':form}
    return render(request,'contact.html',context)

