import random
from django.shortcuts import render,redirect
from .models import Orderline,Customer,Product,Assembling,Employee,ProductPart,Part,Profile,Supplier
from .forms import RegistrationForm,CustomerProfileForm, EmployeeProfileForm,SupplierProfileForm
from django.urls import reverse
from django.db.models import Max

def home(request):

    if request.user.is_authenticated:
        args = {
            'username':request.user
        }
    else:
        args = {
            'username':' '
        }
    return render(request,'index.html',args)

def emp_register(request):
    if request.method == 'POST':
        userform = RegistrationForm(request.POST)
        profileform = EmployeeProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid() :
            form1 = userform.save()
            form2 = profileform.save()
            
            return redirect(reverse('dbms_app:login'))
    else:
        userform = RegistrationForm()
        profileform = EmployeeProfileForm()
    args = {'form1':userform, 'form2':profileform}

    return render(request,'dbms_app/reg_form.html',args)

def supp_register(request):
   
    if request.method == 'POST':
        userform = RegistrationForm(request.POST)
        profileform = SupplierProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid() :
            form1 = userform.save()
            form2 = profileform.save()
            return redirect(reverse('dbms_app:login'))
    else:
        userform = RegistrationForm()
        profileform = SupplierProfileForm()
    args = {'form1':userform, 'form2':profileform}

    return render(request,'dbms_app/reg_form.html',args)

def cust_register(request):
    if request.method == 'POST':
        userform = RegistrationForm(request.POST)
        profileform = CustomerProfileForm(request.POST)
        if userform.is_valid() and profileform.is_valid() :
            form1 = userform.save()
            form2 = profileform.save()
            return redirect(reverse('dbms_app:login'))
    else:
        userform = RegistrationForm()
        profileform = CustomerProfileForm()
    args = {'form1':userform, 'form2':profileform}

    return render(request,'dbms_app/reg_form.html',args)


def buy_porsche(request):

    if request.method == 'POST':
        form = request.POST
        if form:
            profile = Profile.objects.get( user = request.user)
            customer = Customer.objects.get(name = profile.name)
            quantity = form['quantity']
            if Orderline.objects.all().aggregate(Max('id'))['id__max']:
                order_id = Orderline.objects.all().aggregate(Max('id'))['id__max'] +1
            else:
                order_id = 1
            order = Orderline(id = order_id ,customerid = customer, qty = quantity )
            order.save()

            if Product.objects.all().aggregate(Max('id'))['id__max']:
                product_id = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
            else:
                product_id = 1
            porsche_product = Product(id = product_id, orderid = order, title = 'Porsche', price = 10000)
            porsche_product.save()

            empid = random.randint(1,Employee.objects.all().count())
            emp = Employee.objects.get(id = empid)

            assemble = Assembling(productid = porsche_product, employeeid = emp)
            assemble.save()

            for i in range(1,Part.objects.all().count()+1):
                
                pp = ProductPart(productid=porsche_product, partid = Part.objects.get(id=i)) 
                pp.save()
                print(pp)


            return redirect(reverse('dbms_app:success'))

    return render (request,'dbms_app/buy_porsche.html')

def buy_lamborghini(request):

    if request.method == 'POST':
        form = request.POST
        print(request.user)
        if form:
            profile = Profile.objects.get( user = request.user)
            customer = Customer.objects.get(name = profile.name)
            quantity = form['quantity']
            if Orderline.objects.all().aggregate(Max('id'))['id__max']:
                order_id = Orderline.objects.all().aggregate(Max('id'))['id__max'] +1
            else:
                order_id = 1
            order = Orderline(id = order_id ,customerid = customer, qty = quantity )
            order.save()

            if Product.objects.all().aggregate(Max('id'))['id__max']:
                product_id = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
            else:
                product_id = 1
            porsche_product = Product(id = product_id, orderid = order, title = 'Lamborghini', price = 12000 )
            porsche_product.save()

            empid = random.randint(1,Employee.objects.all().count())
            emp = Employee.objects.get(id = empid)

            assemble = Assembling(productid = porsche_product, employeeid = emp)
            assemble.save()

            for i in range(1,Part.objects.all().count()+1):
                pp = ProductPart(productid=porsche_product, partid = Part.objects.get(id=i)) 
                pp.save()


            return redirect(reverse('dbms_app:success'))

    return render (request,'dbms_app/buy_lamborghini.html')

def buy_harley(request):

    if request.method == 'POST':
        form = request.POST
        print(request.user)
        if form:
            profile = Profile.objects.get( user = request.user)
            customer = Customer.objects.get(name = profile.name)
            quantity = form['quantity']
            if Orderline.objects.all().aggregate(Max('id'))['id__max']:
                order_id = Orderline.objects.all().aggregate(Max('id'))['id__max'] +1
            else:
                order_id = 1
            order = Orderline(id = order_id ,customerid = customer, qty = quantity )
            order.save()

            if Product.objects.all().aggregate(Max('id'))['id__max']:
                product_id = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
            else:
                product_id = 1
            porsche_product = Product(id = product_id, orderid = order, title = 'Harley Davidson', price = 8000)
            porsche_product.save()

            empid = random.randint(1,Employee.objects.all().count())
            emp = Employee.objects.get(id = empid)

            assemble = Assembling(productid = porsche_product, employeeid = emp)
            assemble.save()

            for i in range(1,Part.objects.all().count()+1):
                pp = ProductPart(productid=porsche_product, partid = Part.objects.get(id=i)) 
                pp.save()


            return redirect(reverse('dbms_app:success'))

    return render (request,'dbms_app/buy_harley.html')

