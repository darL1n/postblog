from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Опубликованно")
)

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Родитель')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0, verbose_name='Сортировка по счету (навбар)')

    class Meta:
        verbose_name_plural = 'Категории'
        ordering = ('ordering',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, verbose_name='Категория')
    parent = models.ForeignKey('self', related_name='variants', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Сопутсвующий')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255)
    body = RichTextField(verbose_name=("Тело Статьи"), blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата Публикации')
    is_featured = models.BooleanField(default=False, verbose_name='В Рекомендации')
    header_image = models.ImageField(verbose_name=("Заглавное Изображение"), null=True, blank=True, upload_to="images/" )
    snippet = models.CharField(verbose_name=("Фрагмент Статьи"), max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_post')

    class Meta:
        verbose_name_plural = 'Статьи'
        ordering = ('-date_added',)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/%s/' % (self.category.slug, self.slug)

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(verbose_name=("Биография"))
    profile_pic = models.ImageField(verbose_name=("Фото профиля"), null=True, blank=True, upload_to="images/profile/", )
    website_url = models.CharField(verbose_name=("Сайт"), max_length=200, null=True, blank=True)
    instagram_url = models.CharField(verbose_name=("Instagram"), max_length=200, null=True, blank=True)
    twitter_url = models.CharField(verbose_name=("Twitter"),max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(verbose_name=("Призвание"), max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(verbose_name=("Date of birth"), blank=True, null=True)
    country = CountryField(blank=True, null=True) 
    age = models.IntegerField(verbose_name=("Возраст"), null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('frontpage')

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80, verbose_name="Имя")
    body = models.TextField(verbose_name="Текст")
    date_added = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        ordering = ['date_added']
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)