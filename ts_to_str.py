from datetime import datetime


def ts_to_str(timestamp):
    """
    时间戳转换成字符串
    :param timestamp: 时间戳
    :return: 字符串时间
    """
    trans_time = datetime.fromtimestamp(timestamp)
    str_time = trans_time.strftime("%Y-%m-%d %H:%M:%S")
    return str_time


def str_to_ts(time_str, str_format):
    """
    字符串转换成时间戳
    :param time_str: 字符串时间
    :param str_format: 字符串时间的格式 like:"%Y-%m-%d %H:%M:%S"
    :return: 时间戳
    """
    trans_time = datetime.strptime(time_str, str_format)
    timestamp = trans_time.timestamp()
    return timestamp

