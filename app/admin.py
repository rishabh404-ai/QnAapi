from django.contrib import admin
from .models import Questions
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Questions)
class QuestionsAdmin(ImportExportModelAdmin):
    list_fields = ('Text','Image','Tags')