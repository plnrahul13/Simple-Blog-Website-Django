from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import PersonDetails,Blogs

def index(request):
	all_blogs=Blogs.objects.all()
	template=loader.get_template('topic/index.html')
	return HttpResponse(template.render({'all_blogs':all_blogs},request))

def detail(request,user_id):
	person=PersonDetails.objects.get(pk=user_id)
	all_blogs=person.blogs_set.all()
	template=loader.get_template('topic/detail.html')
	return HttpResponse(template.render({
		'person':person,
		'all_blogs':all_blogs,
		},request))

def content(request,user_id,blog_id):
	blog=Blogs.objects.get(pk=blog_id)
	template=loader.get_template('topic/content.html')
	return HttpResponse(template.render({'blog':blog},request))

def allbloggers(request):
	all_people=PersonDetails.objects.all()
	template=loader.get_template('topic/bloggers.html')
	return HttpResponse(template.render({'all_people':all_people},request))

def addblogs(request):
	template=loader.get_template('topic/addblog.html')
	return HttpResponse(template.render({},request))

def addblog(request):
	if PersonDetails.objects.filter(name=request.POST['name'],age=request.POST['age'],profession=request.POST['profession']):
		person=PersonDetails.objects.get(name=request.POST['name'])
	else:
		person=PersonDetails(name=request.POST['name'],age=request.POST['age'],profession=request.POST['profession'])
		person.save()
	blogs=Blogs(author=person,title=request.POST['title'],content=request.POST['content'])
	blogs.save()
	all_blogs=Blogs.objects.all()
	template=loader.get_template('topic/index.html')
	return HttpResponse(template.render({'all_blogs':all_blogs},request))