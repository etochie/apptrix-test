from django.contrib import admin
from apps.core.models import TopBackgroundImage, ItemModel, Block3Image,\
    Reviews, Contacts


class ItemAdmin(admin.ModelAdmin):
    fields = ('title', 'is_main', 'image', 'image_mouseover', 'price', 'old_price')


class TopBackgroundImageAdmin(admin.ModelAdmin):
    fields = ('image',)

class Block3ImageAdmin(admin.ModelAdmin):
    fields = ('first_image', 'second_image')


admin.site.register(TopBackgroundImage, TopBackgroundImageAdmin)
admin.site.register(ItemModel, ItemAdmin)
admin.site.register(Block3Image, Block3ImageAdmin)
admin.site.register(Reviews)
admin.site.register(Contacts)
