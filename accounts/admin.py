from django.contrib import admin
from .models import User, Customer, Vendor

class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'

class VendorInline(admin.StackedInline):
    model = Vendor
    can_delete = False
    verbose_name_plural = 'vendors'

class UserAdmin(admin.ModelAdmin):
    inlines = (CustomerInline, VendorInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        if obj.is_customer:
            return [inline(self.model, self.admin_site) for inline in self.inlines if isinstance(inline, CustomerInline)]
        if obj.is_vendor:
            return [inline(self.model, self.admin_site) for inline in self.inlines if isinstance(inline, VendorInline)]
        return []

admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Vendor)
