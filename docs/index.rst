.. pptx-blueprint documentation master file, created by
   sphinx-quickstart on Sun Oct 13 10:54:23 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pptx-blueprint documentation
==========================================

pptx-blueprint is a PowerPoint templating engine. The tool automatically creates presentations using some data and a ``.pptx`` file as a the layout template.


First steps
===========

.. code-block:: python
   :linenos:

   import pptx_blueprint

   from pathlib import Path

   pres = pptx_blueprint.Template("template.pptx")
   pres.replace_text("head_line", "My first presentation with pptx-blueprint")
   pres.replace_image("title_img", Path("./img/title_img.png"))
   pres.save("my_presentation.pptx")


The helper class ``Template``
=============================

This is only included to demonstrate the usage of ``.. autoclass::``. By adding the argument ``:noindex:`` this occurence of ``pptx_blueprint.Template`` is not used for the index.

.. autoclass:: pptx_blueprint.Template
   :noindex:



.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
