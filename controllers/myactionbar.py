"""."""
from kivy.uix.actionbar import ActionBar
from kivy.properties import BooleanProperty


class MyActionBar(ActionBar):
    """."""

    prev = BooleanProperty(defaultvalue=False)

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)
