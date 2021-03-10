from datetime import datetime


class ProxyDateTime(datetime):
    def __new__(cls, *args, **kwargs):
        return datetime.__new__(datetime, *args, **kwargs)


def sql_to_datetime(sql_date: str) -> datetime:
    return datetime.strptime(sql_date, '%Y-%m-%d %H:%M:%S')