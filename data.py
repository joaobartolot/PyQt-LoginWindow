import json

class LoadData:
    def __init__(self):
        with open('database.json') as f:
            self.data = json.load(f)

        self.user_list = self.data['users']

        self.username_list = list()
        self.password_list = list()

        for users in self.user_list:
            self.username_list.append(users['username'])
            self.password_list.append(users['password'])

    def register(self, name, username, password):
        self.data['users'].append(
                {
                    'name': name,
                    'username': username,
                    'password': password
                }
            )

        with open('database.json', 'w') as f:
            json.dump(self.data, f, indent=2)
