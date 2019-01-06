from django.db import models
from django.utils import timezone

## How to store deleted things
## using username as key..changing foreign keys
## is user_metadata necessary (should it all be in one table)

class User(models.Model):
    username = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = 'user'

class User_Metadata(models.Model):
    user = models.ForeignKey(User, 
        on_delete=models.CASCADE)
    joined_on = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'user_metadata'

# necessary for more fluid upload functionality
class Slide_id(models.Model):
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'slide_id'

class Slide(models.Model):
    # only stores metadata
    class upload_path_handler():
        pass
    id = models.ForeignKey(Slide_id, primary_key=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10) #should it be int?
    description = models.CharField(default='', max_length=500)
    last_mod = models.DateTimeField(default=timezone.now)
    thumbnail = models.URLField(max_length=200, unique=True) #
    class Meta:
        db_table = 'slide'

class Institution(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'institution'
    #location = models.CharField()
    #thumbnail = models.ImageField()

class Affiliation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    class Meta:
        db_table = 'affiliation'
        unique_together = (("user", "institution"))

class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True)
    class Meta:
        db_table = 'tag'
    
class Slide_Tag(models.Model):
    slide = models.ForeignKey(Slide, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    class Meta:
        db_table = 'slide_tag'
        unique_together = (("slide", "tag"))


# Create your models here.
