class Pen
    @name = nil?

    attr_reader :name
    
    def initialize name
        @name = name
    end
end


class HardPen < Pen
    def initialize
        @name = 'hard pen'
    end
end

class SoftPen < Pen
    def initialize
        @name = "soft pen"
    end
end

