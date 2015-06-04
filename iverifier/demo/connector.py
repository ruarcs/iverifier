from zope.interface import implementer
from iconnector import IConnector

@implementer(IConnector)
class Connector(object):

    def __init__(self,x=None):
        self.x = x

#    def connect( b ):
#        pass

def main():
    from iverifier import verifyInterfaces
    verifyInterfaces()

if __name__ == "__main__":
    main()
