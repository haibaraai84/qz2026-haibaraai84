import json


class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1

    def add_user(self, name, age):
        user = {
            "id": self.next_id,
            "name": name,
            "age": age
        }
        self.users.append(user)
        self.next_id += 1
        return user

    def get_user(self, user_id):
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None

    def update_age(self, user_id, new_age):
        user = self.get_user(user_id)
        if user is None:
            return False
        user["age"] = new_age
        return True

    def remove_user(self, user_id):
        user = self.get_user(user_id)
        if user is None:
            return False
        self.users.remove(user)
        return True

    def list_users(self):
        return self.users
