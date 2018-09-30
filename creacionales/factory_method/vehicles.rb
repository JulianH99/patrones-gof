
    class BaseVehicle
        def run
            raise NotImplementedError
        end
    end


    class ACar < BaseVehicle
        def run
            puts "A car is running"
        end
    end

    class ABicicle < BaseVehicle
        def run
            puts "A wheel is going on"
        end

    end

