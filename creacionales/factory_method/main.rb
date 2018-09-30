require "./vehicle_factory.rb"


puts "Creating a car..."

mycar = VehicleFactory.get_vehicle :ACar

puts mycar.run


puts "Creacing a bicicle..."
mybi = VehicleFactory.get_vehicle :ABicicle

puts mybi.run
