from django.db import models
from core import constants as core_constants

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Collages(BaseModel):

    collage_name = models.CharField(max_length=50)
    code  = models.CharField(max_length=50)  
    collages_type = models.CharField(max_length=50,
                        choices = core_constants.COLLAGE_CHOICE)
    city = models.CharField(max_length=50)                        
    
    def __str__(self):
        return self.collage_name

    def collage_get_details(self):
        return{
            "id":self.id,
            "collage_name":self.collage_name,
            "code":self.code,
            "collages_type":self.collages_type,
            "city":self.city,
        }


class CrudUser(BaseModel):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)