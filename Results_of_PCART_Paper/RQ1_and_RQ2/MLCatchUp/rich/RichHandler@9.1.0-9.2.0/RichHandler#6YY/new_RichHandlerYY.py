import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(highlighter=ReprHighlighter(), tracebacks_show_locals=False)