
class Paper

    @pen = nil

    attr_writer :pen
    
    def initialize 
        
    end

    def paint
        puts "Painting in #{self.class.name} with #{@pen.name}"
    end

end


class SoftPaper < Paper

end


class HardPaper < Paper

end