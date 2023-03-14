from django.db import models
from django.contrib.auth.models import User
import uuid
from users.models import Profile
from users.models import User
# Create your models here.

class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link = models.CharField(max_length=2000,blank=True,null=True)
    source_link = models.CharField(max_length=200, blank=True,null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True,blank=True)
    vote_ratio = models.IntegerField(default=0, null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200, choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name
    




class Form(models.Model):
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title
    

class Response(models.Model):
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    created = models.DateTimeField(auto_now_add=True)
    response_text = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.id


class ProjectsForm(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'projects_form'
        
        
class Forms(models.Model):
    form_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True) 
    # user_id = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    form_json = models.TextField(db_column='form_JSON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forms'