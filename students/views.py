# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import messages
from students.models import Student
from courses.models import Course
from students.forms import StudentModelForm

def list_view(request):
	if request.GET.get('course_id'):
		student = Student.objects.filter(courses = request.GET.get('course_id'))
	else:
		student = Student.objects.all()
	return render(request, 'students/list.html', {'students': student})

def detail(request, student_id):
	student = Student.objects.get(id=student_id)
	return render(request, 'students/detail.html', {'student':student})

def create(request):
	if request.method == "POST":
		form = StudentModelForm(request.POST)
		if form.is_valid():
			stud = form.save()
			mes = u'Студент %s %s успешно добавлен' %(stud.name, stud.surname)
			messages.success(request, mes)
			return redirect("students:list_view")
	else:
		form = StudentModelForm()
	return render(request, "students/add.html", {'form':form})

def edit(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		form = StudentModelForm(request.POST, instance=student)
		if form.is_valid():
			stud = form.save()
			mes = u'Данные изменены'
			messages.success(request, mes)
	else:
		form = StudentModelForm(instance=student)
	return render(request, "students/edit.html", {'form':form})
	
def remove(request, student_id):
	student = Student.objects.get(id=student_id)
	if request.method == "POST":
		student.delete()
		mes = u'Студент %s %s был удалён' %(student.name, student.surname)
		messages.success(request, mes)
		return redirect("students:list_view")

	return render(request, "students/remove.html", {'name':student.name, 'surname':student.surname})
	

