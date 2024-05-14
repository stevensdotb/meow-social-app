from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("get_owner", "text", "created_at", )

    def get_owner(self, obj):
        return obj.user.username
    
    get_owner.short_description = "Owner"
