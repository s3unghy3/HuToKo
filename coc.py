import requests

header = {
    'Accept': 'application/json',
    'authorization':'Bearer <API token>',
}
def get_user():
    response = requests.get('https://api.clashofclans.com/v1/players/%23LU298PLJP', header)
    user_json = response.json()
    print(user_json)

get_user()
