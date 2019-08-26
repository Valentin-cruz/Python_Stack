from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)

# ClassName.objects.all() - gets all the records in the table

# ClassName.objects.last() - gets the last record in the table

# ClassName.objects.first() - gets the first record in the table

# c = ClassName.objects.get(id=1)
# c.field_name = "some new value for field_name"
# c.save()

# c = ClassName.objects.get(id=1)
# c.delete()

# ClassName.objects.all().order_by("field_name") - orders by field provided, ascending