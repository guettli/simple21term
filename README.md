# Who or what is xyz?

A Who-or-what-is-xyz is a simple way to a [Single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth)
 in your project, company or startup. Even, if information is scattered
 in several insular [Information silos](https://en.wikipedia.org/wiki/Information_silo).

Who-or-what-is-xyz helps you to define:

* terminology
* roles
* processes
* tools
* resources
* ...

Open Source since 2020.

## State
pre-alpha (unusable)

## Next
* Log every search, incl datetime, user, number of results.
* Feedback-Button
* Which WYSIWYG editor (ckeditor, tinymce, quill, ...)
* Umbrella term for: People, processes, tools
* Data for demos and tests.

## Links
* https://www.wikiorgcharts.com/
* https://pingboard.com/org-charts/org-chart-resources
* https://courses.lumenlearning.com/baycollege-introbusiness/chapter/the-organization-chart-and-reporting-structure/
* https://www.orgchartpro.com/org-chart-examples/
* https://en.wikipedia.org/wiki/Quality_management_system
* https://developers.google.com/tech-writing/overview
* https://google.github.io/styleguide/

## Installation
* Install your favorite IDE. For example PyCharm (Community Edition is enough)
* Create new (empty) project: [Create a Python project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html). Name it "who-or-what". Leave the other values unchanged.
* VCS / Get from Version Control. URL: https://github.com/guettli/who-or-what-is-xyz.git then "clone", then "Open in this window".
* Open "manage.py". A yellow warning is at the top "No Python interpreter is configured for the project". Choose "Configure Python Interpreter". Choose "add", then "New Environment".
* Wait some seconds. PyCharm is indexing.
* A yellow warning should be at the top of manage.py: "Package requirement is missing: Django>=....". Install it. Wait.

Congratulations, now you have the needed source code installed.

Now create the database tables, a superuser and start the server:

* In terminal `python manage.py migrate` (or in PyCharm "Run/migrate")
* In terminal `python manage.py createsuperuser`
* In terminal `python manage.py runserver` (or in PyCharm "Run/runserver"). *Starting development server at http://127.0.0.1:8000/* should be visible
* Open the URL of the development server in your browser. You should see "TODO"
 
## Development Guidelines

[Thomas's Guidelines](https://github.com/guettli/programming-guidelines)

## Theory
[Theory](THEORY.md)

## Later
[Not now, later](LATER.md)
