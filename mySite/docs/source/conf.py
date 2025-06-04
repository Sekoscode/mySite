# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django


sys.path.insert(0, os.path.abspath('../../'))  # Adjust based on your structure
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mySite.settings')
django.setup()


project = 'mySite'
copyright = '2025, fufu'
author = 'fufu'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # auto-documentation from docstrings
    'sphinx.ext.napoleon',       # supports Google & NumPy style docstrings
    'sphinx.ext.viewcode',       # add links to source code
    'sphinx_rtd_theme',          # theme for ReadTheDocs
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
