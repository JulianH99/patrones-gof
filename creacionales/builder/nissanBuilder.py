from builder import Builder
from compositionParts import Extra, Bag, Collection

class NissanBuilder(Builder):

    """ Concrete Builder implementation.
    This class builds parts for Nissan's family cars.
    """

    def getExtra(self):
        extra = Extra()
        extra.size = 22
        return extra

    def getBag(self):
        bag = Bag()
        bag.style = 400
        return bag

    def getCollection(self):
        collection = Collection()
        collection.exclusivity = "SUVV"
        return collection
        