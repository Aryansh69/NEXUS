import requests
data = {"title": "Build NEXUS","completed": False}
response = requests.post(
    "https://jsonplaceholder.typicode.com/todos",
    json=data
)
result=response.json()
print(result)
todo_id=result["id"]
ans = requests.get(
    f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
)
print(ans.json())