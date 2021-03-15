from datetime import datetime

from shared_modules.logger import trace_logging

SQL_FORMAT = '%Y-%m-%d %H:%M:%S'


class ProxyDateTime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(datetime, *args, **kwargs)

    @staticmethod
    @trace_logging()
    def date_time_to_sql(date: datetime) -> str:
        return date.strftime(SQL_FORMAT)
