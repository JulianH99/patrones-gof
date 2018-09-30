require "./logger.rb"

class LoggerSingleton

    @@logger = nil

    def initialize
        raise 'Not possible'
    end

    def LoggerSingleton.get_logger
        if @@logger === nil
            @@logger = Logger.new
        end
        @@logger
    end
end