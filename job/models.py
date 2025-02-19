from django.db import models
from django.utils import timezone

JOB_TYPE = (
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
)


# Create your models here.
class Job(models.Model):  # table name will be job_job

    title = models.CharField(max_length=100)  # column varchar(100)

    job_type = models.CharField(max_length=15, choices=JOB_TYPE)  # column varchar(15)

    description = models.TextField()  # column text

    published_at = models.DateTimeField(auto_now=True)  # column datetime

    vacancy = models.IntegerField(default=1)  # column integer

    salary = models.IntegerField(default=0)  # column integer

    experience = models.IntegerField(default=1)  # column integer

    # The __str__() method returns a human-readable, or informal, string representation of an object
    def __str__(self):
        """this is used to show the title of the job in the admin panel instead of job object 1,2,3,4,5"""
        return self.title
