from django.contrib import admin
from core.models import Page, ContentBase, ContentVideo, ContentAudio, ContentText

class PageContentInline(admin.TabularInline):
    model = ContentBase.page.through
    extra = 1

    # disable green "+" buttons to add new objects in foreign table
    # we don't want user to add to ContentBase directly
    def get_formset(self, request, obj=None, **kwargs):
        formset = super(PageContentInline, self).get_formset(request, obj, **kwargs)
        formset.form.base_fields['content'].widget.can_add_related = False
        return formset


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

class HiddenAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False


class ContentVideoAdmin(ContentBaseAdmin):
    pass


class ContentAudioAdmin(ContentBaseAdmin):
    pass


class ContentTextAdmin(ContentBaseAdmin):
    pass


admin.site.register(Page, PageAdmin)
admin.site.register(ContentBase, HiddenAdmin)
admin.site.register(ContentVideo, ContentVideoAdmin)
admin.site.register(ContentAudio, ContentAudioAdmin)
admin.site.register(ContentText, ContentTextAdmin)
