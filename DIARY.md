# Diary

# 2020

## 2020-12-06

Refactored central model to name "Page".

I have now a picture how I want the menu to look like.

Like the amazon menu. It easy to use and deep nesting works fine. It slides in from the left
side and items are below each other. It is like a table with one column. If you go down one
level, then the current table gets replaced by the new level. 

Related: https://softwarerecs.stackexchange.com/questions/76930/menu-like-amazon

I think I will implement this with bootstrap5 (which is still alpha).

I looked at React and Vue, but I think htmx is easier.

Did some research during the last weeks:

* https://github.com/guettli/static-site-generators
* https://github.com/guettli/gui4db
* https://github.com/guettli/front-end-frameworks
* https://github.com/guettli/html-over-the-wire
* ... see https://github.com/guettli/wol




## 2020-05-30

How to render the menu?

Looks simple and nice:
https://jqueryui.com/menu/
... but jquery is dead. Last update is four years old!

## 2020-05-28

Use React? It looks very wide spread.
http://sotagtrends.com/?tags=antd+material-ui+material-design+twitter-bootstrap+bootstrap-4+jquery-ui+reactjs

... But no, it does not make sense for my project.
See: https://www.reddit.com/r/webdev/comments/atgke2/react_vs_vanilla_js_when_to_use_each_of_them/



## 2020-04-12

Next: 

- Same UX for Admin and normal GUI. 
  - https://getbootstrap.com/docs/4.0/components/navbar/
  - Same tree as for content :-)
  - https://getbootstrap.com/docs/4.0/components/breadcrumb/
  - whole tree in one http request (MVP)
- Datamigration: Create root and Django-Admin and Django-Admin of Terms.
- Import data of iso9001 cert of Michael.

## 2020-04-02

Header should contain a search for the tree. With nice autocomplete. How to get the Django
Admin into this tree?

Should there be an tree entry for every group and for every user?

Do I want sqlite support? It might be easier to support postgres only.

Do I need django-mptt? Or ForeignKey to self enough?

Removed sitetree again. One tree is enough (Model Term).

Next: term.url (Admin of Term) should redirect to this URL

## 2020-03-29

Renamed it to Simple21Tree. Updated "Installation" part in README.

Use a package to improve the GUI? I had a look at: https://djangopackages.org/grids/g/admin-styling/
and https://djangopackages.org/grids/g/admin-interface/.
Way too many options. Most of them are outdated.

Had a look at [Saleor](https://github.com/mirumee/saleor) but this is way too
big for my small project.

Next: pip install mammoth; then import the office docs for the iso9001
certification of a friend.

If everything is in one tree ... is the django admin a part of this tree?
This would make sense. Then some initial data is needed, so that
the tree contains a root node and the django-admin node.


## 2020-03-21

PyCharm is driving me crazy. I try to find a very very simple and newbee friendly
way to set up a new system. I can set up a new system (from the command line, from
PyCharm, forward or backward, day or night), but all ways I see are not really newbee
friendly.

I have a simple goal: I want a virtualenv which contains my simple21tree. But by default
PyCharm does it the other way round: It creates a virtualenv inside simple21tree. Grrr.

Today there is only one git repo, but in the future there could be several. 

I would like to have this directory layout: simple21env/src/simple21tree.

Goal2: If I search with ctrl-shift-f I just want to search in my code, not in the
code of the libraries (like django). If I search for "index.html" I just want
to find my lines containing this.


