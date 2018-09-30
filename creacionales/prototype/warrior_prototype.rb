require "./warrior.rb"

class WarriorPrototype

    @@warrior = nil

    def initialize
        raise 'not possible'
    end

    def self.get_warrior
        if @@warrior == nil
            @@warrior = Warrior.new 30, 40
        end
        @@warrior.clone
    end

end