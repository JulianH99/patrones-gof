class Logger

    def info message
        puts format_message message, "INFO"
    end

    def error message
        puts format_message message, "ERROR"
    end

    def format_message message, message_type
        "[#{message_type}]: #{Time.now} - #{message}"
    end

    private :format_message


end
