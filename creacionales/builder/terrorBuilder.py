from builder import Builder
from compositionParts import Extra, Bag, Collection

class TerrorBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for a collection of Terror Books.
    Each get has a variation according to the kind of builder
    """

    def getExtra(self):
        extra = Extra()
        extra.size = "Some fan art"
        return extra

    def getBag(self):
        bag = Bag()
        bag.style = "Dark"
        return bag

    def getCollection(self):
        collection = Collection()
        collection.exclusivity = "Low"
        return collection