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
* Startpage: Search (use Template from google search page)
* Which WYSIWYG editor (ckeditor, tinymce, quill, ...)
* Umbrella term for: People, processes, tools
* Data for demos and tests.

## Links
* https://www.wikiorgcharts.com/
* https://pingboard.com/org-charts/org-chart-resources
* https://courses.lumenlearning.com/baycollege-introbusiness/chapter/the-organization-chart-and-reporting-structure/
* https://www.orgchartpro.com/org-chart-examples/
* https://en.wikipedia.org/wiki/Quality_management_system

## Installation
* Install your favorite IDE. For example PyCharm (Community Edition is enough)
* Create new project (empty) project: [Create a Python project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html)
* [Set up a Git repository](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html) URL: https://github.com/guettli/who-or-what-is-xyz.git
* Wait some seconds. PyCharm is indexing.
* A yellow warning should be at the top of manage.py: "Package requirement is missing: Django>=....". Install it. Wait.
* Run `python manage.py migrate`
* Run `python manage.py createsuperuser`
* Configure the runserver like explained here: [runnserver in PyCharm Community Edition](https://stackoverflow.com/questions/27269574/how-to-run-debug-server-for-django-project-in-pycharm-community-edition)
* Run 'runserver'. `Starting development server at http://127.0.0.1:8000/` should be visible
* Open the URL of the development server in your browser. You should see "The install worked successfully! Congratulations!"
 
## Development Guidelines

[Thomas's Guidelines](https://github.com/guettli/programming-guidelines)

## Theory
[Theory](THEORY.md)

## Later
[Not now, later](LATER.md)
