from django.db import models

class employee(models.Model):
    eid= models.CharField(max_length=25)
    ename= models.CharField(max_length=25)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=30)


class product(models.Model):
    pid= models.CharField(max_length=25)
    pname= models.CharField(max_length=25)
    pdiscription = models.CharField(max_length=30)
    ptype = models.CharField(max_length=30)
    pcurrent_b_price = models.CharField(max_length=30)
    pcurrent_s_price = models.CharField(max_length=30)
    pcurrent_qty = models.CharField(max_length=30)
    pdate = models.CharField(max_length=30)
    psup = models.CharField(max_length=30)



class Image(models.Model):
    #title = models.CharField(max_length=200)
    real_image = models.ImageField(upload_to='images')
    mask_image = models.ImageField(upload_to='images')
    def __str__(self):
        return " "
