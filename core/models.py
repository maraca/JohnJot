import datetime

from django.db import models
from django.contrib.auth.models import User


class ModelOrigin(models.Model):
    """
    This is the common part for each models
    Used to track the origin of the data
    """
    date_created = models.DateTimeField(default=datetime.datetime.now)
    last_edit = models.DateTimeField(default=datetime.datetime.now)
    agent = models.CharField(max_length=50)
    
    class Meta:
        abstract = True


class Group(ModelOrigin):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    
    class Meta:
        unique_together = ("owner", "name")
        
    def __unicode__(self):
        return self.name


class Contact(ModelOrigin):
    owner = models.ForeignKey(User)
    tag_name = models.CharField(max_length=40)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    
    def __unicode__(self):
        return self.tag_name


class Jot(ModelOrigin):
    """
    Every Jot types herits from this class
    """
    content = models.CharField(max_length=250)
    
    class Meta:
        abstract = True
    
    def __unicode__(self):
        return self.content


class JotDaily(Jot):
    """
    Used to take simple notes
    """
    owner = models.ForeignKey(User)


class JotContact(Jot):
    contact = models.ForeignKey(Contact)


class JotGroup(Jot):
    group = models.ForeignKey(Group)
