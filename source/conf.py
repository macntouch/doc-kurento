# -*- coding: utf-8 -*-
#
# PyLint: Disable false positives (IDs from `pylint --list-msgs`)
# pylint: disable=invalid-name

"""
Kurento documentation build configuration file, created by
sphinx-quickstart on Tue Jan 14 01:23:07 2014.

This file is execfile()d with the current directory set to its
containing dir.

Note that not all possible configuration values are present in this
autogenerated file.

All configuration values have a default; values that are commented out
serve to show the default.

If extensions (or modules to document with autodoc) are in another directory,
add these directories to sys.path here. If the directory is relative to the
documentation root, use os.path.abspath to make it absolute, like shown here.
"""

import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.append(os.path.abspath('extensions'))
extensions = [
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
    'wikipedia',
    'examplecode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Kurento'
copyright = u'2018, Kurento'  # pylint: disable=redefined-builtin
author = u'Kurento'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = None
version_files = ['./VERSION', '../VERSION']
version_paths = [os.path.abspath(f) for f in version_files]  # Make absolute
for version_path in version_paths:
    try:
        with open(version_path, 'r') as f:
            print "Found VERSION file: '{}'".format(version_path)
            version = f.read().strip()
            break
    except IOError as err:
        print "Failed reading '{}': {}".format(version_path, err.strerror)

if version is None:
    print "ERROR reading VERSION: File not found"
    exit(1)

# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Extensions configuration ---------------------------------------------

# 'svg' would be preferred, but then graphs appear too big and don't adjust
# their width to the available space (overflows the paragraph size).
graphviz_output_format = 'png'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Default language for Wikipedia articles. Default: 'en'.
wikipedia_lang = 'en'  # English


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'logo_only': False,
    'display_version': True
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'images/kurento-white.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'images/favicon.ico'

# A list of paths that contain custom static files (such as style sheets or
# script files). Relative paths are taken as relative to the configuration
# directory. They are copied to the output's _static directory after the theme's
# static files, so a file named default.css will overwrite the theme's default.css.
html_static_path = ['_static', 'langdoc']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Kurentodoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '\\usepackage{enumitem}\n\\setlistdepth{99}',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Kurento.tex', u'Kurento Documentation', author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'kurento', u'Kurento Documentation', [author], 1),
    ('components/servers/kmf-media-connector', u'kmf-media-connector',
     u'Kurento Media Proxy', [author], 1),
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Kurento', u'Kurento Documentation',
     author, 'Kurento', 'Kurento is a WebRTC media server',
     'Miscellaneous'),
]


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Additional options for Kurento ---------------------------------------

# linkcheck, jboss forbids us
linkcheck_ignore = [r'https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm']
