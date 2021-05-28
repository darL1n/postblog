from django.contrib import admin
from .models import Post, Category,Profile, Comment
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class PostAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','date_added')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Profile)
admin.site.register(Comment)
