from rich.segment import Segment
from rich.style import Style
segments = [Segment('Hello'), Segment('World')]
styled_segments = Segment.apply_style(segments=segments, style=Style(color='red'), post_style=None)
