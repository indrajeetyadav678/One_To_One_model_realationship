from django.contrib import admin
from .models import AadharModel,StudentModel
# Register your models here.

# admin.site.register(AadharModel)
# admin.site.register(StudentModel)


@admin.register(AadharModel)
class AadharAdmin(admin.ModelAdmin):
    list_display=['id','AadharNo']

@admin.register(StudentModel)
class StudentAdmin(admin.ModelAdmin):
    list_display=['stu_name','stu_aadhar']

#class StudentAdmin(admin.ModelAdmin):
    #list_display=['stu_name','aadhar_no',is_staff']

# admin.site.register(StudentModel.StudentAdmin)