from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence, 'Working...', None, True, console, False, None, 10, style='bar.back', show_speed=True)