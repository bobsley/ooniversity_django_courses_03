# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from coaches.models import Coach

class Course(models.Model):
	name = models.CharField(max_length = 255, help_text = u'название')
	short_description = models.CharField(max_length = 255, help_text = u'краткое описание', null = True, blank = True)
	description = models.TextField(help_text = u'полное описание', null = True, blank = True)
	coach = models.ForeignKey(Coach, related_name='coach_courses', null = True, blank = True)
	assistant = models.ForeignKey(Coach, related_name='assistant_courses', null = True, blank = True)

	def __unicode__(self):
		return self.name

class Lesson(models.Model):
	subject = models.CharField(max_length = 255)
	description = models.TextField()
	course = models.ForeignKey(Course)
	order = models.PositiveIntegerField()
	def __unicode__(self):
		return self.subject
	#def get_absolute_url(self):
	#	return reverse('courses:detail', {'pk':self.course.pk})

