from logger_facade import LoggerFacade


def main():
    print("Using console logger")

    LoggerFacade.console_log(LoggerFacade.INFO, "an info message")

    print("-" * 10)

    print("Using html logger")

    LoggerFacade.html_log(LoggerFacade.ERROR, "an error message")

if __name__ == '__main__':
    main()
