from requests import get
server = get("https://api.ipify.org").text
print(server)
