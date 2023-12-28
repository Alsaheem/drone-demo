docker build -t alsaheem/webhook .
docker push alsaheem/webhook
docker run --rm \
  -e PLUGIN_METHOD=GET \
  -e PLUGIN_URL=https://wallet-api-qa.yassir.io/api/v1/actuator/health \
  alsaheem/webhook
