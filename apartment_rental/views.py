from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
# FILE UPLOAD AND VIEW
from django.contrib.auth import authenticate

from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *

def admin(request):
    return render(request,'adminpanel.html')  

def dash(request):
    return render(request,'adminpanel.html')      
    
def home(request):
    return  render(request,'staffregistration.html')

def login(request):
    return  render(request,'login.html')

def custreg(request):
    return render(request,'custregistration.html')

def staffregist(request):
    return render(request,'staffregistration.html')

def ownerregist(request):
    return render(request,'ownerregistration.html')     

def registcust(request):
    if request.method == "POST":
        entered_fname = request.POST.get("cust_fname")
        entered_mname = request.POST.get("cust_mname")
        entered_lname = request.POST.get("cust_lname")
        entered_email = request.POST.get("username")
        entered_dist = request.POST.get("cust_district")
        entered_city = request.POST.get("cust_city")
        entered_pin = request.POST.get("cust_pin")
        entered_phno = request.POST.get("cust_phno")
        entered_gender = request.POST.get("cust_gender")
        entered_dob = request.POST.get("cust_dob")
        entered_pass = request.POST.get("password_")
        today_date = timezone.now().date()
        
        # Check if the username already exists in tbl_login
        if tbl_login.objects.filter(username=entered_email).exists():
            error_message = "Username already exist!"
            return render(request, 'custregistration.html', {'error_message': error_message})
        else:
            # Create new user and customer if username doesn't exist
            lg = tbl_login.objects.create(
                username=entered_email,
                password=entered_pass,
                join_date=today_date,
                user_type='customer'
            )

            exe = tbl_customer(
                username=lg,
                Cust_Phno=entered_phno,
                Cust_Fname=entered_fname,
                Cust_Mname=entered_mname,
                Cust_Lname=entered_lname,
                Cust_Dob=entered_dob,
                Cust_Gender=entered_gender,
                Cust_Dist=entered_dist,
                Cust_City=entered_city,
                Cust_Pin=entered_pin,
                Cust_Status='1',
            )
            exe.save()

    return render(request, 'login.html')

def registstaff(request):
    if request.method == "POST":
        entered_fname = request.POST.get("staff_fname")
        entered_mname = request.POST.get("staff_mname")
        entered_lname = request.POST.get("staff_lname")
        entered_email = request.POST.get("username")
        entered_dist = request.POST.get("staff_district")
        entered_city = request.POST.get("staff_city")
        entered_desig = request.POST.get("staff_desig")
        entered_phno = request.POST.get("staff_phno")
        entered_gender = request.POST.get("staff_gender")
        entered_dob = request.POST.get("staff_dob")
        entered_join = request.POST.get("staff_join")
        entered_pass = request.POST.get("password_")
        today_date = timezone.now().date()
        lg = tbl_login.objects.create(
            username=entered_email,
            password=entered_pass,
            join_date=today_date,
            user_type='staff'
        )

        # Use the retrieved instance when creating the tbl_customer instance
        exe = tbl_staff(
            username=lg,
            Staff_Phno=entered_phno,
            Staff_Fname=entered_fname,
            Staff_Mname=entered_mname,
            Staff_Lname=entered_lname,
            Staff_Dob=entered_dob,
            Staff_Join=entered_dob,
            Staff_Gender=entered_gender,
            Staff_Dist=entered_dist,
            Staff_City=entered_city,
            Staff_Designation=entered_desig,
            Staff_Status='1',
        )
        exe.save()
        
    return render(request, 'managestaff.html')
    
def managestaff(request):
    res=tbl_staff.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'managestaff.html',{'result':res, 'error_message': error_message})

def managecust(request):
    c=tbl_customer.objects.all()
    return render(request,"managecustomer.html",{"c":c})

def manageowner(request):
    res=tbl_owner.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'manageowner.html',{'result':res, 'error_message': error_message})

