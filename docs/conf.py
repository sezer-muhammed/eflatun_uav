import os
import sys
import sphinx_rtd_theme
from pathlib import Path

docs_path = Path(__file__).parent
project_path = docs_path.parent

sys.path.insert(0, str(project_path.resolve()))

for child_path in project_path.glob('**/'):
    if child_path.is_dir() and (child_path / '__init__.py').exists():
        sys.path.insert(0, str(child_path.resolve()))

project = 'Eflatun UAV'
copyright = '2023, Muhammed Sezer, Şevval Dikkaya'
author = 'Muhammed Sezer, Şevval Dikkaya'
release = '2023'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon', 'sphinx.ext.autosummary', 'sphinx.ext.intersphinx',]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
    'special-members': '__init__',
    'imported-members': True,
    'show-inheritance': True,
}


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

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_static_path = ['_static']