from django.db import models
from OnlinePropertySales import settings

# Create your models here.
class Login(models.Model):
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=30)
    type=models.CharField(max_length=20,choices=(('admin','ADMIN'),('user','USER')))



class CreatePlotModel(models.Model):
    plotno=models.IntegerField(primary_key=True)
    roadno=models.IntegerField()
    surveyno=models.IntegerField()
    costpersqyard=models.DecimalField(max_digits=10,decimal_places=2)
    otherexpences=models.CharField(max_length=30)
    boundaries=models.CharField(max_length=200)
    facing=models.CharField(max_length=30,choices=(('east','EAST'),('west','WEST')))
    status=models.CharField(max_length=15,choices=(('vacant','VACANT'),('reserve','RESERVE'),('sold','SOLD')))
    totalcost=models.DecimalField(default=True,max_digits=10,decimal_places=2)


class AppartmentModel(models.Model):
    appartmentno=models.IntegerField(primary_key=True)
    flatno=models.IntegerField()
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=200)
    noofflats=models.IntegerField()



class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    empid = models.IntegerField()
    mail = models.EmailField(max_length=100)
    location = models.CharField(max_length=40)
    doj = models.DateField()
    role=models.CharField(max_length=30,choices=(('general manager','GENERAL MANAGER'),('acounts manager','ACOUNTS MANAGER'),('sales manager','SALES MANAGER'),
                                   ('sales representative','SALES REPRESENTATIVE'),('accountant','ACCOUNTANT'),('accounts assistance','ACCOUNTS ASSISTANCE'),
                                   ('clerk','CLERK'),('receptionist','RECEPTIONIST'),('security','SECURITY')))
    qualification=models.CharField(max_length=30)
    remarks=models.CharField(max_length=30)



class SalesModel(models.Model):
    plotno=models.IntegerField(primary_key=True)
    salevalue=models.DecimalField(max_digits=10,decimal_places=2)
    dateofsale=models.CharField(max_length=40)
    advance=models.DecimalField(max_digits=10,decimal_places=2)
    balance=models.DecimalField(max_digits=10,decimal_places=2)
    installment=models.CharField(max_length=10)
    soldto=models.CharField(max_length=30,default=True)
    check=models.CharField(max_length=30,default=True)
    payeename=models.CharField(max_length=30,default=True)

class EmployeeModels(models.Model):
    name = models.CharField(max_length=30)
    empid = models.IntegerField()
    mail = models.EmailField(max_length=100)
    location = models.CharField(max_length=40)
    doj = models.CharField(max_length=40)
    role=models.CharField(max_length=30,choices=(('general manager','GENERAL MANAGER'),('acounts manager','ACOUNTS MANAGER'),('sales manager','SALES MANAGER'),
                                   ('sales representative','SALES REPRESENTATIVE'),('accountant','ACCOUNTANT'),('accounts assistance','ACCOUNTS ASSISTANCE'),
                                   ('clerk','CLERK'),('receptionist','RECEPTIONIST'),('security','SECURITY')))
    qualification=models.CharField(max_length=30)
    remarks=models.CharField(max_length=30)

