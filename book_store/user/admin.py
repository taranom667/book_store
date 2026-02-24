from django.contrib import admin
from .models import *

admin.site.register(User)
''' 
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return self.model.all_objects.get_queryset()

    # search_fields = ['username']
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    def get_queryset(self,request):
       qs = self.model.all_objects.get_queryset()
       ordering=self.ordering or ()
       if ordering:
           qs = qs.order_by(*ordering)
       return qs'''
