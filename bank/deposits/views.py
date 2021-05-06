
from django.shortcuts import render
from django.views.generic import View, ListView
from user.models import User
from django.http import HttpRequest, HttpResponse

def add_deposit(request):

    if request.method == 'POST':

        add_money = Deposit(
            deposit=request.POST['deposit'],
            term=request.POST['term'],
            rate=request.POST['rate'],
            interest=request.POST['interest']
        )

        add_money.save()

        context = {
            'add_money': add_money,
        }

        return render(
            template_name='deposit.html',
            request=request,
            context=context,

        )
def index(request):

     money = Deposit.objects.all()

     context = {
         'money': money,
     }

     return render(
         template_name='index.html',
         request=request,
         context=context,
     )
