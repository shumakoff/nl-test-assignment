from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Page
from core.serializers import PageSerializer, PageContentSerializer


def hit(queryset):
    """
    Increases counter for objects
    in queryset
    """
    # TODO: offload this to celery
    # TODO: select_for_update
    for entry in queryset:
        entry.hit()
        entry.save()


class PageViewSet(viewsets.ModelViewSet):

    """
    Handles API queries for pages, displays content too
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer

    def retrieve(self, request, pk=None):
        page = Page.objects.get(id=pk)
        page_content = page.contentbase_set.select_subclasses()
        hit(page_content)
        serializer = PageContentSerializer(page)
        return Response(serializer.data)
