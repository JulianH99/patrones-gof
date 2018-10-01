from loggers import LoggerLevels, ConsoleLogger, HtmlLogger


class LoggerFacade():

    console_logger = ConsoleLogger()
    html_logger = HtmlLogger('app')

    INFO = LoggerLevels.INFO

    ERROR = LoggerLevels.ERROR

    WARNING = LoggerLevels.WARNING

    @classmethod
    def console_log(cls, level, message):
        cls.console_logger.log(level, message)

    @classmethod
    def html_log(cls, level, message):
        cls.html_logger.log(level, message)
