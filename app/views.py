from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Login, CreatePlotModel,AppartmentModel,EmployeeModel,SalesModel,EmployeeModels
from django.views.generic import CreateView, DetailView, ListView, TemplateView,UpdateView,DeleteView
from django.db.models import Q
from django.contrib.auth import logout



def getUser(request):
    user = request.session['token']
    print(user)

    return user


def userCheck(request):
    uname = request.POST.get("uname")
    upass = request.POST.get("upass")
    request.session['token'] = uname
    # request.session.set_expiry(15)
    # request.session.clear_expired()


    qs = Login.objects.filter(username=uname, password=upass)
    for x in qs:
        if x.username == uname and x.password == upass:
            return render(request, "home.html", {"name": getUser(request)})
        else:
            return render(request, "signinback.html", {"msg": "Invalid Credentials"})
    else:
        return render(request, "signinback.html", {"msg": "Invalid Credentials"})




class CreatePlot(SuccessMessageMixin,CreateView):
    template_name = "plot.html"
    model = CreatePlotModel
    fields = ('plotno', 'roadno', 'surveyno', 'costpersqyard', 'otherexpences', 'boundaries', 'facing', 'status','totalcost')
    success_url = "/home/"
    success_message = "Plot Added Successfully"


class ViewPlot(View):
    def post(self,request):
        id=request.POST.get("pid")
        qs=CreatePlotModel.objects.filter(plotno=id)
        if not qs:
            return render(request,"potid.html",{"msg":"Invaild plot no"})
        else:
            return render(request,"viewplot.html",{"data":qs,"name":getUser(request)})

class DeleteUser(View):
    def post(self,request):
        na = request.POST.get("un")
        Login.objects.filter(username=na).delete()
        messages.success(request, "user deleted successfully")
        return redirect('home')


def editPlot(request):

    return render(request,"plotedit.html",{"name":getUser(request)})


def updatePlot(request):
    pid=request.POST.get("plotid")
    qs=CreatePlotModel.objects.filter(plotno=pid)
    if qs[0].plotno:
      return render(request,"updateplot.html",{"data":qs,"name":getUser(request)})
    else:
        return render(request, "plotedit.html",{"msg":"Invalid Id No"})


def updatePlots(request):
    pid=request.POST.get("pid")
    rid=request.POST.get("rid")
    sid=request.POST.get("sid")
    cps=request.POST.get("cps")
    oe=request.POST.get("oe")
    bou=request.POST.get("bou")
    face=request.POST.get("face")
    status=request.POST.get("status")
    e=CreatePlotModel(plotno=pid,roadno=rid,surveyno=sid,costpersqyard=cps,otherexpences=oe,boundaries=bou,facing=face,status=status)
    e.save()
    return render(request,"home.html",{"msg":"Updated Successfully","name":getUser(request)})


class AddAppartment(SuccessMessageMixin,CreateView):
    template_name = "appartment.html"
    model = AppartmentModel
    fields = ('appartmentno','flatno','name','address','noofflats')
    success_url = "/home/"
    success_message = "Appartment Added Successfully"


class ViewAppartments(ListView):
    template_name = "viewappartment.html"
    model = AppartmentModel



class AddEmployee(SuccessMessageMixin,CreateView):
    template_name = "addemp.html"
    model = EmployeeModels
    fields = ('name','empid','mail','location','doj','role','qualification','remarks')
    success_url = "/home/"
    success_message = "Employee Register Succesfully"


def soldPlots(request):
    #qs=CreatePlotModel.objects.all()
    #st="sold"
    #qs1=CreatePlotModel.objects.filter(status="sold")
    qs1 = CreatePlotModel.objects.filter(status="sold")
    print(qs1)
    return render(request,"sold.html",{"data":qs1,"name":"admin"})


def reservedPlots(request):
    qs1 = CreatePlotModel.objects.filter(status="reserve")
    return render(request,"reserve.html",{"data":qs1,"name":getUser(request)})


def vacantPlots(request):
    qs1 = CreatePlotModel.objects.filter(status="vacant")
    return render(request, 'vacant.html', {"data": qs1,"name":getUser(request)})


def storeSales(request):
    pno=request.POST.get("pno")
    sale=request.POST.get("sale")
    saledate=request.POST.get("saledate")
    soldto=request.POST.get("soldto")
    advance=request.POST.get("advance")
    balance=request.POST.get("balance")
    installment=request.POST.get("installment")
    e=SalesModel(plotno=pno,salevalue=sale,dateofsale=saledate,advance=advance,balance=balance,installment=installment,soldto=soldto)
    e.save()
    return render(request,"home.html",{"msg":"Plot is stored","name":getUser(request)})


