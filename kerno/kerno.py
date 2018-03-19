"""The Kerno class."""


class Kerno:
    """Core of an application, integrating decoupled resources.

    The Kerno instance is used at runtime; at startup it is instantiated by
    the "Eko" configurator.
    """

    def __init__(self, settings=None):
        """Construct. The ``settings`` are a dict of dicts."""
        self.settings = settings
        # self.actions = ActionRegistry(kerno=self)
