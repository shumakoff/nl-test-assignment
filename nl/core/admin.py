from django.contrib import admin
from core.models import Page, ContentVideo, ContentAudio, ContentText


class PageAdmin(admin.ModelAdmin):
    pass


class ContentVideoAdmin(admin.ModelAdmin):
    pass


class ContentAudioAdmin(admin.ModelAdmin):
    pass


class ContentTextAdmin(admin.ModelAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(ContentVideo, ContentVideoAdmin)
admin.site.register(ContentAudio, ContentAudioAdmin)
admin.site.register(ContentText, ContentTextAdmin)
