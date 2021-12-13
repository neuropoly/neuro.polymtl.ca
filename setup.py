"""
To build the docs:

    pip install .[sphinx]
    make html

They will end up in _build/html/

(this note is here and not in README.md because, in this case, README.md is the front-page)
"""

from setuptools import setup, find_packages

setup(
    name="neuro.polymtl.ca",
    python_requires=">=3.6",
    author="NeuroPoly",
    extras_require={
        "sphinx": [
            "myst-parser",
            "ghapi",
            "sphinx-book-theme",
            "sphinx-panels",
            "sphinx-design~=0.0.11", # pinned because of this bug https://github.com/pydata/pydata-sphinx-theme/pull/50# and that the patched sphinx-book-theme isn't out yet: https://github.com/executablebooks/sphinx-book-theme/issues/428#issuecomment-966021270
            "sphinx~=4.2.0", # TODO: unpin when the next sphinx-book-theme is released
        ],
    },
)