class UpdateSales(View):
    def post(self,request):
        id=request.POST.get("saleid")
        qs=SalesModel.objects.filter(plotno=id)
        if not qs:
            return render(request,"updatesaleid.html",{"msg":"Invaild plot no","name":"admin"})
        else:
            return render(request,"updatesales.html",{"data":qs,"name":getUser(request)})


class AddUser(SuccessMessageMixin,CreateView):
    template_name = "adduser.html"
    model = Login
    fields = ('username', 'password', 'type', )
    success_url = "/home/"
    success_message = "User Added Successfully"


class ViewUsers(SuccessMessageMixin,ListView):
    template_name = "viewusers.html"
    model = Login



# class DeleteUser(SuccessMessageMixin,DeleteView):
#     template_name = "delete.html"
#     model = Login
#     success_url = "/home/"
#     success_message = "Deleted User Successfully"


def deleteUser(request):
    qs=Login.objects.all()
    return render(request,"deleteuser.html",{"data":qs,"name":getUser(request)})


# def userDelete(request):
#     user=request.POST.get("user")
#     Login.objects.filter(username=user).delete()
#     return render(request,"home.html",{"deleteuser":"User deleted successfully","name":getUser(request)})


def makePayment(request):
    qs=SalesModel.objects.filter(~Q(balance=0))
    return render(request,"payment.html",{"data":qs,"name":getUser(request)})


def payView(request):
    pay=request.POST.get("pay")
    qs=SalesModel.objects.filter(plotno=pay)
    return render(request,"payview.html",{"data":qs,"name":getUser(request)})


def payMoney(request):
    pno=request.POST.get("pno")
    sale=request.POST.get("sale")
    blc=request.POST.get("balance")
    amount=request.POST.get("amount")
    check=request.POST.get("check")
    payee=request.POST.get("payeename")
    saledate=request.POST.get("saledate")
    installment=request.POST.get("installment")
    e1= SalesModel(plotno=pno,salevalue=sale,balance=blc,advance=amount,check=check,payeename=payee,dateofsale=saledate,installment=installment)
    e1.save()
    return render(request,"home.html",{"msg":"payed plot"+pno,"name":getUser(request)})


def changePassword(request):
    uname= request.POST.get("username")
    oldpw= request.POST.get("old")
    newpw= request.POST.get("new")
    type=request.POST.get("type")
    qs=Login.objects.filter(username=uname)
    for x in qs:
        if x.username == uname and x.password == oldpw:
            Login(username=uname,password=newpw,type=type).save()
            return render(request,"home.html",{"msg":"successfully Change ur Password","name":getUser(request)})
        else:
            return render(request,"changepw.html",{"msg":"invalid user","name":getUser(request)})
    else:
        return redirect("chngpw")


def logOut(request):
    #del request.session['token']
    try:
        del request.session['token']
    except KeyError:
        pass
    # return HttpResponse("You're logged out.")
    return render(request, "signin1.html", {"msg": "Sucessfully Logged out"})


def sundryDebit(request):
    qs = SalesModel.objects.filter(balance=0)
    return render(request,"sdebit.html",{"data":qs,"name":getUser(request)})


def sundryCredit(request):
    qs = SalesModel.objects.filter(~Q(balance=0))
    return render(request,"scredit.html",{"data":qs,"name":getUser(request)})


def homeView(request):
    # res = request.session.get("token","Unavailable")

    return render(request,"home.html",{"name":getUser(request),"x":Login.objects.all()})
    # return HttpResponse(res)


def about(request):
    return render(request, "about.html", {"name": getUser(request)})


# class ViewAllPlots(ListView):
#     template_name = "Viewallplots.html"
#     model = CreatePlotModel
#     queryset = CreatePlotModel.objects.values('plotno','surveyno','costpersqyard','roadno','totalcost')
#     def post(self,request):
#         return getUser(request)


def deletePlot(request):
    num = request.GET.get("no")
    CreatePlotModel.objects.filter(plotno=num).delete()
    messages.success(request,"Plot deleted successfully")
    return redirect('viewallplots')


def ViewallPlots(request):
    return render(request,"Viewallplots.html",{"info":CreatePlotModel.objects.all(),"name":getUser(request)})