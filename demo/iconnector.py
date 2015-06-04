from zope.interface import Interface

class IConnector(Interface):

    def connect( port ):
        """Connect to the thing."""
