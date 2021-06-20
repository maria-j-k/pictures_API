from django.contrib import admin

from api.models import Picture, Thumbnail


class ThumbnailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Thumbnail, ThumbnailAdmin)


class ThumbnailInline(admin.TabularInline):
    model = Thumbnail


class PictureAdmin(admin.ModelAdmin):
    inlines = [
            ThumbnailInline,
            ]

admin.site.register(Picture, PictureAdmin)
