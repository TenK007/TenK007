import json

class DataStorage:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_data_file = f"{user_id}_data.json"

    def save_user_profile(self, user_profile):
        with open(self.user_data_file, "w") as f:
            json.dump(user_profile.__dict__, f)

    def load_user_profile(self):
        try:
            with open(self.user_data_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def save_meal_log(self, meal_log):
        with open(self.user_data_file, "a") as f:
            json.dump(meal_log, f)
            f.write("\n")
