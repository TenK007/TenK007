import requests

class DietRecommender:
    def __init__(self, user_profile):
        self.user_profile = user_profile

    def generate_meal_plan(self):
        # In a real application, this would use a more sophisticated algorithm
        # to generate a personalized meal plan based on the user's profile
        # and dietary requirements.
        # For now, we'll just search for recipes based on the user's
        # dietary preferences.
        dietary_preferences = self.user_profile.dietary_preferences
        if not dietary_preferences:
            return {"error": "No dietary preferences specified"}

        # For simplicity, we'll just use the first dietary preference
        # to search for recipes.
        query = dietary_preferences[0]
        response = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?c={query}")
        data = response.json()

        if not data["meals"]:
            return {"error": f"No recipes found for {query}"}

        # We'll just return the first 3 meals as a sample meal plan.
        meal_plan = {}
        if len(data["meals"]) >= 1:
            meal_plan["breakfast"] = data["meals"][0]["strMeal"]
        if len(data["meals"]) >= 2:
            meal_plan["lunch"] = data["meals"][1]["strMeal"]
        if len(data["meals"]) >= 3:
            meal_plan["dinner"] = data["meals"][2]["strMeal"]

        return meal_plan
