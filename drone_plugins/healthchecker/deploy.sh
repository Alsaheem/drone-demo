docker build -t alsaheem/healthchecker .
docker push alsaheem/healthchecker

docker run --rm \
  -e PLUGIN_PASS_NUM=10 \
  -e PLUGIN_HEALTH_URL=https://wallet-api-qa.yassir.io/api/v1/actuator/health \
  alsaheem/healthchecker
