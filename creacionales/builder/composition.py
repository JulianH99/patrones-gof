# The whole product
class Composition:
    
    """ The final product.
    A composition is constructed by the `Director' class using the
    parts made by `Builder'.
        """

    def __init__(self):
        self.__extra  = None
        self.__bag  = None
        self.__collection    = None

    """ The respectives sets.
        """

    def setCollection(self, collection):
        self.__collection = collection

    def setExtra(self, extra):
        self.__extra = extra

    def setBag(self, bag):
        self.__bag = bag

    """ The description in display about each composition.
        """

    def description(self):
        print ("Collection: %s" % self.__collection.exclusivity)
        print ("Bag Style: %s" % self.__bag.style)
        print ("extras size: %s\'" % self.__extra.size)