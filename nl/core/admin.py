from django.contrib import admin
from core.models import Page, ContentBase, ContentVideo, ContentAudio, ContentText

class PageContentInline(admin.TabularInline):
    model = ContentBase.page.through
    extra = 1


class PageAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        PageContentInline
    ]


class ContentBaseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    exclude = ['page']
    inlines = [
        PageContentInline
    ]


class ContentVideoAdmin(ContentBaseAdmin):
    pass


class ContentAudioAdmin(ContentBaseAdmin):
    pass


class ContentTextAdmin(ContentBaseAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(ContentVideo, ContentVideoAdmin)
admin.site.register(ContentAudio, ContentAudioAdmin)
admin.site.register(ContentText, ContentTextAdmin)
