from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import generics
from .models import Image
from django.views.generic import ListView


def index(request):
    if request.method == 'POST':
        form = Image(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/image/") 
    else:
        form = Image
    return render(request, 'index.html')

def Display_Image(request):
    if request.method=="GET":
        pics=Image.objects.all()
        return render(request, 'index.html')       


global data;
data=['test']
# Create your views here.

class PersonView(APIView):

    def get(self,request, fromat=None):
        message={
            'Response': 200 ,
            'Message': 'Welcome to EZ',
            'data':data
        }

        return Response(message)

    def post(self,request, fromat=None):
        datam=request.data
        name=datam.get('Name', None)
        data.append(name)
        message={
            'Response': 200 ,
            'Message': 'Welcome to EZ',
            'data':data
        }

        return Response(message)
    
   
from .serializer import DummySerializer   

class Details(generics.CreateAPIView):

    serializer_class= DummySerializer

    def create(self,request,*args, **kwargs):
        try:
            name=request.data.get('name')
            age=request.data.get('age')
            address=request.data.get('address')
            city=request.data.get('city')
            mobile_no=request.data.get('mobile_no')
            return super().create(request,*args,**kwargs)

        except Exception as e:
            return Response({
                "Message":"Done"
            })
