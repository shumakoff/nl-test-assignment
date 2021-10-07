from rest_framework import serializers
from core.models import Page


class PageSerializer(serializers.ModelSerializer):
    """
    Represents page and it's content
    """
    content = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = ['id', 'title', 'content']

    def get_content(self, obj):
        page_content = []
        for content in obj.contentbase_set.select_subclasses():
            base_serializer = content.get_serializer()
            serializer = base_serializer(content)
            page_content.append(serializer.data)
        return page_content