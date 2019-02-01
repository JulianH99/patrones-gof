from builder import Builder
from compositionParts import Extra, Bag, Collection

class RomanticBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for a collection of Romantic Books.
    """

    def getExtra(self):
        extra = Extra()
        extra.size = "Some poster"
        return extra

    def getBag(self):
        bag = Bag()
        bag.style = "Light"
        return bag

    def getCollection(self):
        collection = Collection()
        collection.exclusivity = "High"
        return collection
        