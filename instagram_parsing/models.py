from django.db import models
from admin_app.models import School


# Create your models here.
class InstagramPost(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    post_id = models.CharField(max_length=100, unique=True)
    image_url = models.URLField()
    caption = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    post_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f'{self.school.school_kz_name}'