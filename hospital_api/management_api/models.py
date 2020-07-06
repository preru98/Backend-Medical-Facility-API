from django.db import models

# Create your models here.

class Admin(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)

    def __str__(self):
        record='{}, {} : {}, {}'.format(str(self.id), str(self.username), str(self.email), str(self.password))
        return record



class Branch(models.Model):
    name = models.CharField(max_length=200, unique=True)
    discount_rate = models.FloatField()

    def __str__(self):
        record='{} {} : {}'.format(str(self.id), str(self.name), str(self.discount_rate))
        return record



class Staff(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, to_field='name', on_delete=models.CASCADE)
    password = models.CharField(max_length=15)

    def __str__(self):
        record='{}, {}, {}, {}, {} from branch {}'.format(str(self.id), str(self.username), str(self.email), str(self.phone_number), str(self.password), str(self.branch))
        return record



class Patient(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    branch = models.ForeignKey(Branch, to_field='name', on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    datetime_of_admission=models.DateTimeField(auto_now=True)

    def __str__(self):
        record='{}, {}, {}, {}, {}, {} from branch {}'.format(str(self.id), str(self.username), str(self.email), str(self.phone_number),  str(self.age), str(self.datetime_of_admission),  str(self.branch))
        return record



class Doctor(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)

    def __str__(self):
        record='{}, {}, {}, {}'.format(str(self.id), str(self.username), str(self.email), str(self.password))
        return record
