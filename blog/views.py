from django.shortcuts import render , get_object_or_404
from .models import Blog

def all_blog(request):
   blogs = Blog.objects.order_by('-date')

   return render(request ,'blog/blog.html' ,{'blogs' : blogs})

def some_blog(request ,blog_id):
   blog = get_object_or_404(Blog ,pk = blog_id)

   return render(request ,'blog/someblog.html',{'blog':blog})