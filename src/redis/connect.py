import redis
import json

r = redis.Redis(decode_responses=True).from_url('redis://localhost:6379')

dict_data = {
    "employee_name": "Adam Adams",
    "employee_age": 30,
    "position": "Software Engineer",
}

print(r.ping())

print("exists", r.exists("full_name"))

r.set("full_name", json.dumps(dict_data), 200)

response = r.get("full_name")

print(response.decode('utf-8'))

print(type(response.decode('utf-8')))

print(json.loads(response.decode('utf-8')))


def cache_redis():
    try:
        cache = redis.Redis(decode_responses=True).from_url('redis://localhost:6379')

        return cache
    except Exception as e:
        print("Error connect Redis", e)


x = cache_redis()
print(x.ping())
