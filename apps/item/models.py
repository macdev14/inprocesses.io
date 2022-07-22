from unicodedata import name
from django.db import models
from django.urls import reverse

from apps.authentication.models import Company
# from apps.subitem.models import SubItem

# Create your models here.

class Item(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Nome", max_length=512, blank=True)
    description = models.CharField(verbose_name="Descrição", max_length=512, blank=True)
    quantity = models.IntegerField(default=1, editable=True)
    number =  models.IntegerField(default=1)
    #subitem = models.ManyToManyField(SubItem, related_name='subitem', verbose_name='Sub Item')
    def get_absolute_url(self): # new
        return reverse('item:update', args=[int(self.id)])

    def save(self, *args, **kwargs):
        if self._state.adding:
            # company = Company.objects.get(user=self.request.user)
            # self.company = company
            # Get the maximum display_id value from the database
            last_number = Item.objects.all().aggregate(largest=models.Max('number'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_number is not None:
                self.number = last_number + 1
        super().save(*args, **kwargs)
    
 

    def __str__(self):
        return str(self.number)+' - '+self.name

