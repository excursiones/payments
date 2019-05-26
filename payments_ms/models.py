from djongo import models
from django.core.validators import MinValueValidator
# Create your models here.
    
class UserPayment(models.Model):
    id = models.AutoField(primary_key = True)
    user_id = models.IntegerField()
    price = models.FloatField(validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now_add=True)
    origin_account = models.CharField(max_length = 30)
    destination_account = models.CharField(max_length = 30)

    def __str__(self):
        return '{} - ${}'.format(self.user_id, self.price)

class PaymentRefund(models.Model):
    id = models.AutoField(primary_key = True)
    user_payment = models.ForeignKey(UserPayment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.user_payment)

class CompanyPayment(models.Model):
    id = models.AutoField(primary_key = True)
    company_id = models.IntegerField()
    price = models.FloatField(validators=[MinValueValidator(1)])
    date = models.DateTimeField(auto_now_add=True)
    origin_account = models.CharField(max_length = 30)
    destination_account = models.CharField(max_length = 30)

    def __str__(self):
        return '{} - ${}'.format(self.company_id, self.price)