def registowner(request):
    if request.method == "POST":
        entered_fname = request.POST.get("owner_fname")
        entered_mname = request.POST.get("owner_mname")
        entered_lname = request.POST.get("owner_lname")
        entered_email = request.POST.get("username")
        entered_dist = request.POST.get("owner_district")
        entered_city = request.POST.get("owner_city")
        entered_pin = request.POST.get("owner_pin")
        entered_phno = request.POST.get("owner_phno")
        entered_gender = request.POST.get("owner_gender")
        entered_dob = request.POST.get("owner_dob")
        entered_pass = request.POST.get("password_")
        today_date = timezone.now().date()
        lg = tbl_login.objects.create(
            username=entered_email,
            password=entered_pass,
            join_date=today_date,
            user_type='owner'
        )

        exe = tbl_owner(
            username=lg,
            Owner_Phno=entered_phno,
            Owner_Fname=entered_fname,
            Owner_Mname=entered_mname,
            Owner_Lname=entered_lname,
            Owner_Dob=entered_dob,
            Owner_Gender=entered_gender,
            Owner_Dist=entered_dist,
            Owner_City=entered_city,
            Owner_Pin=entered_pin,
            Owner_Status=1,
        )
        exe.save()

    return render(request, 'manageowner.html')

def catregist(request):
    return render(request,'category.html')

def registcat(request):
    if request.method == "POST":
        entered_catname = request.POST.get("category_name")
        entered_catimage = request.FILES.get("category_image")
        entered_catdesc = request.POST.get("category_desc")

        exe = tbl_category(
            Cat_Name=entered_catname,
            Cat_Img=entered_catimage,
            Cat_Desc=entered_catdesc,
        )
        exe.save()
        return redirect(managecat) 

    return render(request, 'managecategory.html')

def managecat(request):
    res=tbl_category.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'managecategory.html',{'result':res, 'error_message': error_message})

def activate_customer(request, id):
    customer = tbl_customer.objects.get(pk=id)
    customer.Cust_Status = 1
    customer.save()
    return redirect(managecust)

def deactivate_customer(request, id):
    customer = tbl_customer.objects.get(pk=id)
    customer.Cust_Status = 0
    customer.save()
    return redirect(managecust)

def activate_staff(request, id):
    staff = tbl_staff.objects.get(pk=id)
    staff.Staff_Status = 1
    staff.save()
    return redirect(managestaff)

def deactivate_staff(request, id):
    staff = tbl_staff.objects.get(pk=id)
    staff.Staff_Status = 0
    staff.save()
    return redirect(managestaff)

def editstaff_fetch(request, id):
    staff = tbl_staff.objects.get(id=id)
    return render(request, 'editstaff.html', {'staff': staff})

def editstaff(request, id):
    staff = tbl_staff.objects.get(id=id)
    login_obj = tbl_login.objects.get(username=staff.username.username) 

    if request.method == 'POST':
        staff.Staff_Fname = request.POST.get('staff_fname')
        staff.Staff_Mname = request.POST.get('staff_mname')
        staff.Staff_Lname = request.POST.get('staff_lname')
        staff.Staff_Dist = request.POST.get('staff_district')
        staff.Staff_City = request.POST.get('staff_city')
        staff.Staff_Designation = request.POST.get('staff_desig')
        staff.Staff_Phno = request.POST.get('staff_phno')
        staff.Staff_Gender = request.POST.get('staff_gender')
        staff.Staff_Dob = request.POST.get('staff_dob')
        staff.Staff_Join = request.POST.get('staff_join')
        staff.save()

        # Update username if provided in the form
        new_username = request.POST.get('username')
        if new_username:
            login_obj.username = new_username
            login_obj.save()

        # Update password if provided in the form
        new_password = request.POST.get('password_')
        if new_password:
            login_obj.password = new_password
            login_obj.save()

        return redirect(managestaff)

def activate_owner(request, id):
    owner = tbl_owner.objects.get(pk=id)
    owner.Owner_Status = 1
    owner.save()
    return redirect(manageowner)

def deactivate_owner(request, id):
    owner = tbl_owner.objects.get(pk=id)
    owner.Owner_Status = 0
    owner.save()
    return redirect(manageowner)

