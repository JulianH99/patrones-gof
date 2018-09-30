require "./papers.rb"
require "./pens.rb"

class BaseFactory

    def initialize
        raise 'Not possible'
    end

    def self.get_paper
        raise 'Not possible'
    end

    def self.get_pen
        raise 'Not possible'
    end

end

class HardPaperFactory < BaseFactory

    def initialize
        
    end

    def self.get_paper
        HardPaper.new 
    end

    def self.get_pen
        HardPen.new
    end

end

class SoftPaperFactory < BaseFactory
    def initialize
    end

    def self.get_paper
        SoftPaper.new
    end

    def self.get_pen
        SoftPen.new
    end

end
