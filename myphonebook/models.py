from django.db import models

class Person(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self):
        return self.name
    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])
class PhoneNumber(models.Model):
    phone = models.CharField('Phone', max_length=55)
    contact = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return self.phone
