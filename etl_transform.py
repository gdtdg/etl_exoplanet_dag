def transform_row(row):
    transform_disc_pubdate_last_digit(row)
    transform_pl_pubdate_last_digit(row)
    transform_pl_pubdate_date_format(row)
    transform_releasedate_date_format(row)
    transform_rowupdate_date_format(row)


def transform_disc_pubdate_last_digit(row):
    if row['disc_pubdate'][-2:] == "00":
        delete_last_digit = row['disc_pubdate'][:-1] + "1"
        row['disc_pubdate'] = delete_last_digit


def transform_pl_pubdate_last_digit(row):
    if row['pl_pubdate'][-2:] == "00":
        delete_last_digit = row['pl_pubdate'][:-1] + "1"
        row['pl_pubdate'] = delete_last_digit


def transform_pl_pubdate_date_format(row):
    if len(row['pl_pubdate']) != 7:
        row['pl_pubdate'] = row['pl_pubdate'][:7]


def transform_releasedate_date_format(row):
    if len(row['releasedate']) != 10:
        row['releasedate'] = row['releasedate'][:10]


def transform_rowupdate_date_format(row):
    if len(row['rowupdate']) == 0:
        row['rowupdate'] = row['releasedate']
