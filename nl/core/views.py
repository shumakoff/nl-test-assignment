from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Page
from core.serializers import PageSerializer


def hit(queryset):
    """
    Increases counter for objects
    in queryset
    """
    for entry in queryset:
        entry.hit()
        entry.save()


class PageViewSet(viewsets.ViewSet):

    """
    Handles api queries for pages,
    displays content too
    """

    def list(self, request):
        queryset = Page.objects.all()
        serializer = PageSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        page = Page.objects.get(id=pk)
        page_content = page.contentbase_set.select_subclasses()
        hit(page_content)
        serializer = PageSerializer(page)
        return Response(serializer.data)