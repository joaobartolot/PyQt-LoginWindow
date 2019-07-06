import json

class Load:
    def __init__():
        with open('database.json') as f:
            data = json.load(f)

        self.data = data
        self.user_list = data['users']

def register(name, username, password):
    data = load().data

    data['users'].append(
            {
                'name': name,
                'username': username,
                'password': password
            }
        )

    with open('database.json', 'w') as f:
        json.dump(data, f, indent=2)
