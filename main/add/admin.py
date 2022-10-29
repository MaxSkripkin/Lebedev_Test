from django.contrib import admin

from add.models import Putin_order


@admin.register(Putin_order)
class childrenAdmin(admin.ModelAdmin):

    list_display=('id', 'doc_name', 'chapter_num', 'chapter_name', 'link')