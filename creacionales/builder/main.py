from terrorBuilder import TerrorBuilder
from romanticBuilder import RomanticBuilder
from director import Director

def main():

    """
        The inicialization of a two kinds of builders
    """
    romanticBuilder = RomanticBuilder()
    terrorBuilder = TerrorBuilder()

    director = Director()

    # The construction of a terror Pack
    print ("Terror Pack")
    director.setBuilder(terrorBuilder)
    terrorCollection = director.getComposition()
    terrorCollection.description()

    print ("")

    # The construction of a romantic Pack
    print ("Romantic Pack")
    director.setBuilder(romanticBuilder)
    romanticCollection = director.getComposition()
    romanticCollection.description()

if __name__ == "__main__":
    main()