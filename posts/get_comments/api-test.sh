#!/usr/bin/bash
KEY=$(cat api-key)
curl $1 -H \
  "x-api-key: $KEY" \
  -H "Content-Type: application/json" \
  -d @example_request.json \
  https://cx00ooxpol.execute-api.us-west-2.amazonaws.com/default/post_comment | python -mjson.tool
