class Warrior
    @attack = 0
    @defense = 0

    def initialize attack, defense
        @attack = attack
        @defense = defense
    end


    def fight
        puts "Warrior figthing with #{@attack} attack and #{@defense} defense"
    end

end