# Zero21Tree: A tree of #Hashtags to increase obviousness


A Zero21Tree is a simple way to a [Single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth)
 in your project, company or startup. Even, if information is scattered
 in several insular [Information silos](https://en.wikipedia.org/wiki/Information_silo).

Zero21Tree helps you to define:

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
* Same header (Django Admin and Search/Result)
* Feedback-Button
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
* https://en.wikipedia.org/wiki/Advanced_product_quality_planning

# Feedback Loops

Different kind of feedback loops, or "same content, differnt names"?

* https://en.wikipedia.org/wiki/Lean_startup#Build-Measure-Learn
* https://en.wikipedia.org/wiki/DMAIC
* https://en.wikipedia.org/wiki/Six_Sigma#DMADV_or_DFSS
* https://en.wikipedia.org/wiki/Program_lifecycle_phase
* https://en.wikipedia.org/wiki/PDCA
* https://en.wikipedia.org/wiki/Feedback

## Installation
* Install your favorite IDE. For example PyCharm (Community Edition is enough)
* Create new (empty) project: [Create a Python project](https://www.jetbrains.com/help/pycharm/creating-empty-project.html). Name it "zero21project". Leave the other values unchanged.
* VCS / Get from Version Control. URL: https://github.com/guettli/zero21tree.git then "clone", then "Open in this window".
* Open "manage.py". A yellow warning is at the top "No Python interpreter is configured for the project". Choose "Configure Python Interpreter". Choose "add", then "New Environment".
* Wait some seconds. PyCharm is indexing.
* A yellow warning should be at the top of manage.py: "Package requirement is missing: Django>=....". Install it. Wait.

Congratulations, now you have the needed source code installed.


* Create database tables: In terminal `python manage.py migrate` (or in PyCharm "Run/migrate")
* Create superuser: In terminal `python manage.py createsuperuser`
* Run tests: In terminal `python manage.py test zero21` (if there is something wrong, please create an [issue](https://github.com/guettli/zero21tree/issues))
* Run development server: In terminal `python manage.py runserver` (or in PyCharm "Run/runserver"). *Starting development server at http://127.0.0.1:8000/* should be visible
* Open the URL of the development server in your browser. You should see "TODO"
 
## Development Guidelines

[Thomas's Guidelines](https://github.com/guettli/programming-guidelines)

## Theory
[Theory](THEORY.md)

## Later
[Not now, later](LATER.md)
