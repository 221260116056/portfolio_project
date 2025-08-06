from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost, Comment
from .forms import CommentForm  # ✅ Make sure you create this form in forms.py

def blog_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_home.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    comments = post.comments.all().order_by('-created_at')  # ✅ related_name='comments'

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog-detail', pk=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })

