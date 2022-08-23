import sys
from datetime import datetime

from config_file import error_log_file, log_file, es_url


def log_summary(csv_file, elapsed, rows_posted, error_count):
    log = f"{datetime.now()}: Process done. From {csv_file} to {es_url} " \
          f"in {elapsed:.2f} seconds, {rows_posted} rows read for {error_count} error(s).\r"

    print(log)
    with open(log_file, 'a') as file:
        file.write(log)


def log_error(message):
    log = f"{datetime.now()}: {message}\r"

    print(log, file=sys.stderr)
    with open(error_log_file, 'a') as file:
        file.write(log)


def log_info(message, log_to_file=False):
    log = f"{datetime.now()}: {message}\r"

    print(log)
    if log_to_file:
        with open(log_file, 'a') as file:
            file.write(log)
