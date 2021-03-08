import unittest
from unittest.mock import patch
from shared_modules.logger import Logger, LogLevel


class LoggerTest(unittest.TestCase):
    """
        This is a test for the Logger
    """
    @patch('builtins.print')
    def test_log_trace(self, mock_print):
        result = Logger()
        result.log_trace("this is trace")

        mock_print.assert_called_with("TRACE: this is trace")

    @patch('builtins.print')
    def test_log_debug(self, mock_print):
        result = Logger()
        result.log_debug("this is debug")

        mock_print.assert_called_with("DEBUG: this is debug")

    @patch('builtins.print')
    def test_log_info(self, mock_print):
        result = Logger()
        result.log_info("this is info")

        mock_print.assert_called_with("INFO:  this is info")

    @patch('builtins.print')
    def test_log_warning(self, mock_print):
        result = Logger()
        result.log_warning("this is warning")

        mock_print.assert_called_with("WARN:  this is warning")

    @patch('builtins.print')
    def test_log_error(self, mock_print):
        result = Logger()
        result.log_error("this is error")

        mock_print.assert_called_with("ERR:   this is error")

    @patch('builtins.print')
    def test_log_when_log_level_too_high(self, mock_print):
        result = Logger(LogLevel.error)
        result.log_warning("this is warning and not shown")

        mock_print.assert_not_called()
