from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
	"""
	This model used to create table for blog categories
	"""
	
	name = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'blog_category'


class Blog(models.Model):
	"""
	Tis model is used to create table for blogs
	"""
	
	status_choices = ((0, 'Inactive'), (1, 'Activate'), (2, 'Deleted'))
	title = models.CharField(max_length=255)
	content = RichTextField(null=True, blank=True)
	created_by = models.ForeignKey(User, null=True, blank=True)
	category = models.ForeignKey(Category, null=True, blank=True)
	status = models.IntegerField(max_length=1, choices=status_choices)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	
	def __unicode__(self):
		return self.title
		
	class Meta:
		db_table = 'blog_blog'


class BlogComment(models.Model):
	"""
	This table is used for creating blog comments
	"""
	
	status_choices = ((0, 'Inactive'), (1, 'Activate'), (2, 'Deleted'))
	blog = models.ForeignKey(Blog, null=True, blank=True )
	content = models.TextField(null=True, blank=True)
	created_by = models.ForeignKey(User, null=True, blank=True)
	status = models.IntegerField(max_length=1, choices=status_choices)
	created_at = models.DateTimeField()
	updated_at = models.DateTimeField()
	
	def __unicode__(self):
		return self.content
	
	class Meta:
		db_table = 'blog_comment'
	
