# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import sphinx_rtd_theme
from pathlib import Path

docs_path = Path(__file__).parent
project_path = docs_path.parent

sys.path.insert(0, str(project_path.resolve()))

for child_path in project_path.glob("**/"):
    if child_path.is_dir() and (child_path / "__init__.py").exists():
        sys.path.insert(0, str(child_path.resolve()))

project = "eflatun_uav"
copyright = "2023, Muhammed Sezer, Şevval Belkıs Dikkaya"
author = "Muhammed Sezer, Şevval Belkıs Dikkaya"
release = "04.05.2023"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",  # Core Sphinx library for auto html doc generation from docstrings
    "sphinx.ext.autosummary",  # Create neat summary tables for modules/classes/methods etc
    "sphinx.ext.intersphinx",  # Link to other project's documentation (see mapping below)
    "sphinx.ext.viewcode",  # Add a link to the Python source code for classes, functions etc.
    "sphinx_autodoc_typehints",  # Automatically document param types (less noise in class signature)
]
autosummary_generate = True
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
autodoc_inherit_docstrings = True
autodoc_docstring_signature = True
set_type_checking_flag = True  # Enable 'expensive' imports for sphinx_autodoc_typehints

add_module_names = False  # Remove namespaces from class/method signatures

napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ["_static"]
