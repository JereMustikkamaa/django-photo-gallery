from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_upload_path(instance, filename):
    return "%s/%s" % (instance.user, filename)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=20, null=False)
    image = models.ImageField(upload_to=get_upload_path)
    private = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=100, blank=True)
    # size
    # resolution
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.title
