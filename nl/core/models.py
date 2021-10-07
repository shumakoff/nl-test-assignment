from rest_framework import serializers
from django.db import models
from model_utils.managers import InheritanceManager


class Page(models.Model):
    """
    Holds page data
    """
    title = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.title}'


class ContentBase(models.Model):
    title = models.CharField(max_length=250)
    counter = models.PositiveIntegerField(default=0)
    page = models.ManyToManyField(Page, blank=True)
    objects = InheritanceManager()

    def __str__(self):
        return f'{self.title}'

    def hit(self):
        """ Increases the counter """
        self.counter += 1

    @classmethod
    def get_serializer(cls):
        class BaseSerializer(serializers.ModelSerializer):
            class Meta:
                model = cls  # this is the main trick here, this is how I tell the serializer about the model class
                fields = '__all__'

        return BaseSerializer  # return the class object so we can use this serializer


class ContentVideo(ContentBase):
    url_video = models.CharField(max_length=250)
    url_subtitles = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.title} - {self.url_video} at {self.page} with {self.counter}'


class ContentAudio(ContentBase):
    bitrate = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.bitrate} at {self.page} with {self.counter}'


class ContentText(ContentBase):
    text = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.text} at {self.page} with {self.counter}'
