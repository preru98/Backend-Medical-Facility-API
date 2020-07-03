from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=15)

    def __str__(self):
        record='{}, {} : {}, {}'.format(str(self.username), str(self.email), str(self.password), str(self.id))
        return record



class Branch(models.Model):
    name = models.CharField(max_length=200)
    discount_rate = models.FloatField()

    def __str__(self):
        record='{} {} : {}'.format(str(self.name), str(self.id), str(self.discount_rate))
        return record



class Staff(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    password = models.CharField(max_length=15)

    def __str__(self):
        record='{}, {}, {}, {}, {} from branch {}'.format(str(self.username), str(self.email), str(self.phone_number),  str(self.password),  str(self.id), str(self.branch))
        return record
