from datetime import datetime

from shared_modules.logger import trace_logging

SQL_FORMAT = '%Y-%m-%d %H:%M:%S'


class ProxyDateTime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(datetime, *args, **kwargs)

    @trace_logging()
    def date_time_now_to_sql(self) -> str:
        return ProxyDateTime.date_time_to_sql(self.now())

    @staticmethod
    @trace_logging()
    def sql_to_datetime(sql_date: str) -> datetime:
        return datetime.strptime(sql_date, SQL_FORMAT)

    @staticmethod
    @trace_logging()
    def date_time_to_sql(date: datetime) -> str:
        return date.strftime(SQL_FORMAT)
