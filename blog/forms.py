from django import forms
from blog.models import Post,Category,Comments

class PostCreateFroms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'categories','content', 'images', 'tags']
        

class CategoryCreateFroms(forms.ModelForm):
    class Meta:
        model =  Category
        fields = ['name']       
        
        