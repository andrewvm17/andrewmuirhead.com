from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('blog/', views.blogs, name='blog-blog'),
    path("post/<int:pk>/", views.postdetail, name = 'post_detail'),
]

urlpatterns += staticfiles_urlpatterns()