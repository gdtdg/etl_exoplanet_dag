import time

import requests

from config_file import csv_file_cleaned, csv_file
from etl_extract import extract_csv, remove_hashtag_lines_in_csv
from etl_load import load_in_elasticsearch, handle_response, create_index_with_mapping, delete_index
from etl_logs import log_summary, log_info
from etl_mapping_elasticsearch import mapping
from etl_transform import transform_row


def main():
    remove_hashtag_lines_in_csv(csv_file, csv_file_cleaned)
    log_info("CSV file has been cleaned.", False)

    reader, file = extract_csv(csv_file_cleaned)

    transformed_rows = []
    for row in reader:
        transform_row(row)
        transformed_rows.append(row)
    log_info("All rows transformed", False)

    delete_index("exoplanet_csv")
    log_info("Index deleted", False)

    create_index_with_mapping("exoplanet_csv", mapping)
    log_info("Index with mapping created", False)

    response = load_in_elasticsearch(transformed_rows)
    rows_posted, error_count = handle_response(response)

    file.close()
    return rows_posted, error_count


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings()
    log_info("Process started", True)

    start = time.time()
    rows_posted, error_count = main()
    end = time.time()
    elapsed = end - start

    log_summary(csv_file_cleaned, elapsed, rows_posted, error_count)
