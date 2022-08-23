import csv


def remove_hashtag_lines_in_csv(csv_file, cleaned_csv_file):
    file_to_clean = open(csv_file, "r")
    lines = file_to_clean.readlines()
    file_cleaned = open(cleaned_csv_file, "w")
    for line in lines:
        if not line.startswith("#"):
            file_cleaned.write(line)
    file_to_clean.close()
    file_cleaned.close()


def extract_csv(csv_file):
    """
    Take a csv file and return it as a dictionary.
    """
    file = open(csv_file, "r")
    reader = csv.DictReader(file)
    return reader, file
