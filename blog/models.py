from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

STATUS = (
    (0, 'draft'),
    (1, 'published')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def publish(self):
        self.published_on = timezone.now()
        self.status = 1
        self.save()

    def get_approved_comments(self):
        return self.comments.filter(approved=True)

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    # def get_absolute_url(self):
    #     return reverse('post_list')

    def __str__(self):
        return self.text