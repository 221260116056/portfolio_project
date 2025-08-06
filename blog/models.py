from django.db import models
from django.utils import timezone  # ✅ Add this import

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)  # ✅ Correct usage

    def __str__(self):
        return f'Comment by {self.name}'
