from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _
# from account.models import CustomUser
from django.contrib.auth.models import User
from account import models as mod


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')



class Blog(models.Model):
    STATUS_CHOICES = {
        ('draft', 'Draft'),
        ('published', 'Published')
    }
    author = models.ForeignKey(
        mod.Profile, null=True, blank=True ,on_delete=models.CASCADE, related_name='blog_author')
    slug = models.SlugField(max_length=255, unique_for_date='publish')
    caption = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    tags = models.ManyToManyField(
        "Tag", verbose_name=_('تگ ها'), related_name="blogs")
    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.caption[:20]


class ImageBlog(models.Model):
    post = models.ForeignKey(
        Blog, null=False, on_delete=models.CASCADE, related_name='blog_image')
    name = models.CharField(max_length=255, default='image')
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    def __str__(self):
        return self.name[:20]


class Tag (models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(_("عنوان لاتین"), max_length=255)
    publish = models.DateTimeField(
        _('تاریخ انتشار'), auto_now_add=True, auto_now=False)
    update = models.DateTimeField(
        _('تاریخ بروزرسانی'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
