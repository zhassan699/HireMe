from django.shortcuts import render
from hero.models import Hero
from client.models import Client
from .models import Job
from .serializer import *
from rest_framework import viewsets


# Create your views here.
class HeroListApi(viewsets.generics.ListAPIView):
    serializer_class = HeroSerializer

    def get_queryset(self):
        queryset = Hero.objects.all()
        job = self.request.query_params.get('job',None)
        size = self.request.query_params.get('page_size',None)
        count = self.request.query_params.get('page_number',None)
        
        if size and count is not None:
            queryset = Hero.objects.all()[((int(count)-1)*int(size)):int(count)*int(size)]
        if job is not None:
            queryset = Hero.objects.filter(job=job)
        return queryset

class HeroGetApi(viewsets.generics.RetrieveAPIView):
    serializer_class = HeroSerializer
    queryset = Hero.objects.all()

class JobsListApi(viewsets.generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()

class ClientGetApi(viewsets.generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

