"""ablog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewsSitemap, CategorySitemap, PostSitemap
from theblog.views import frontpage, about, contact, post_detail, category_detail, asd, AddPostView, UpdatePostView, DeletePostView,search, AddPostView, books, documentation,LikeView



sitemaps = {'static': StaticViewsSitemap, 'post': PostSitemap, 'category': CategorySitemap}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('captcha/', include('captcha.urls')),
    path('components/', include('components.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),    
    path('', frontpage, name='frontpage'),
    path('about', about, name='about'),
    path('contact/', contact, name='contact'),
    path('asd/', asd, name='asd'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('search/', search, name='search'),
    path('article/edit/<slug:slug>', UpdatePostView.as_view(), name='update_post'),
    path('article/<slug:slug>/delete', DeletePostView.as_view(), name='delete_post'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('components/', include('components.urls')),
    path('books/', books, name="books"),
    path('documentation/', documentation, name='documentation'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('<slug:category_slug>/<slug:slug>/', post_detail, name='post_detail'),
    path('<slug:slug>/', category_detail, name='category_detail'),  
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
