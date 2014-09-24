from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Category, Blog

# Create your views here.
def index(request):
	return render(request, 'home/index.html')
	
def contact(request):
	return render(request, 'home/contact.html')
	
def about(request):
	return render(request, 'home/about.html')

def projects(request):
	return render(request, 'home/projects.html')

def blogs(request, category=False, blog=False, search_text=''):
	category_name = False
	target = False
	categories = Category.objects.all()
	all_blogs = Blog.objects.all().order_by('created_at')
	
	# case when directly both category and blog id is passed
	if category and blog:
		category_name = Category.objects.get(id=category).name
		blogs = Blog.objects.filter(category_id=category, id=blog).order_by('created_at')
		target = 'Blog'
	# case when directly only category is passed
	elif category:
		category_name = Category.objects.get(id=category).name
		blogs = Blog.objects.filter(category_id=category).order_by('created_at')
	# case when search text is passed
	elif search_text:
		blogs = Blog.objects.filter(title__icontains=search_text).order_by('created_at')
	# case when nothing is passed	
	else:
		blogs = all_blogs

	return render(request, 'home/blogs.html',
						{'category': categories, 
						'blogs': blogs,
						'category_name': category_name,
						'all_blogs': all_blogs,
						'target': target,
						'search_text': search_text
						}
	)
