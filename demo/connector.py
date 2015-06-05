from zope.interface import implementer
from iconnector import IConnector

@implementer(IConnector)
class Connector(object):

    def __init__(self,x=None):
        self.x = x

    # Yes, this is meant to be here.
    # With this in place the utility will
    # flag this method as missing. Try
    # putting it in and you'll see the
    # error going away.
#    def connect( self, port ):
#        pass

def main():
    from iverifier import verifyInterfaces
    verifyInterfaces()

if __name__ == "__main__":
    main()
