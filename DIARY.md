# Diary

# 2020

## 2020-04-12

Next: 

- Same UX for Admin and normal GUI. 
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


