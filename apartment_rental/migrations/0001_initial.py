# Generated by Django 5.0.2 on 2024-02-12 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_login',
            fields=[
                ('username', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=25)),
                ('user_type', models.CharField(max_length=50)),
                ('join_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cust_Phno', models.CharField(max_length=120)),
                ('Cust_Fname', models.CharField(max_length=150)),
                ('Cust_Mname', models.CharField(max_length=150)),
                ('Cust_Lname', models.CharField(max_length=150)),
                ('Cust_Dob', models.CharField(max_length=150)),
                ('Cust_Gender', models.CharField(max_length=150)),
                ('Cust_Dist', models.CharField(max_length=150)),
                ('Cust_City', models.CharField(max_length=150)),
                ('Cust_Pin', models.CharField(max_length=150)),
                ('Cust_Status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment_rental.tbl_login')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Staff_Phno', models.CharField(max_length=120)),
                ('Staff_Fname', models.CharField(max_length=150)),
                ('Staff_Mname', models.CharField(max_length=150)),
                ('Staff_Lname', models.CharField(max_length=150)),
                ('Staff_Dob', models.CharField(max_length=150)),
                ('Staff_Gender', models.CharField(max_length=150)),
                ('Staff_Dist', models.CharField(max_length=150)),
                ('Staff_City', models.CharField(max_length=150)),
                ('Staff_Pin', models.CharField(max_length=150)),
                ('Staff_Status', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment_rental.tbl_login')),
            ],
        ),
    ]
