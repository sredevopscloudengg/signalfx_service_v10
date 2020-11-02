import requests

# signalfx service rest endpoint
signalfx_response = requests.post('http://127.0.0.1:4996/', json={'id': 'i-0085adkdfjkj2895', 'description': 'This server is unhealthy'})

# validate signalfx http response
assert signalfx_response.status_code == 200

# validate signalfx content type
assert signalfx_response.headers['Content-Type'] == 'application/json'

# validate signalfx json params
signalfx_response_json = signalfx_response.json()
assert signalfx_response_json['id'] == 'i-0085adkdfjkj2895'
assert signalfx_response_json['description'] == 'This server is unhealthy'
