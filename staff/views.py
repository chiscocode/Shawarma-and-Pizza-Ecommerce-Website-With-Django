from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from . models import Staff
from products.models import Product
from django.contrib import messages, auth
from . forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,  login, logout
from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.

def become_staff(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request, user)
            staff=Staff.objects.create(name=user.username, created_by=user)
            return redirect('staff_admin')
        
    return render(request,'become_staff.html',{'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('staff_admin')
                      
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request, 'login.html')
@login_required
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required
def staff_admin(request):
    staff=request.user.staff
    products = staff.products.all()
    orders = staff.orders.all()
    #pagination
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    users = paginator.get_page(page)

    for order in orders:
        order.staff_amount = 0
        order.staff_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.staff == request.user.staff:
                if item.staff_paid:
                    order.staff_paid_amount += item.get_total_price()
                else:
                    order.staff_amount += item.get_total_price()
                    order.fully_paid = False
    #pagination
    paginator = Paginator(orders, 2)
    page = request.GET.get('page')
    oderpage = paginator.get_page(page)
    context={'staff':staff,'products':users, 'orders': oderpage}
    return render(request,'staff_admin.html',context)


@login_required
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product =form.save(commit=False)
            product.staff = request.user.staff
            product.slug =slugify(product.title)
            product.save()
            
            return redirect('staff_admin')
    context={'form':form}
    return render(request,'add_product.html',context)

@login_required
def edit_product(request,pk):
    products = Product.objects.get(id=pk)
    form = ProductForm(instance=products)
    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES,instance=products)
        if form.is_valid():
            form.save()
            return redirect('staff_admin')            
    context={'form':form}
    return render(request,'edit_product.html',context)


@login_required(login_url='login')
def delete_product(request, pk):
    products=Product.objects.get(id=pk)
    
    if request.method == 'POST':
        products.delete()
        return redirect('staff_admin')
    context={'item':products}
    return render(request, 'delete.html', context)

@login_required
def edit_staff(request):
    staff = request.user.staff

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        if name:
            staff.created_by.email = email
            staff.created_by.save()

            staff.name = name
            staff.save()

            return redirect('staff_admin')
    
    return render(request, 'edit_staff.html', {'staff': staff})
@login_required
def staffs(request):
    staffs = Staff.objects.all()
    #pagination
    paginator = Paginator(staffs, 4)
    page = request.GET.get('page')
    staffspage = paginator.get_page(page)

    return render(request, 'staffs.html', {'staffs': staffspage})
@login_required
def staff(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    return render(request, 'staff.html', {'staff': staff})


