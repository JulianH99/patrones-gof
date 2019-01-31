from composition import Composition

class Director:
    
    """ Controls the construction process.
    Director has a builder associated with him. Director then
    delegates building of the smaller parts to the builder and
    assembles them together.
    """

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The algorithm for assembling a car
    def getComposition(self):
        composition = Composition()

        # First goes the collection
        collection = self.__builder.getCollection()
        composition.setCollection(collection)

        # Then bag
        bag = self.__builder.getBag()
        composition.setBag(bag)

        # And four extras
        i = 0
        while i < 4:
            extra = self.__builder.getExtra()
            composition.addExtra(extra)
            i += 1

        return composition