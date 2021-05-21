from django.contrib import admin
from .models import Region,Product,ProductCircuit,Opportunity,ProductDirectory




def assign_circuit(modeladmin, request, queryset):
    for qs in queryset:
        try:
            product_directory_obj,_ = ProductDirectory.objects.get_or_created(product_code = qs.product_code)
            opportunity_obj = Opportunity.objects.filter(circuit_id__icontains = product_directory_obj.product_code)
            _new_circuit_id = 0
            num = 1
            if opportunity_obj.exists():
                _circuit_id = opportunity_obj.latest()('circuit_id').split('.')[-1][len(product_directory_obj.number_prefix):]
            _new_circuit_id = f"00{int(_circuit_id) +num}"
            qs.circuit_id = f'{product_directory_obj.region}.{product_directory_obj.product_name}.{product_directory_obj.number_prefix}{_new_circuit_id}'
            qs.save()
        except Exception as e:
            print(e)
   
    
    
    
assign_circuit.short_description = "Assign circuit ID"

class OpportunityAdmin(admin.ModelAdmin):
    list_display = [
       'customer_name','address', 'product_code', 'phone', 'email','circuit_id']
    actions = [assign_circuit]
    exclude = ('circuit_id',)

admin.site.register(ProductCircuit)

admin.site.register(Opportunity,OpportunityAdmin)

admin.site.register(ProductDirectory)


admin.site.register(Region)
admin.site.register(Product)

