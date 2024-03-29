# Creating a new record
ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
# Reading existing records
# Methods that return a single instance of a class
ClassName.objects.first() - gets the first record in the table
ClassName.objects.last() - gets the last record in the table
ClassName.objects.get(id=1) - gets the record in the table with the specified id
this method will throw an error unless only and exactly one record matches the query
# Methods that return a list of instances of a class
ClassName.objects.all() - gets all the records in the table

ClassName.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided

ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided
# Updating an existing record
c = ClassName.objects.get(id=1)
c.field_name = "some new value for field_name"
c.save()
# Deleting an existing record
c = ClassName.objects.get(id=1)
c.delete()
# Other helpful methods
# Displaying records
ClassName.objects.get(id=1).__dict__ - shows all the values of a single record as a dictionary
ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)
# Ordering records
ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
ClassName.objects.all().order_by("-field_name") - orders by field provided, descending