from django.contrib import admin
# from django.forms import Field
from testApp.models import MycustomUser,SaveBookData,Bookissue

class Bookdetail(admin.ModelAdmin):
    list_display=['bookname','auther_name','total_book']

admin.site.register(SaveBookData,Bookdetail)

class StudentDetail(admin.ModelAdmin): 
    list_display=['studentname','email','classname','branch','mobile_no','date_of_birth','address','is_admin']

admin.site.register(MycustomUser,StudentDetail)
# Register your models here.

class BookissueAdmin(admin.ModelAdmin):
    list_display = ['email','bookname','auther_name','total_book','date']

admin.site.register(Bookissue,BookissueAdmin)