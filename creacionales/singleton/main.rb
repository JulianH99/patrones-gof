require "./logger_singleton.rb"


logger = LoggerSingleton.get_logger


logger.info "This is an info message"

logger.error "This is an error message"