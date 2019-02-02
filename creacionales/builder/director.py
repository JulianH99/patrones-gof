import random
from composition import Composition

class Director:
    
    """ Just like indicates the name, is the one who "directs" 
    the construction process. Director has a builder associated with him, after 
    delegates building of the smaller parts to the builder and
    then une them together.
    """

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # The construction of a Car
    def getComposition(self):
        composition = Composition()

        # Star the collection
        collection = self.__builder.getCollection()
        composition.setCollection(collection)

        # Then bag
        bag = self.__builder.getBag()
        composition.setBag(bag)

        extra = self.__builder.getExtra()
        composition.setExtra(extra)    

        return composition