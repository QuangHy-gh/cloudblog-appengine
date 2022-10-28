from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        r_urls = reverse("post_detail", kwargs={"pk": self.pk})

        return r_urls
