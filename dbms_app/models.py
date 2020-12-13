# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    user_type = models.CharField( max_length=255, default = 'C')
    name = models.CharField(max_length=255, default='') 
    address = models.CharField(max_length=255, default='')

    def __str__(self):
            return self.user.username

class Assembling(models.Model):
    productid = models.OneToOneField('Product', db_column='ProductId', primary_key=True,on_delete = models.CASCADE)  # Field name made lowercase.
    employeeid = models.ForeignKey('Employee',  db_column='EmployeeId',on_delete = models.CASCADE)  # Field name made lowercase.
    done = models.BooleanField(default=False)

    class Meta:
        db_table = 'assembling'
        unique_together = (('productid', 'employeeid'),)


class Customer(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    sales_personid = models.ForeignKey('SalesPerson',  db_column='Sales_personId', blank=True, null=True, on_delete = models.CASCADE)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'customer'

    def __str__(self):
            return self.name


class Employee(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'employee'
    def __str__(self):
            return self.name


class Orderline(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    customerid = models.ForeignKey(Customer,  db_column='CustomerId', blank=True, null=True,on_delete = models.CASCADE)  # Field name made lowercase.
    qty = models.IntegerField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'orderline'
    def __str__(self):
            return self.customerid.name


class Part(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    supplierid = models.ForeignKey('Supplier',  db_column='SupplierId', blank=True, null=True,on_delete = models.CASCADE)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    supplied = models.BooleanField(default=False)

    class Meta:
        db_table = 'part'
    def __str__(self):
            return self.name


class Product(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    orderid = models.ForeignKey(Orderline,  db_column='OrderId',on_delete = models.CASCADE)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(default = 0)

    class Meta:
        db_table = 'product'
        unique_together = (('id', 'orderid'),)
    def __str__(self):
            return self.title


class ProductPart(models.Model):
    productid = models.ForeignKey(Product,  db_column='ProductId', on_delete = models.CASCADE)  # Field name made lowercase.
    partid = models.ForeignKey(Part,  db_column='PartId',on_delete = models.CASCADE)  # Field name made lowercase.

    class Meta:
        db_table = 'product_part'


class SalesPerson(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'sales_person'
    def __str__(self):
            return self.name


class Supplier(models.Model):
    id = models.IntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'supplier'
    def __str__(self):
            return self.name
