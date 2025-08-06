from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment_text']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'comment_text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment'}),
        }
