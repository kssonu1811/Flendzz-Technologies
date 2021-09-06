from flendzz.models import student
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from flendzz.serializers import studentSerializers
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import student
from .forms import Orderform




def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        date_of_birth = request.POST['date_of_birth']
        marks = request.POST['marks']
        Student = student(name=name,roll_number=roll_number,date_of_birth=date_of_birth,marks=marks)
        Student.save()
        messages.success(request,'Thankyou, Your request has been submitted.')
    return render(request, 'phase1/home.html')

def add(request):
    if request.method == 'POST':
        name = request.POST['name']
        roll_number = request.POST['roll_number']
        date_of_birth = request.POST['date_of_birth']
        marks = request.POST['marks']
        Student = student(name=name,roll_number=roll_number,date_of_birth=date_of_birth,marks=marks)
        Student.save()
        messages.success(request,'Thankyou, Your request has been submitted.')
    return render(request, 'phase1/add.html',)

def dashboard(request):
    students = student.objects.all()
    data ={
        "student" : students
    }
    return render(request, 'phase1/dashboard.html', data)

def details(request,pk):
    single_app = get_object_or_404(student, pk=pk)
    context ={
        "single_app":single_app
    }
    return render(request, 'phase1/detail.html', context)

def update(request, pk):
    context ={}
    obj = get_object_or_404(student, pk = pk )
    form = Orderform(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context["form"] = form
    return render(request, 'phase1/update.html',context,)

def deleteorder(request, pk):
    context ={}
    obj = get_object_or_404(student, pk = pk )
    if request.method == "POST":
        obj.delete()
        return redirect('dashboard')
    return render(request, 'phase1/delete.html',context)

class studentapi(APIView):
    def get(self, request, pk=None , format=None):
        id = pk
        if id is not None:
            stu = student.objects.get(id=id)
            serializer = studentSerializers(stu)
            return Response(serializer.data)
        stu = student.objects.all()
        serializer = studentSerializers(stu, many =True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save
            return Response({'msg':'Data Saved'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        id = pk
        stu = student.objects.get(pk=id)
        serializer = studentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def patch(self, request, pk, format=None):
        id = pk
        stu = student.objects.get(pk=id)
        serializer = studentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    def delete(self, request, pk, format=None):
        id = pk
        stu = student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'data Deleted'})


