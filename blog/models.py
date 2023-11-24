from django.db import models
from django.contrib.auth.models import User
import os

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}'

# Create your models here.
class Post(models.Model):
    # DB col을 생성하는데, model -> title
    title = models.CharField(max_length=30)

    # 필수 아님
    # hook_text = models.CharField


    # DB col을 생성하는데, model -> content
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    # DB col을 생성하는데, model -> time
    # 현재시간을 새로 작성할 때 바로 넣기
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정시간을 업데이트 했을때, 현재시각으로 교체
    update_at = models.DateTimeField(auto_now=True)
    
    # 작성자
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    
    # 카테고리
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    # 태그
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'