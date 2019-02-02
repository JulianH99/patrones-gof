from terrorBuilder import TerrorBuilder
from romanticBuilder import RomanticBuilder
from director import Director

def main():
    romanticBuilder = RomanticBuilder()
    terrorBuilder = TerrorBuilder()

    director = Director()

    # Build a terror Pack
    print ("Terror Pack")
    director.setBuilder(terrorBuilder)
    terrorCollection = director.getComposition()
    terrorCollection.description()

    print ("")

    # Build a romantic Pack
    print ("Romantic Pack")
    director.setBuilder(romanticBuilder)
    romanticCollection = director.getComposition()
    romanticCollection.description()

if __name__ == "__main__":
    main()