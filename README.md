# Simple21Tree: A tree of #Hashtags to increase obviousness


Simple21Tree is a simple way to a [Single source of truth](https://en.wikipedia.org/wiki/Single_source_of_truth)
 in your project, company or startup.

Simple21Tree helps you to define:

* terminology
* roles
* processes
* tools
* resources
* ...

## State

brainstorming


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

## Similar projects
* https://www.graphitedocs.com/
* https://www.xwiki.org/ (Java, established since 2003)
* https://djangopackages.org/grids/g/wikis/ (But all use a markup language, not HTML and a WYSIWYG editor)
* https://djangopackages.org/grids/g/cms/ They support WYSIWYG, but do they feel lightweight and simple?

## Installation
```
python3 -m venv simple21env
cd simple21env
. bin/activate
pip install -e git+https://github.com/guettli/simple21tree.git#egg=simple21tree
ls src
 --> src/simple21tree contains the source code
 ```
 
* Open your favorite IDE. For example PyCharm (Community Edition is perfectly adequate)
* Open `simple21env/src` "... How would you like to open the project?" choose "This Window".
* Open "manage.py" (for example via shift-shift). A yellow warning is at the top "No Python interpreter is configured for the project". Choose "Configure Python Interpreter". Choose "add", then "Existing Environment". Choose `simple21env/bin/python`.
* Wait some seconds. PyCharm is indexing.
* In terminal: `cp simple21tree/manage.py .`

Congratulations, now you have the needed source code installed.


* Create database tables: `python manage.py migrate` (or in PyCharm "Run/migrate")
* Create superuser: `python manage.py createsuperuser`
* Run tests: `python manage.py test simple21` (if there is something wrong, please create an [issue](https://github.com/guettli/simple21tree/issues))
* Run development server: `python manage.py runserver` (or in PyCharm "Run/runserver"). *Starting development server at http://127.0.0.1:8000/* should be visible
* Open the URL of the development server in your browser. You should see the startpage of Simple21: A simple search input field (like google).
 
## Development Guidelines

* [My general Guidelines](https://github.com/guettli/programming-guidelines)
 
## Theory
[Theory](THEORY.md)

## Later
[Not now, later](LATER.md)
