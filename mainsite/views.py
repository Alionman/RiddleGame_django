from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from mainsite.models import Telephone
from mainsite.models import Count
import random
# Create your views here.

def homepage(request):
    Count.objects.create(count=1)
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

def Add(request):
    if request.GET:
        Telephone.objects.create(number= request.GET['tel'], score=request.GET['tyNum'])
    return HttpResponse("submit successed")

def luckydraw(request):
    template = get_template('lucky.html')
    html = template.render(locals())
    return HttpResponse(html)

def luckynumber(request):
    context = {}
    numrange = range(1,1693)
    numlist = random.sample(numrange, 3)
    context['telNum1'] = Telephone.objects.get(id=numlist[0]).number
    context['telNum2'] = Telephone.objects.get(id=numlist[1]).number
    context['telNum3'] = Telephone.objects.get(id=numlist[2]).number
    return render(request, 'lucky.html', context) 
