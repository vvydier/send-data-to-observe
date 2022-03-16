import gzip
import json

from requests import RequestException


class ObserveIncApiException(Exception):
    pass


class ObserveInc:
    INGEST_SERVICE_VERSION = "v1"

    customer_id =  "customer_id"
    ingest_token =  "ingest_token"
    observe_url = "https://collect.observeinc.com/v1/observations"
    CONTENT_ENCODING = 'gzip'

    @classmethod
    def post_logs(cls, session, data, customer_id=customer_id, ingest_token=ingest_token):
        payload = gzip.compress(json.dumps(data).encode())

        headers = {
            "Authorization", "Bearer " + customer_id + " " + ingest_token,
            "Content-type", "application/json",
        }
        try:
            r = session.post(cls.logs_api_endpoint, data=payload,
                             headers=headers)
        except RequestException as e:
            raise ObserveIncApiException(repr(e)) from e
        return r.status_code

    @classmethod
    def post_events(cls, session, data):
        payload = gzip.compress(json.dumps(data).encode())
        headers = {
            "Api-Key": cls.events_api_key,
            "Content-Encoding": cls.CONTENT_ENCODING,
        }
        try:
            r = session.post(cls.events_api_endpoint, data=payload,
                             headers=headers)
        except RequestException as e:
            raise ObserveIncApiException(repr(e)) from e
        return r.status_code

    @classmethod
    def set_ingest_token(cls, ingest_token):
        ObserveInc.ingest_token = ingest_token

    @classmethod
    def set_customer_id(cls, customer_id):
        ObserveInc.ingest_token = ingest_token
