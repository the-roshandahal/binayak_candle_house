from django.contrib import admin
from .models import *
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Attachment)
admin.site.unregister(Group)
admin.site.unregister(User)

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('product_title', 'created')
    summernote_fields = ('product_description',)



admin.site.register(Product,ProductAdmin)
admin.site.register(Gallery)
admin.site.register(Contact)


# class BlogAdmin(SummernoteModelAdmin):
#     list_display = ('title', 'created')
#     summernote_fields = ('blog',) 
# admin.site.register(Blog,BlogAdmin)

class ReadOnlyModelAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return True
    
    def has_delete_permission(self, request, obj=None):
        return False

class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('our_story',) 

@admin.register(AboutPageContent)
class AboutPageContentAdmin(AboutAdmin, ReadOnlyModelAdmin):
    pass

@admin.register(CompanySetup)
class CompanySetupAdmin(ReadOnlyModelAdmin):
    pass


@admin.register(HomeContent)
class HomeContentAdmin(ReadOnlyModelAdmin):
    pass

@admin.register(WeBelieveIn)
class WeBelieveInAdmin(ReadOnlyModelAdmin):
    pass

