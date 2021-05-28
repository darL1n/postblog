from django import forms
from .models import Post, Comment
from captcha.fields import CaptchaField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category','snippet', 'header_image', 'body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id': 'elder', 'type': 'hidden'}), 
            'category': forms.Select(attrs={'class': 'form-control'}),       
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title' , 'snippet' , 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }



class ConatactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class': 'form-control', "rows":5}))
    captcha = CaptchaField()

class Comment(forms.ModelForm):
   class Meta:
       model = Comment
       fields = ('name', 'body') 

       widgets = {

            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
          }
