from flask import Flask, jsonify, request
import json
import signalfx

# initialize Flask
app = Flask(__name__)

# decorator to accept post requests
@app.route('/', methods=['POST'])
def get_post_params():
    post_params = request.get_json()
    ret_val = validate_params(post_params)
    if(ret_val == 'validated'):
        signalfx_event = 'unhealthy'
        post_signalfx_event(signalfx_event)
    return jsonify(post_params)

# validate post params
def validate_params(post_params):
    event_desc = post_params['description']
    event_desc_lc = event_desc.lower()

    if(len(event_desc) > 0):
        if(isinstance(event_desc, str)):
            if("unhealthy" in event_desc_lc):
                return "validated"
            else:
                return "not validated"

# post event to signalfx rest endpoint
def post_signalfx_event(signalfx_event):
    '''
    sfx = signalfx.SignalFx(ingest_endpoint='https://ingest.{REALM}.signalfx.com')
    with signalfx.SignalFx().ingest('ORG_TOKEN') as sfx:
        sfx.send_event(
            event_type = signalfx_event)
    '''
    # signalfx trail version valid only for 10 days
    ORG_TOKEN='2uVk73DtBX4ke2gu4ir23w'
    sfx = signalfx.SignalFx(ingest_endpoint='https://ingest.us1.signalfx.com/v2/event')
    with signalfx.SignalFx().ingest(ORG_TOKEN) as sfx:
        sfx.send_event(event_type = signalfx_event)
    
    return

# start service at port 4996
if __name__ == '__main__':
    app.run(debug=True,port=4996,host='0.0.0.0')