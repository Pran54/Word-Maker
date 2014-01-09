Basic Django.

Don't forget to use python3 instead of python in terminal.'

Random Stuff
=============
-Django uses sqlite3 for its database instead of full-on SQL.
-INSTALLED_APPS contains the list of all installed apps, expect it to be changed


To start a project : django-admin.py startproject mysite
======================================================

A lot of stuff is done through the manage.py file.
======================================================
python manage.py runserver (port-number)

python manage.py syncdb
-Seeds the db

python manage.py startapp (name-of-app)
-A project can have multiple apps
-Apps have models: models are classes

python manage.py sql (name-of-app)

python manage.py sqlall (name-of-app)

python manage.py shell
-Look up the API

Models
======
-A Model class is essentially a database table
-Import the model, create it, and save it (save())
  -create() both makes and saves it
-Updates are made after you say save()
-.objects is the default name for the manager. A manager is basically like an API
  -objects.all() returns everything in the data table
  -This returns a QuerySet, which is lazy. Not evaluated until actually called.
-Database table entries are python objects


class Choice(models.Model):

    def __str__(self): 
        return self.choice_text #Or anything else you want the model to be indentified by
            
SQL Stuff
=========
.filter()
-field__lookuptype=value   
    -lookuptype is something like lte (<=) or exact (=)
    -For a complete set of lookups: https://docs.djangoproject.com/en/1.6/ref/models/querysets/#field-lookups
-Spanning across relationships: two underscores with two fields
    -A SQL join or some shit like that
.get()  (pk=x)
-Returns a single value
.all()
-Returns a QuerySet with everything in the table
.exclude(condition)
-Returns a QuerySet excluding the condition
.order_by(sort-condition)
-Orders the QuerySet

A QuerySet can be sliced like a normal python iterable.
  
  
Admin Page
==========
-add /admin to the server URL
-The login is your superuser thing (david9517, tcgm)
-Have to edit the admin.py file 

from django.contrib import admin
from polls.models import Poll

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question'] #Orders the order by pubdate and question, not question and pubdate
    
    fieldsets = [
            (None,               {'fields': ['question']}),  #Creates a separate header for question and pubdate
            ('Date information', {'fields': ['pub_date']}),
        ] 

admin.site.register(Poll, PollAdmin)

-I didnt cover a lot of the other admin stuff, so if you need it it is here: https://docs.djangoproject.com/en/1.6/intro/tutorial02/


Views
=====
  
  
  
  
 