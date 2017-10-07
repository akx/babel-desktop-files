Babel extractor for desktop files
=================================

Following up on the discussion in https://github.com/python-babel/babel/issues/536 ,
this repository implements bare-bones, proof-of-concept desktop file i18n generation.

There are coarse edges, and this needs some packaging, but hey, it's a proof of concept.

Usage
-----

* Clone including submodules (this will download the source of `polari` for an example)
* Install `babel` (in a virtualenv maybe?)
* Run `make` (see the makefile for the steps involved).

You should find a new `org.gnome.Polari.desktop` file in the checkout directory, with translations in all known languages.
