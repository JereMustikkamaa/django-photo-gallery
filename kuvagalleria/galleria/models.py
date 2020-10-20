from django.db import models
from django.contrib.auth.models import User
import os.path
from PIL import Image as pillowImage
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.

def get_upload_path(instance, filename):
    return "%s/%s/%s" % (instance.user, instance.subfolder, filename)


def get_thumbnail_path(instance, filename):
    return "%s/%s/%s" % (instance.user, instance.subfolder, "thumbnail_" + filename)


class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    subfolder = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=20, null=False)
    private = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to=get_upload_path)
    full_hd = models.ImageField(upload_to=get_upload_path, null=True)
    thumbnail = models.ImageField(upload_to=get_upload_path, editable=False)
    aspect_ratio = models.FloatField()
    def save(self, *args, **kwargs):

        if not self.thumbnail:
            self.make_thumbnail()
        
        if self.check_if_full_hd() and not self.full_hd:
            self.make_full_hd()

        super(Image, self).save(*args, **kwargs)

    def check_if_full_hd(self):
        im_size = pillowImage.open(self.image)
        width, height = im_size.size
        if width <= 1080 or height <= 1080:
            return False
        else:
            return True

    def make_full_hd(self):
        file, ext = os.path.splitext(self.image.name)
        im = pillowImage.open(self.image)
        im.thumbnail((1920, 1920), pillowImage.ANTIALIAS)
        ext = ext.lower()
        
        if ext in [".jpg", ".jpeg"]:
            filetype = "JPEG"
        elif ext == ".gif":
            filetype = "GIF"
        elif ext == ".png":
            filetype = "PNG"
        else:
            return
        buf = BytesIO()
        im.save(buf, filetype)
        buf.seek(0)
        self.full_hd.save(file+"_full_hd"+ext, ContentFile(buf.read()))
        buf.close()
        return


    def make_thumbnail(self):

        file, ext = os.path.splitext(self.image.name)
        im = pillowImage.open(self.image)

        # save image aspect ratio
        width, height = im.size
        aspect_ratio = width/height
        self.aspect_ratio = aspect_ratio

        im.thumbnail((500,500), pillowImage.ANTIALIAS)
        ext = ext.lower()
        
        if ext in [".jpg", ".jpeg"]:
            filetype = "JPEG"
        elif ext == ".gif":
            filetype = "GIF"
        elif ext == ".png":
            filetype = "PNG"
        else:
            return
        buf = BytesIO()
        im.save(buf, filetype)
        buf.seek(0)
        self.thumbnail.save(file+"_thumbnail"+ext, ContentFile(buf.read()))
        buf.close()
        return

    @property
    def fullhdURL(self):
        try:
            url = self.full_hd.url
        except:
            url = ""
        return url

    @property
    def thumbnailURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ""
        return url

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
        return url

    def __str__(self):
        return self.title
