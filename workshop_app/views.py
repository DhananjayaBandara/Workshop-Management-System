from django.shortcuts import render, get_object_or_404, redirect
from .models import Workshop
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import WorkshopSerializer

def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, 'workshop_list.html', {'workshops': workshops})

def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    return render(request, 'workshop_detail.html', {'workshop': workshop})

def workshop_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        trainer = request.POST['trainer']
        date = request.POST['date']
        time = request.POST['time']
        location = request.POST['location']
        target_audience = request.POST['target_audience']
        Workshop.objects.create(
            title=title, description=description, trainer=trainer,
            date=date, time=time, location=location, target_audience=target_audience
        )
        return redirect('workshop_list')
    return render(request, 'workshop_form.html')

from django.core.exceptions import ValidationError

def workshop_update(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if request.method == 'POST':
        try:
            workshop.title = request.POST['title']
            workshop.description = request.POST['description']
            workshop.trainer = request.POST['trainer']
            workshop.date = request.POST['date']  
            workshop.time = request.POST['time']  
            workshop.location = request.POST['location']
            workshop.target_audience = request.POST['target_audience']
            workshop.full_clean()  # Validate the model fields
            workshop.save()
            return redirect('workshop_list')
        except ValidationError as e:
            return render(request, 'workshop_form.html', {
                'workshop': workshop,
                'errors': e.message_dict
            })
    return render(request, 'workshop_form.html', {'workshop': workshop})

def workshop_delete(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if request.method == 'POST':
        workshop.delete()
        return redirect('workshop_list')
    return render(request, 'workshop_confirm_delete.html', {'workshop': workshop})

@api_view(['GET', 'POST'])
def workshop_list_api(request):
    if request.method == 'GET':
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = WorkshopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def workshop_detail_api(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    if request.method == 'GET':
        serializer = WorkshopSerializer(workshop)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = WorkshopSerializer(workshop, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        workshop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
