from django.db import models

class tbl_login(models.Model):
    username = models.CharField(max_length=120, primary_key=True)
    password = models.CharField(max_length=25)
    user_type = models.CharField(max_length=50)
    join_date = models.DateField(null=True)

class tbl_customer(models.Model):
    username = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    Cust_Phno = models.CharField(max_length=120)
    Cust_Fname = models.CharField(max_length=150)
    Cust_Mname = models.CharField(max_length=150)
    Cust_Lname = models.CharField(max_length=150)
    Cust_Dob = models.CharField(max_length=150)
    Cust_Gender = models.CharField(max_length=150)
    Cust_Dist = models.CharField(max_length=150)
    Cust_City = models.CharField(max_length=150)
    Cust_Pin = models.CharField(max_length=150)
    Cust_Status = models.IntegerField(default=0)

class tbl_staff(models.Model):
    username = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    Staff_Phno = models.CharField(max_length=120)
    Staff_Fname = models.CharField(max_length=150)
    Staff_Mname = models.CharField(max_length=150)
    Staff_Lname = models.CharField(max_length=150)
    Staff_Dob = models.CharField(max_length=150)
    Staff_Join = models.CharField(max_length=150)
    Staff_Gender = models.CharField(max_length=150)
    Staff_Dist = models.CharField(max_length=150)
    Staff_City = models.CharField(max_length=150)
    Staff_Designation = models.CharField(max_length=150)
    Staff_Status = models.IntegerField(default=0)

class tbl_owner(models.Model):
    username = models.ForeignKey(tbl_login, on_delete=models.CASCADE)
    Owner_Phno = models.CharField(max_length=120)
    Owner_Fname = models.CharField(max_length=150)
    Owner_Mname = models.CharField(max_length=150)
    Owner_Lname = models.CharField(max_length=150)
    Owner_Dob = models.CharField(max_length=150)
    Owner_Gender = models.CharField(max_length=150)
    Owner_Dist = models.CharField(max_length=150)
    Owner_City = models.CharField(max_length=150)
    Owner_Pin = models.CharField(max_length=150)
    Owner_Status = models.IntegerField(default=0)

class tbl_category(models.Model):
    Cat_Name=models.CharField(max_length=120)
    Cat_Desc=models.CharField(max_length=255)
    Cat_Img=models.ImageField(upload_to='cat_images/', null=True, blank=True)

class tbl_subcategory(models.Model):
    Cat_id = models.ForeignKey(tbl_category, on_delete=models.CASCADE, db_column='Cat_id')
    Subcat_Name=models.CharField(max_length=120)
    Subcat_Desc=models.CharField(max_length=255)
    Subcat_Img=models.ImageField(upload_to='subcat_images/', null=True, blank=True)

class tbl_card(models.Model):
    Card_Number=models.CharField(max_length=120)
    Card_Name=models.CharField(max_length=120)
    Card_Date=models.CharField(max_length=120)
    Card_Cust=models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    Card_Status=models.CharField(max_length=120)
    Card_Cvv=models.CharField(max_length=120)

class tbl_room(models.Model):
    Room_Number = models.CharField(max_length=120)
    Subcat_id = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
    Room_Rent = models.DecimalField(max_digits=5, decimal_places=0)
    Room_Desc = models.CharField(max_length=255)
    Room_Status = models.CharField(max_length=120)
    Room_City = models.CharField(max_length=255)
    Room_District = models.CharField(max_length=255)
    Square_Feet = models.PositiveIntegerField()
    Room_Image = models.ImageField(upload_to='room_images/')

class tbl_booking(models.Model):
    Cust_id=models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    Room_id=models.ForeignKey(tbl_room, on_delete=models.CASCADE)
    Booking_date = models.DateField()
    Total_price = models.DecimalField(max_digits=5, decimal_places=0)
    Booking_Status = models.IntegerField(default=0)

class tbl_payment(models.Model):
    Booking_id=models.ForeignKey(tbl_booking, on_delete=models.CASCADE)
    Cust_id=models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    Card_id = models.ForeignKey(tbl_card, on_delete=models.CASCADE)
    Payment_date = models.DateField()
    Total_price = models.DecimalField(max_digits=5, decimal_places=0)
    Status = models.IntegerField(default=0)

class tbl_feedback(models.Model):
    Cust_id=models.ForeignKey(tbl_customer, on_delete=models.CASCADE)
    Date = models.DateField()
    Room_Rating=models.CharField(max_length=120)
    Service_Rating=models.CharField(max_length=120)
    Comment=models.CharField(max_length=255)
    Status = models.IntegerField(default=0)

class tbl_maintenance(models.Model):
    Maintenance_name=models.CharField(max_length=120)
    Maintenance_desc=models.CharField(max_length=255)
    Staff_id=models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    Status = models.IntegerField(default=0)

class tbl_maintenance_assign(models.Model):
    Maintenance_id=models.ForeignKey(tbl_maintenance, on_delete=models.CASCADE)
    Room_id=models.ForeignKey(tbl_room, on_delete=models.CASCADE)   
    Staff_id=models.ForeignKey(tbl_staff, on_delete=models.CASCADE)
    Date=models.CharField(max_length=120)
    Status = models.IntegerField(default=0)