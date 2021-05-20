from django.contrib import admin
from .models import Region,Product,ProductCircuit,Opportunity,ProductDirectory


def assign_circuit(modeladmin, request, queryset):
    for qs in queryset:
        try:
            product_directory_obj = ProductDirectory.objects.get(product_code = qs.product_code)
            opportunity_obj = Opportunity.objects.filter(circuit_id__isnull = False).last()
            
            _new_circuit_id = 0
 

            if opportunity_obj:
                _circuit_id = opportunity_obj.circuit_id
                _circuit_id = _circuit_id.split('.')[-1]
                
                if _circuit_id.startswith(product_directory_obj.number_prefix):
                    _new_circuit_id  = _circuit_id[len(product_directory_obj.number_prefix):]
                
                _new_circuit_id =  int(_new_circuit_id) + 1
            else:
                _new_circuit_id = 1
                
                        
            qs.circuit_id = f'{product_directory_obj.region}.{product_directory_obj.product_name}.{product_directory_obj.number_prefix}{_new_circuit_id}'
            qs.save()
            
        except Exception as e:
            print(e)
   
    
    
    
assign_circuit.short_description = "Assign circuit ID"

class OpportunityAdmin(admin.ModelAdmin):
    list_display = [
       'customer_name','address', 'product_code', 'phone', 'email','circuit_id']
    actions = [assign_circuit]
    #exclude = ('circuit_id',)

admin.site.register(ProductCircuit)

admin.site.register(Opportunity,OpportunityAdmin)

admin.site.register(ProductDirectory)

# admin.site.register(ProductCircuit)
admin.site.register(Region)
admin.site.register(Product)

