from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class UserInfo(AbstractUser):
    gender = (('male', '男'), ('female', '女'))
    nickname = models.CharField(max_length=15, blank=True)
    sex = models.CharField(max_length=10, choices=gender, default='female')

    class Meta(AbstractUser.Meta):
        pass

    def __str__(self):
        return self.nickname


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category')
    tags = models.ManyToManyField(Tag, blank=True, related_name='post_tags')

    objects = models.Manager()  # 默认的管理器
    published = PublishedManager()  # 自定义管理器

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
