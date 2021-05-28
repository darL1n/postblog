from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import PostForm, EditForm, ConatactForm, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def frontpage(request):
    posts = Post.objects.filter(status=1)
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
   
    context = {
        'posts': posts,
        
    }
    return render(request, 'frontpage.html', context)


def post_detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = Comment(request.POST)
        if form.is_valid():
           obj = form.save(commit=False)
           obj.post = post
           obj.save()
           return redirect('post_detail', post.category.slug, post.slug)
    else:
        form = Comment()

    try:
        next_post = post.get_next_by_date_added()
    except Post.DoesNotExist:
        next_post = None
    try:
        previous_post = post.get_previous_by_date_added()
    except Post.DoesNotExist:
            previous_post = None

    context = {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
        'form': form
    
     }
    

    return render(request, 'post_detail.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(parent=None)

    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'category_detail.html', context)


def about(request):
    return render(request, 'about.html')


def asd(request):
    return render(request, 'asd.html')


def contact(request):
    if request.method == 'POST':
        form = ConatactForm(request.POST)
        if form.is_valid():
            mail=send_mail(form.cleaned_data['subject'], form.cleaned_data['body'], 'gamer97abk@mail.ru', ['davinci97abk@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, 'Сообщение отправлено!')
                return redirect('contact')
            else:
                messages.error(request, 'Сбой')
        else:
            messages.error(request, 'Сообщение не отправленно! Вы не правильно ввели каптчу!')
    else:
        form = ConatactForm()
    return render(request, 'contact.html', {"form":form})


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(title__icontains=query) | Q(snippet__icontains=query))


    context = {
        'query': query,
        'posts': posts
    }
    return render(request, 'search.html', context)

def books(request):
    return render(request, 'books.html')

def documentation(request):
    return render(request, 'documentation.html')

def LikeView(request, pk):
    post = Post.objects.get(id=pk)
    post.likes.add(request.user)
    return redirect('post_detail', post.category.slug, post.slug)

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name= 'add_post.html'
    success_url = reverse_lazy('frontpage')

class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = EditForm
    #fields = ['title', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('frontpage')