"""."""
from kivy.uix.actionbar import ActionBar
from kivy.properties import BooleanProperty, Property  # pylint: disable=no-name-in-module


class MyActionBar(ActionBar):
    """."""

    prev = BooleanProperty(False)
    func = Property(lambda: ...)

    def __init__(self, *args, **kwargs):
        """."""
        super().__init__(*args, **kwargs)
