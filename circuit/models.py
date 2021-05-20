from django.db import models
from base_rest.models import BaseModel
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe


class Opportunity(BaseModel):
    customer_name = models.CharField(max_length=255)
    address = models.TextField()
    product_code = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    altitude = models.CharField(max_length=50)
    status = models.CharField(max_length=255)
    site_survey_status = models.CharField(max_length=100,
                                          choices=[('Not Initiated',
                                                    'Not Initiated'),
                                                   ('Initiated', 'Initiated'),
                                                   ('Completed', 'Completed')],
                                          default="Not Initiated")
    project_status = models.CharField(max_length=100,
                                      choices=[('Not Initiated',
                                                'Not Initiated'),
                                               ('Initiated', 'Initiated'),
                                               ('Completed', 'Completed'),
                                               ('Rejected', 'Rejected')],
                                      default="Not Initiated")
    circuit_id = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.customer_name + "/" + self.product_code


    # def save(self, *args, **kwargs):
        
    #     if self.circuit_id is None:
    #         opportunity_obj_count = Opportunity.objects.count()
    #         opportunity_obj_count += 1
    #         try:
    #             product_directory_obj = ProductDirectory.objects.get(product_code = self.product_code)
    #             self.circuit_id = f'{product_directory_obj.region}.{product_directory_obj.product_name}.{product_directory_obj.number_prefix}{opportunity_obj_count}'  
    #         except Exception as e:
    #             return
    #     super(Opportunity, self).save(*args, **kwargs)
    
    class Meta:
        db_table = "opportunities"
        verbose_name_plural = "Opportunities"
        ordering = ["-created_at"]
        
        
class ProductDirectory(BaseModel):
    """oduct code and product directory
    """
    product_name = models.CharField(max_length=500)
    region = models.CharField(max_length=20, default="NG")
    product_code = models.CharField(max_length=10)
    number_prefix = models.CharField(max_length=3, default='0')
    
    def __str__(self) -> str:
        return self.product_name
    class Meta:
        db_table = "product_directory"
        verbose_name = "Product Directory"


class Region(BaseModel):
    region_name = models.CharField(max_length=100)
    def __str__(self):
        return self.region_name

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.product_name


class ProductCircuit(BaseModel):
    id = models.IntegerField(default=1 )
    region = models.ForeignKey(Region , related_name="region" , on_delete=models.SET_NULL , null=True , blank=True)
    product = models.ForeignKey(Product, related_name="product" , on_delete=models.SET_NULL , null=True , blank=True)
    number_prefix = models.IntegerField(default=0)
    next_circuit_id = models.CharField(max_length=100 , null=True , blank=True)
   
    def __str__(self):
        return self.next_circuit_id
    

    def save(self, *args, **kwargs):
        
        if self.next_circuit_id is None:
            # Getting the last Product Circuit ID 
            last_product_circuit = ProductCircuit.objects.last()
            
            # if circuit id not present
            last_product_circuit_id = 1
            
            # if circuit id present getting the last index
            if last_product_circuit:
                last_product_circuit_id = last_product_circuit.id + 1
                self.id = last_product_circuit.id + 1
              
            # Creating a new Circuit ID    
            self.next_circuit_id = f'{self.region.region_name}.{self.product.product_name}.{self.number_prefix}{last_product_circuit_id}'
            
        super(ProductCircuit, self).save(*args, **kwargs)
    