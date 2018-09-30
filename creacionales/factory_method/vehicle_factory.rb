require "./vehicles.rb"

class VehicleFactory

    def initialize
        raise SecurityError
    end

    def VehicleFactory.get_vehicle vehicle_name
        
        {:ACar => ACar, :ABicicle => ABicicle}[vehicle_name].new
    
    end

    
end