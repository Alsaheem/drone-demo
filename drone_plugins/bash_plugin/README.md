to run the application locally

docker run --rm \
  -e PLUGIN_METHOD=post \
  -e PLUGIN_URL=http://hook.acme.com \
  -e PLUGIN_BODY=hello \
  alsaheem/webhook