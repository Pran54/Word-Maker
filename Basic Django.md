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
- Django uses URLConfs, which map URL patterns to views. 

- We redirected the urls.py from mysite.urls to the polls.urls. The mysite.urls also has stuff for the admin site. 

- include() is used. include() points to other URLConfs. It chops off the preceding part of the string.

- The urls.py file has all the regexes and the matching commands, in the form of url() functions. views is imported from polls.

- Meanwhile, the views.py file has the views given a request. The return statement has an HTTP response.

- Don't need the .html at the end.



-url()
------

Arguments:

-		regex
Matches regular expressions against requested URLs, looking for the first match.

A r'^ starts a regex. 

( Some complicated shit about regex notations )

A $ sign ends a regex.

-   	view	
Calls the specified view function
(Optional)

- 	kwargs

- `	name`

Views that do something: Django's template system
---------------------------------------------------------

Bottom line, all a view needs to return is either an HTTPResponse or an HTTP404. An HTTP response is a very broad category, however.

- A template should go in the app folder, not the project folder for the sake of portability.

- It is necessary to namespace (having a directory inside a template folder inside of the directory) because otherwise Django could find views from another app.

Example of loading a view:

`def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)`
	
-The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. It returns an HttpResponse object of the given template rendered with the given context.

Raising a 404 error
-------------------
`try:
	blahblahblah
except:
	raise Http404`

    poll = get_object_or_404(Poll, pk=poll_id)
     return render(request, 'polls/detail.html', {'poll': poll})

The get_object_or_404() function takes a Django model as its first argument and an arbitrary number of keyword arguments, which it passes to the get() function of the model’s manager. It raises Http404 if the object doesn’t exist.
 
Templates
---------
https://docs.djangoproject.com/en/1.6/topics/templates/

Obviously, there is a lot to read up on.
  

  
 