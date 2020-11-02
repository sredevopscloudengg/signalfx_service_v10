#!/bin/bash

# safely abort shell command
set -e

# start signalfx service
python3 signalfx_post_event.py