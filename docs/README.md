# Creating the documentation using Sphinx

The documentation of [pptx-blueprint](https://github.com/timhoffm/pptx-blueprint) is created using [Sphinx](https://www.sphinx-doc.org/en/master/index.html#). This file describes how to update the documentation and explains the basic configuration.


## Updating the documentation

On Linux make sure to have `make` installed. Go to the `docs/` directory of pptx-blueprint and run

```bash
make html
```

This will create a HTML version of the documentation at `docs/_build/`. Open `docs/_build/index.html` to read the documentation.

The directory `doces/source/` contains the automatically generated API documentation for pptx-blueprint. This one needs to be updated manually after making changes to the API. The update can be performed by running

```bash
sphinx-apidoc -f -o source/ ../pptx_blueprint
```

The argument `-f` forces `sphinx-apidoc` to overwrite existing files. `-o` is used to define the output directory.


## Setting up Sphinx to create the documentation

We decided to place the documentation into the sub-directory `docs/`. Inside of this directory `sphinx-quickstart` will create the basic configuration. At the wizard we decided to split up `source/` and `_build/` into separate directories.
The next step is to update `conf.py`. For `sphinx-apidoc` to work some changes are necessary:

```python
# Extending sys.path to find the module pptx-blueprint:
import os
import sys
sys.path.insert(0, os.path.abspath('../'))

# Activating autodoc and napoleon:
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

# Setting the theme to 'classic':
html_theme = 'classic'
```

[Autodoc](https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html) is needed to use different directives that include the documentation created with `sphinx-apidoc` into our documentation. For example `.. autoclass:: pptx_blueprint.Template` will load the automatically created documentation for the class `Template`.
[Napoleon](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html) is necessary to parse docstrings that follow the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html).
The default theme of Sphinx is [Alabaster](https://alabaster.readthedocs.io/en/latest/) is the default theme. From [the list of buildin themes](https://www.sphinx-doc.org/en/master/usage/theming.html#builtin-themes) we have selected *classic* to be theme we use.

## Sources

- [An idiot’s guide to Python documentation with Sphinx and ReadTheDocs](https://samnicholls.net/2016/06/15/how-to-sphinx-readthedocs/) by [Sam Nicholls](https://samnicholls.net/about/)
- [Sphinx for Python documentation](https://gisellezeno.com/tutorials/sphinx-for-python-documentation.html) by [Giselle Zeno](https://gisellezeno.com/pages/about-me.html)