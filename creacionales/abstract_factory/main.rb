
require "./abstract_factories.rb"


puts "Makin' a paint in soft paper"

soft_paper = SoftPaperFactory.get_paper
soft_pen = SoftPaperFactory.get_pen

soft_paper.pen = soft_pen

soft_paper.paint

puts "Makin' a paint in hard paper"

hard_paper = HardPaperFactory.get_paper
hard_pen = HardPaperFactory.get_pen

hard_paper.pen = hard_pen

hard_paper.paint