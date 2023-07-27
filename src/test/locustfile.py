from locust import HttpUser, task

class HttpBrenmarch(HttpUser):
    @task
    def http_cache(self):
        self.client.get("/api/v1/query/demo")
        self.client.get("/api/v1/query/cache")
        self.client.get("/api/v1/query/cachedep")
        self.client.get("/api/v1/query/redis")