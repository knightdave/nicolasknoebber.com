#!/usr/bin/bash
zip -r get_comments.zip index.js
aws lambda update-function-code --function-name get_comments --zip-file fileb://get_comments.zip
rm get_comments.zip
