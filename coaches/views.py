from django.shortcuts import render, get_object_or_404
from coaches.models import Coach
from courses.models import Course

def detail(request, teacher_id):
	teacher =  get_object_or_404(Coach, id=teacher_id)
	return render(request, 'coaches/detail.html', {'teacher':teacher})
