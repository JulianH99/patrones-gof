require "./warrior_prototype.rb"

warriors = Array.new

(0..10).each do
    warriors += [WarriorPrototype.get_warrior]
end


warriors.each do |warrior|
    puts warrior.fight
end