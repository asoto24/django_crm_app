from django.db import models

#django pluralizes the name of the class for us, so always use single
class Record(models.Model):
    #this will be all the fields in our database for this record
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    address =models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode =models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    phone =models.CharField(max_length=50)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
