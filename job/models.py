from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)


class Cetegory(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


def imageUpload(instance, file_name):
    fileName, extension = file_name.split(".")
    return "jobs/{:s}.{:s}".format(instance.title, extension)


class Job(models.Model):
    owner = models.ForeignKey(
        User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    description = models.TextField(null=True, max_length=1000, blank=True)
    publish_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    cetegory = models.ForeignKey(
        Cetegory, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to=imageUpload, null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title + str(self.id))
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Apply(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='cv/')
    cover_letter = models.TextField(null=True, blank=True)
    job = models.ForeignKey(
        Job, related_name='apply_job', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
