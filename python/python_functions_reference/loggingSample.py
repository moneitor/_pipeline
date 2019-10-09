# IMPORT STANDARD MODULES
import logging
import sys

class ErrorFilter(logging.Filter):
    """
    Pass any message meant for stderr.
    """
    def __init__(self, *args, **kwargs):
        super(ErrorFilter, self).__init__(*args, **kwargs)
    # end __init__
    
    def filter(self, record):
        """
        If the record does is not logging.INFO, return True
        """
        return record.levelno != logging.INFO
    # end filter
# end ErrorFilter

class OutFilter(logging.Filter):
    """
    Pass any message meant for stderr.
    """
    def __init__(self, *args, **kwargs):
        super(OutFilter, self).__init__(*args, **kwargs)
    # end __init__
    
    def filter(self, record):
        """
        If the record does is logging.INFO, return True
        """
        return record.levelno == logging.INFO
    # end filter
# end OutFilter

def get_terminal_logger(name=None):
    """
    Returns a logging.Logger object as per logging.getLogger(name), but with
    logging.INFO messages filtered to sys.stdout and all other levels to
    sys.stderr.  This is to provide for standard stream redirection.

    :key name: name of the logger to use
    :type name: str
    :returns: the prepared logger
    :rtype: logging.Logger
    """
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    basic_formatter = logging.Formatter(fmt='%(message)s')
    
    # add stderr handling
    error = logging.StreamHandler(stream=sys.stderr)
    error.addFilter(ErrorFilter())
    error.setFormatter(basic_formatter)
    logger.addHandler(error)
    
    # add stdout handling
    out = logging.StreamHandler(stream=sys.stdout)
    out.addFilter(OutFilter())
    out.setFormatter(basic_formatter)
    logger.addHandler(out)

    # finally return the logger
    return logger
# end get_terminal_logger

def main():
    """
    Simple demonstration if module is run directly.
    """
    logger = get_terminal_logger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.debug('This is a logging.DEBUG level message')
    logger.info('This is a logging.INFO level message')
    logger.warning('This is a logging.WARNING level message')
    logger.error('This is a logging.ERROR level message')
    logger.critical('This is a logging.CRITICAL level message')
# end main

if __name__ == '__main__':
    main()
    
