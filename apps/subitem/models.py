from django.db import models

from apps.authentication.models import Company
from apps.item.models import Item

# Create your models here.
class SubItem(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    main_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, editable=True)
    number = models.IntegerField(default=1, editable=False)
    name = models.CharField(verbose_name="Nome", max_length=512, blank=False)
    description = models.CharField(verbose_name="Descrição", max_length=512, blank=False)

    def save(self, *args, **kwargs):
        if self._state.adding:
            # company = Company.objects.get(user=self.request.user)
            # self.company = company
            # Get the maximum display_id value from the database
            last_number = SubItem.objects.all().aggregate(largest=models.Max('number'))['largest']

            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_number is not None:
                self.number = last_number + 1
        super().save(*args, **kwargs)