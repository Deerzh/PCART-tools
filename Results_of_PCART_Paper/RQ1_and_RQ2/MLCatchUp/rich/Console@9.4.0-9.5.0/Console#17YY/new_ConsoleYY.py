from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(highlighter=ReprHighlighter(), soft_wrap=False, stderr=False, style=None)