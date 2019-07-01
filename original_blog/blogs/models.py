from django.db import models
from markdown import markdown
from django.utils.html import mark_safe
from django import forms
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

def get_upload_path(instance, filename):
    n = datetime.now()
    prefix = "upload/"
    ymd='/'.join([n.strftime('%Y'), n.strftime('%m'), n.strftime('%d'), ""]) + "/"
    directory=str(instance.user.id) + "/"
    name=str(uuid.uuid4()).replace("-", "")
    extension=os.path.splitext(filename)[-1]
    return ''.join([prefix, directory, ymd, name, extension])

class Blog(models.Model):
    # blankの初期値はFalse,そのままでよければ省略
    title = models.CharField(blank=False, null=False, max_length=150)
    text = models.TextField(blank=True)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    origin = models.ImageField(blank=True, null=True, upload_to="media")

    big = ImageSpecField(source="origin",
    processors=[ResizeToFill(1280, 1024)],
    format='JPEG'
    )

    thumbnail = ImageSpecField(source='origin',
    processors=[ResizeToFill(250,250)],
    format="JPEG",
    options={'quality': 60}
    )

    middle = ImageSpecField(source='origin',
    processors=[ResizeToFill(600, 400)],
    format="JPEG",
    options={'quality': 75}
    )

    small = ImageSpecField(source='origin',
    processors=[ResizeToFill(75,75)],
    format="JPEG",
    options={'quality': 50}
    )

    def get_message_as_markdown(self):
        return mark_safe(markdown(self.text, safe_mode='escape'))

    def __str__(self):
        return self.title
