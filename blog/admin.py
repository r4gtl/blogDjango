from django.contrib import admin
from .models import Post, Comment, PostCategory
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self,request, queryset):
        queryset.update(active=True)
        

class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)



class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on', 'logo_post')
    list_filter= ("status",)
    search_fields = ['title', 'content']        
    prepopulated_fields = {'slug': ('title', )}
    summernote_fields = ('content',)




admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)

