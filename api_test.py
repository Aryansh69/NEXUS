import requests

data = {
    "title": "Learning APIs",
    "completed": False
}

response = requests.post("https://jsonplaceholder.typicode.com/todos",json=data)

print(response)
result=response.json()
print(result)