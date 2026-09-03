import requests
id=int(input("enter ur user id :"))
params = {
    "userId": id
}
a=requests.get("https://jsonplaceholder.typicode.com/todos", params=params)
ans=a.json()
for i in ans:
    print(i["title"])
