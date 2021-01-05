"""OnlinePropertySales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView,DetailView,UpdateView,ListView,DeleteView

from app import views
from app.models import CreatePlotModel,EmployeeModel,SalesModel,Login,EmployeeModels

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="signin1.html")),
    path('signin/', TemplateView.as_view(template_name="signin1.html")),
    path('usercheck/',views.userCheck),
    #path('hidden/',views.getUser),
    path('createplot/',views.CreatePlot.as_view()),
    path('home/',views.homeView,name='home'),
    path('viewplot/',TemplateView.as_view(template_name='potid.html'),name="viewplot"),
    # path('viewallplots/',views.ViewAllPlots.as_view(),name="viewallplots"),
    path('viewallplots/',views.ViewallPlots,name="viewallplots"),
    path('getplot/',views.ViewPlot.as_view()),
    path('plotdetails<int:pk>/',DetailView.as_view(template_name="detialplot.html",model=CreatePlotModel)),
    path('editplot/',views.editPlot),
    path('plotedit/',views.updatePlot),
    path('updateplot/',views.updatePlots),
    path('deleteplot/',views.deletePlot,name="deleteplot"),
    path('addappartment/',views.AddAppartment.as_view()),
    path('viewappartments/',views.ViewAppartments.as_view()),
    path('addemployee/',views.AddEmployee.as_view()),
    path('viewemp/',ListView.as_view(template_name="allemp.html",model=EmployeeModels)),
    path('soldplots/',views.soldPlots),
    path('reservedplots/',views.reservedPlots),
    path('vacantplots/',views.vacantPlots),
    path('saleentry/',TemplateView.as_view(template_name="saleentry.html")),
    path('storesales/',views.storeSales),
    path('altersale/',TemplateView.as_view(template_name="updatesaleid.html")),
    path('updatesales/',views.UpdateSales.as_view()),
    # path('viewsale/',ListView.as_view(template_name="allsales.html",model=SalesModel,content_type="allsale"),name="viewsale"),
    path('viewsale/',ListView.as_view(template_name="allsales.html",model=SalesModel),name="viewsale"),
    path('adduser/',views.AddUser.as_view()),
    path('viewusers/',views.ViewUsers.as_view()),
    path('deleteuser/',views.deleteUser),
    path('deleteuserdetails/',views.DeleteUser.as_view()),
    # path('userdelete<str:pk>/',views.DeleteUser.as_view(),name="userdelete"),
    # path('userdelete/',views.userDelete,name="userdelete"),
    path('makepayment/',views.makePayment),
    path('payview/',views.payView),
    path('paymoney/',views.payMoney),
    path('changepw/',TemplateView.as_view(template_name="changepw.html"),name="chngpw"),
    path('changepassword/',views.changePassword),
    path('logout/',views.logOut),
    path('sundrydebit/',views.sundryDebit),
    path('sundrycredit/',views.sundryCredit),
    path('allpayments/',ListView.as_view(template_name="allpays.html",model=SalesModel)),
    path('about/',views.about)




]
