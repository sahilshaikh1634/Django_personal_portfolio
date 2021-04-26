from django.shortcuts import render, get_object_or_404
from .models import blog


def blogs(request):


    blogs = blog.objects.order_by('-date')


    return render(request,"blog/all_blogs.html", { 'blogs':blogs })

def details(request,blog_id):

    blo = get_object_or_404(blog, pk=blog_id)

    return render(request, 'blog/detail.html', { 'blog':blo })
