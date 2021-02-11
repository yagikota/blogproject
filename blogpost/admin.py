from django.contrib import admin
from .models import BlogModel, SampleModele
# Register your models here.
#モデルの追加、管理画面がモデルを認識
admin.site.register(SampleModele)
admin.site.register(BlogModel)