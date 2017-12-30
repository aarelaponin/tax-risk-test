from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class BzEntity(models.Model):
    author = models.ForeignKey('auth.User', related_name='%(class)s_created', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now())
    deleted_by = models.ForeignKey('auth.User',blank=True, null=True, related_name='%(class)s_deleted', on_delete=models.CASCADE)
    deleted_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)


class Registry (BzEntity, models.Model):
    name = models.CharField(max_length=255)


class IDEntity (BzEntity, models.Model):
    registry_id = models.CharField(max_length=255)
    registered_in = models.ForeignKey('Registry', on_delete=models.CASCADE)
    registration_date = models.DateTimeField(default=timezone.now(),blank=True, null=True)


class Person (IDEntity, models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    dob = models.DateTimeField(default=timezone.now())

