from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from config_file import es_url, auth, index
from etl_logs import log_error

es = Elasticsearch([es_url], basic_auth=auth, verify_certs=False)


def delete_index(index_name):
    es.options(ignore_status=[400, 404]).indices.delete(index=index_name)


def create_index_with_mapping(index_name, body):
    es.indices.create(
        index=index_name,
        body=body
    )


def load_in_elasticsearch(rows):
    actions = [transform_row_in_action(row) for row in rows]
    errors = bulk(client=es, actions=actions, stats_only=False, raise_on_error=False)
    return {"errors": errors, "size": len(rows)}


def transform_row_in_action(row):
    action = {
        '_index': index,
        '_id': row["rowid"],
        '_source': row
    }
    return action


def handle_response(response: dict):
    errors = response["errors"][1]
    size = response["size"]

    for r in errors:
        log_error(r)

    error_count = len(errors)
    rows_posted = size - error_count

    return rows_posted, error_count
