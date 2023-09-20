1. Create Flask application
2. Add prometheus wsgi middleware to route /metrics requests, little addon that is required for getting the /metrics endpoint
3. Create Dockerfile
4. Create the docker-compose.yml file
5. Let it run! (docker-compose up --build)
5. Add the Prometheus data source to Grafana
   a. You need to set the Prometheus server URL to http://prometheus:9090 and not http://localhsot:9090. When you're inside the Grafana container and you try to access localhost or 127.0.0.1, you're referencing the Grafana container itself, not the host machine or other containers. Therefore, you can't access the Prometheus service by using localhost. When you're using http://prometheus:9090, Grafana will work with Docker's internal DNS resolve.
6. Create custom dashboard