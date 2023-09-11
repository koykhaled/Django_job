from django.db import models

# Create your models here.

JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)


class Job(models.Model):
    title = models.CharField(max_length=100)
    # location =
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    description = models.TextField(null=True, max_length=1000, blank=True)
    publish_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title