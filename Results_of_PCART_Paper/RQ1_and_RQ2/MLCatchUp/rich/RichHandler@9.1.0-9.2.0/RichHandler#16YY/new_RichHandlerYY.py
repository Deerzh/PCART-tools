import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.highlighter import ReprHighlighter
rich_handler = RichHandler(show_time=True, show_level=True, enable_link_path=True, highlighter=ReprHighlighter(), show_path=True, tracebacks_show_locals=False)
