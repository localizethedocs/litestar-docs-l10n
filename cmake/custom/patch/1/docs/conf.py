from __future__ import annotations

import importlib.metadata
import os
from functools import partial
from typing import Any, TYPE_CHECKING
from sphinx.locale import _


if TYPE_CHECKING:
    from sphinx.addnodes import document
    from sphinx.application import Sphinx


project = "Starlite"
copyright = "2023, Starlite-API"
author = "Starlite-API"
release = os.getenv("_STARLITE_DOCS_BUILD_VERSION", importlib.metadata.version("starlite").rsplit(".")[0])

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "auto_pytabs.sphinx_ext",
    "tools.sphinx_ext",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "msgspec": ("https://jcristharif.com/msgspec/", None),
    "anyio": ("https://anyio.readthedocs.io/en/stable/", None),
    "multidict": ("https://multidict.aio-libs.org/en/stable/", None),
    "sqlalchemy": ("https://docs.sqlalchemy.org/en/14/", None),
}


napoleon_google_docstring = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_attr_annotations = True

autoclass_content = "class"
autodoc_class_signature = "separated"
autodoc_default_options = {
    "special-members": "__init__",
    "show-inheritance": True,
}
autodoc_member_order = "bysource"
autodoc_typehints_format = "short"

auto_pytabs_min_version = (3, 8)
auto_pytabs_max_version = (3, 11)

autosectionlabel_prefix_document = True

suppress_warnings = ["autosectionlabel.*"]

html_theme = "litestar_sphinx_theme"
html_static_path = ["_static"]
html_js_files = ["versioning.js"]
html_css_files = ["style.css"]
html_show_sourcelink = False
html_title = "Starlite Framework"


html_theme_options = {
    "use_page_nav": False,
    "github_repo_name": "litestar",
    "logo": {
        "link": "https://litestar.dev",
    },
    "extra_navbar_items": {
        _("Documentation"): "index",
        _("Community"): {
            _("Contributing"): {
                "description": _("Learn how to contribute to the Litestar project"),
                "link": "https://docs.litestar.dev/2/contribution-guide.html",
                "icon": "contributing",
            },
            _("Code of Conduct"): {
                "description": _("Review the etiquette for interacting with the Litestar community"),
                "link": "https://github.com/litestar-org/.github/blob/main/CODE_OF_CONDUCT.md",
                "icon": "coc",
            },
        },
        _("About"): {
            _("Litestar Organization"): {
                "description": _("Details about the Litestar organization"),
                "link": "about/organization",
                "icon": "org",
            },
            _("Releases"): {
                "description": _("Details about the Litestar release process"),
                "link": "about/litestar-releases",
                "icon": "releases",
            },
        },
        _("Release notes"): {
            _("2.x Changelog"): "https://docs.litestar.dev/2/release-notes/changelog.html",
            _("1.x Changelog"): "https://docs.litestar.dev/1/release-notes/changelog.html",
        },
        _("Help"): "https://github.com/orgs/litestar-org/discussions",
    },
}


def update_html_context(
    app: Sphinx, pagename: str, templatename: str, context: dict[str, Any], doctree: document
) -> None:
    context["generate_toctree_html"] = partial(context["generate_toctree_html"], startdepth=0)


def setup(app: Sphinx) -> dict[str, bool]:
    app.connect("html-page-context", update_html_context, priority=1000)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
