import uuid
from django.db import models
from account.models import User
# Create your models here.

_types = [
    ('debit',"Debit"),
    ('credit',"Credit"),
]

class RazorpayPayments(models.Model):
    def __str__(self):
        return str(self.userid)
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    order_id=models.CharField(max_length=200)
    transaction_id=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True,editable=False)
    amount=models.IntegerField(null=True)
    type=models.CharField(max_length=6,choices=_types,blank=False)
    is_paid = models.BooleanField(default=False)