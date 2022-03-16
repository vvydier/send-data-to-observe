import urllib.request
import json
customer_id = "customer_id"
ingest_token = "dingest_token"
observe_url = "https://collect.observeinc.com/v1/observations"
path = "test"
host = "localhost"

data = [
    {
        'url': '/rest/shifts',
        'params': {'user_id': 0, 'other_stuff': 'value'},
        'method': 'post',
    },
    {
        'url': '/rest/shifts',
        'params': {'user_id': 1,'other_stuff': 'value'},
        'method':'post',
    },
]

payload = json.dumps(data)
# payload = str.format(data)

req = urllib.request.Request(url=observe_url + '/' +
                                 path + '?' + "host=" + host,
                             method="POST",
                             data=bytes(payload.encode("utf-8")))

req.add_header("Authorization", "Bearer " + customer_id + " " + ingest_token)
req.add_header("Content-type", "application/json")


# Send the request
response = urllib.request.urlopen(req)
json_response = response.read().decode("utf-8")

# Print the output for debugging
print(payload)
print(json_response)