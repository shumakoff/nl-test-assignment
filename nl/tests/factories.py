import factory
from core.models import Page, ContentBase, ContentVideo, ContentAudio, ContentText


class ContentVideoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentVideo


class ContentAudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentAudio


class ContentTextFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ContentText


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page
