from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    return render(request, 'blog/homepage.html') # "/" different for the mac and window.. 

       
blogs = [
        {
            "title1": "This is blog one title",
            "description": "lorem ipsum dolor sit amet denfe enfefn enfenn fenfjen ejnf",
            "id": 1,
            "slug": "title-1",
        },
        {
            "title1": "This is blog two title",
            "description": "two lorem ipsum dolor sit amet denfe enfefn enfenn fenfjen einf",
            "id": 2,
            "slug": "title-2",
        },
        {
            "title1": "This is blog three title",
            "description": "three lorem ipsum dolor sit amet denfe enfefn enfenn fenfjen einf",
            "id": 3,
            "slug": "title-3"
        }
    ] 

def blog(request):
 #blog = ['Blog 1', 'Blog 2', 'Blog 3', 'Blog 4', 'blog 5']
   
    context = {
        'all_blog':blogs,
        'project_name': "This is the project name!"
    }
   
    return render(request, 'blog/blog_list.html', context)


def blog_post(request, slug):

    blog_post = [blog for blog in blogs if blog['slug'] == slug]

    context = {
        'blog_post': blog_post[0]
    }
    return render(request, 'blog/blog_post.html', context)

      
def example_route(request):
    context = {
    "project_name": "This is Youtube.com",
    "greetings": "Hello World !!! ",
    "fruit_list": ["Apple", "Banana", "Mango", "Orange", "Papaya"],
    "is_user_logged_in": True
    }

    return render(request, 'blog/example_route.html', context)
    

