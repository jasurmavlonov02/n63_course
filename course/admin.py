from django.contrib import admin
from .models import Subject,Course,Module,Text,Video,Image,File,Topic
# Register your models here.



admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Text)
admin.site.register(Video)
admin.site.register(File)
admin.site.register(Image)
admin.site.register(Topic)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    prepopulated_fields = {'slug':('title',)}
