from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', '草稿'), # 草稿
        ('published', '发布'), # 已发布
    )
    title = models.CharField('标题',max_length=250)
    slug = models.SlugField('固有链接',max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts',
                               verbose_name='作者')
    body = models.TextField('正文')
    publish = models.DateTimeField('发表时间',default=timezone.now)
    created = models.DateTimeField('创建时间',auto_now_add=True)
    updated = models.DateTimeField('更新时间',auto_now=True)
    status = models.CharField('状态',max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
        ordering = ('-publish',) # 按发布时间倒序排列

    def __str__(self):
        return self.title
