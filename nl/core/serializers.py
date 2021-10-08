from rest_framework import serializers
from core.models import Page, ContentBase


class PageSerializer(serializers.HyperlinkedModelSerializer):
    """
    Represents list of pages available
    """

    class Meta:
        model = Page
        fields = '__all__'

class PageContentSerializer(serializers.ModelSerializer):
    """
    Represents page and it's content
    """
    content = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = '__all__'

    def get_content(self, obj):
        page_content = []
        for content in obj.contentbase_set.select_subclasses().order_by('pagecontent__relative_order'):
            base_serializer = content.get_serializer()
            serializer = base_serializer(content)
            page_content.append(serializer.data)
        return page_content