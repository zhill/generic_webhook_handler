# generic_webhook_handler
A very simple Flask app for handling inbound webhooks.

Runs on port 8000 by default and echos all POST requests to any path into stdout. Built for simple Docker deployment.

Usage with Docker:
docker run -p 8000:8000 --name handler1 <tag>

To watch the incoming requests:
docker logs handler1 --follow

The handler does not require any auth/authz.

