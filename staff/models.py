from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Staff(models.Model):
    name=models.CharField(max_length=255,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='staff', on_delete= models.CASCADE)

    class Meta:
        ordering = ['name']
    

    def __str__(self):
        return self.name

    def get_balance(self):
        items = self.items.filter(staff_paid=False, order__staffs__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)
    
    def get_paid_amount(self):
        items = self.items.filter(staff_paid=True, order__staffs__in=[self.id])
        return sum((item.product.price * item.quantity) for item in items)