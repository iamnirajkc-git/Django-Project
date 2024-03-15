from django.urls import path
#from .views import homepage, blog
from blog.views import homepage, blog, example_route, blog_post

app_name ="blog"



urlpatterns = [
    path('', homepage, name="homepage"),
    path('blog/', blog, name="blog_list"),
    #path('blog/<int:id>/', blog_post, name="blog_post"),
    path('blog/<str:slug>/', blog_post, name="blog_post"),
    
    path('example_route/', example_route, name="example_route"),
]

