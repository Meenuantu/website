from django.shortcuts import render
from .models import place,team
# Create your views here.
def demo(request):
    var1=place.objects.all()
    var2=team.objects.all()

    return render(request, 'index.html',{'result': var1,'result2':var2})

