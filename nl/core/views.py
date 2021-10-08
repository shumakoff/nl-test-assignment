from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Page
from core.serializers import PageSerializer, PageContentSerializer
from core.tasks import update_hits_task


def hit(queryset):
    """
    Increases counter for objects in queryset
    """
    for entry in queryset:
        update_hits_task.delay(entry.id)


class PageViewSet(viewsets.ModelViewSet):

    """
    Handles API queries for pages, displays content too
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def retrieve(self, request, pk=None):
        page = get_object_or_404(Page.objects.all(), id=pk)
        page_content = page.contentbase_set.select_subclasses()
        hit(page_content)
        serializer = PageContentSerializer(page)
        return Response(serializer.data)
