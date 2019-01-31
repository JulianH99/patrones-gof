# The whole product
class Composition:
    
    """ The final product.
    A composition is assembled by the `Director' class from
    parts made by `Builder'. Both these classes have
    influence on the resulting object.
    """

    def __init__(self):
        self.__extra  = list()
        self.__bag  = None
        self.__collection    = None

    def setCollection(self, collection):
        self.__collection = collection

    def addExtra(self, extra):
        self.__extra.append(extra)

    def setBag(self, bag):
        self.__bag = bag

    def description(self):
        print ("Collection: %s" % self.__collection.exclusivity)
        print ("Bag Style: %d" % self.__bag.style)
        print ("extras size: %d\'" % self.__extra[0].size)