def editowner_fetch(request, id):
    owner= tbl_owner.objects.get(id=id)
    return render(request, 'editowner.html', {'owner': owner})

def editowner(request, id):
    owner = tbl_owner.objects.get(id=id)
    login_obj = tbl_login.objects.get(username=owner.username.username)

    if request.method == 'POST':
        owner.Owner_Fname = request.POST.get('owner_fname')
        owner.Owner_Mname = request.POST.get('owner_mname')
        owner.Owner_Lname = request.POST.get('owner_lname')
        owner.Owner_Dist = request.POST.get('owner_district')
        owner.Owner_City = request.POST.get('owner_city')
        owner.Owner_Pin= request.POST.get('owner_pin')
        owner.Owner_Phno = request.POST.get('owner_phno')
        owner.Owner_Gender = request.POST.get('owner_gender')
        owner.Owner_Dob = request.POST.get('owner_dob')
        owner.save()

        # Update username if provided in the form
        new_username = request.POST.get('username')
        if new_username:
            login_obj.username = new_username
            login_obj.save()

        # Update password if provided in the form
        new_password = request.POST.get('password_')
        if new_password:
            login_obj.password = new_password
            login_obj.save()

        return redirect(manageowner)

def editcat_fetch(request, id):
    cat= tbl_category.objects.get(id=id)
    return render(request, 'editcategory.html', {'cat': cat})

def editcat(request, id):
    cat = tbl_category.objects.get(id=id)
    if request.method == 'POST':
        # Update category fields based on the form data
        cat.Cat_Name = request.POST.get('category_name')
        cat.Cat_Desc = request.POST.get('category_desc')

        if 'category_image' in request.FILES:
            cat.Cat_Img = request.FILES['category_image']
        cat.save()
        return redirect(managecat)

def managesubcat(request):
    res=tbl_subcategory.objects.all()
    cat=tbl_category.objects.all()
    error_message = request.session.pop('error_message', None)
    return render(request, 'managesubcategory.html',{'result':res,'category':cat, 'error_message': error_message})

def subcatregist(request):
    categories = tbl_category.objects.all()
    return render(request, 'subcategory.html', {'categories': categories})

def registsubcat(request):
    if request.method == "POST":
        cat_id = request.POST.get("category_id")
        category = tbl_category.objects.get(id=cat_id)
        entered_subcatname = request.POST.get("subcategory_name")
        entered_subcatdesc = request.POST.get("subcategory_desc")
        subcat_image = request.FILES.get("subcategory_image")

        subcat = tbl_subcategory(
            Cat_id=category,
            Subcat_Name=entered_subcatname,
            Subcat_Desc=entered_subcatdesc,
            Subcat_Img=subcat_image
        )
        subcat.save()
        return redirect(managesubcat)

    return render(request, 'managesubcategory.html')

def editsubcat_fetch(request, id):
    subcat = tbl_subcategory.objects.get(id=id)
    categories = tbl_category.objects.all() 
    return render(request, 'editsubcategory.html', {'subcat': subcat, 'categories': categories})

def editsubcat(request, id):
    subcat = tbl_subcategory.objects.get(id=id)
    
    if request.method == 'POST':
        subcat.Subcat_Name = request.POST.get('subcategory_name')
        subcat.Subcat_Desc = request.POST.get('subcategory_desc')

        # Check if a file is uploaded
        if 'subcategory_image' in request.FILES:
            subcat.Subcat_Img = request.FILES.get('subcategory_image')

        subcat.save()
        return redirect(managesubcat)  # Redirect to the managesubcat URL

    return render(request, 'managesubcategory.html')

def homepg(request):
    categories = tbl_category.objects.all() 
    return render(request, 'homepage.html', {'categories': categories})

def loginverify(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = tbl_login.objects.get(username=username)
            if user.password != password:
                return render(request, 'login.html', {'error_message': 'Invalid password'})
        except tbl_login.DoesNotExist:
            return render(request, 'login.html', {'error_message': 'Invalid username and password'})
        
        return redirect(homepg)  
    else:
        return HttpResponse("Method not allowed")
 