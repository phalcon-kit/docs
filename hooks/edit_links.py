"""Keep site edit links on the source repository that owns each page."""
from mkdocs.structure.pages import Page


def on_page_markdown(markdown: str, *, page: Page, **kwargs) -> str:
    """Route narrative edits to Core and hide edits of generated API pages."""
    source = page.file.src_uri
    if source.startswith('guides/'):
        page.edit_url = 'https://github.com/phalcon-kit/core/edit/master/' + source
    elif source.startswith('api/'):
        page.edit_url = None
    return markdown
