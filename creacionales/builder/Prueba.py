from jeepBuilder import JeepBuilder
from nissanBuilder import NissanBuilder
from director import Director

def main():
    jeepBuilder = JeepBuilder()
    nissanBuilder = NissanBuilder()

    director = Director()

    # Build Jeep
    print ("Jeep")
    director.setBuilder(jeepBuilder)
    jeep = director.getComposition()
    jeep.description()

    print ("")

    # Build Nissan
    print ("Nissan")
    director.setBuilder(nissanBuilder)
    nissan = director.getComposition()
    nissan.description()

if __name__ == "__main__":
    main()