def buy_royal(request):

    if request.method == 'POST':
        form = request.POST
        print(request.user)
        if form:
            profile = Profile.objects.get( user = request.user)
            customer = Customer.objects.get(name = profile.name)
            quantity = form['quantity']
            if Orderline.objects.all().aggregate(Max('id'))['id__max']:
                order_id = Orderline.objects.all().aggregate(Max('id'))['id__max'] +1
            else:
                order_id = 1
            order = Orderline(id = order_id ,customerid = customer, qty = quantity )
            order.save()

            if Product.objects.all().aggregate(Max('id'))['id__max']:
                product_id = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
            else:
                product_id = 1
            porsche_product = Product(id = product_id, orderid = order, title = 'Royal Enfield', price = 7000)
            porsche_product.save()

            empid = random.randint(1,Employee.objects.all().count())
            emp = Employee.objects.get(id = empid)

            assemble = Assembling(productid = porsche_product, employeeid = emp)
            assemble.save()

            for i in range(1,Part.objects.all().count()+1):
                pp = ProductPart(productid=porsche_product, partid = Part.objects.get(id=i)) 
                pp.save()


            return redirect(reverse('dbms_app:success'))

    return render (request,'dbms_app/buy_royal.html')

def buy_benz(request):

    if request.method == 'POST':
        form = request.POST
        print(request.user)
        if form:
            
            profile = Profile.objects.get( user = request.user)
            customer = Customer.objects.get(name = profile.name)
            quantity = form['quantity']
            if Orderline.objects.all().aggregate(Max('id'))['id__max']:
                order_id = Orderline.objects.all().aggregate(Max('id'))['id__max'] +1
            else:
                order_id = 1
            order = Orderline(id = order_id ,customerid = customer, qty = quantity )
            order.save()

            if Product.objects.all().aggregate(Max('id'))['id__max']:
                product_id = Product.objects.all().aggregate(Max('id'))['id__max'] + 1
            else:
                product_id = 1
            porsche_product = Product(id = product_id, orderid = order, title = 'Mercedes Benz', price = 9000)
            porsche_product.save()

            empid = random.randint(1,Employee.objects.all().count())
            emp = Employee.objects.get(id = empid)

            assemble = Assembling(productid = porsche_product, employeeid = emp)
            assemble.save()

            for i in range(1,Part.objects.all().count()+1):
                pp = ProductPart(productid=porsche_product, partid = Part.objects.get(id=i)) 
                pp.save()


            return redirect(reverse('dbms_app:success'))

    return render (request,'dbms_app/buy_benz.html')

def success(request):

    return render (request,'dbms_app/success.html')

def profile(request):

    if request.user.is_authenticated:
        profile = Profile.objects.get(user = request.user)
        if profile.user_type == 'E':
            return redirect(reverse('dbms_app:emp_profile'))
        if profile.user_type == 'C':
            return redirect(reverse('dbms_app:cust_profile'))
        if profile.user_type == 'S':
            return redirect(reverse('dbms_app:supp_profile'))
    else:
        return redirect(reverse('dbms_app:home'))



def emp_profile(request):

    if request.user.is_authenticated:
        profile = Profile.objects.get( user = request.user)
        employee = Employee.objects.get( name = profile.name) 
        assembles = Assembling.objects.filter(employeeid = employee)  
        args={
            'employee' : employee,
            'assembles' : assembles
        }
    else:
        args={
            'employee' : employee,
        }


    return render (request,'dbms_app/emp_profile.html',args)

def cust_profile(request):

    if request.user.is_authenticated:
        profile = Profile.objects.get( user = request.user)
        customer = Customer.objects.get( name = profile.name)
        orders = Orderline.objects.filter(customerid = customer)
        orderid_list = []
        for order in orders:
            orderid_list.append(order.id )
        if orderid_list : 
            products = Product.objects.filter(orderid__in=orderid_list)
            print(products)
        args={
            'products' : products,
            'customer' : customer
        }
    else:
        args={
            'customer' : customer
        }

    return render (request,'dbms_app/cust_profile.html',args)

def supp_profile(request):

    if request.user.is_authenticated:
        profile = Profile.objects.get( user = request.user)
        supplier = Supplier.objects.get( name = profile.name) 
        part = Part.objects.get( supplierid = supplier)
        productparts = ProductPart.objects.filter(partid = part) 
        for productpart in productparts: 
            print(productpart.partid)
        args={
            'supplier' : supplier,
            'productparts' : productparts
        }
    else:
        args={
            'supplier' : supplier,
        }

    return render (request,'dbms_app/supp_profile.html',args)