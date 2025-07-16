import tkinter as tk
from tkinter import filedialog
from diet_planner.user.profile import UserProfile
from diet_planner.meal.logging import MealLogger
from diet_planner.meal.recommendation import DietRecommender
from diet_planner.data.storage import DataStorage

class DietPlannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Diet Planner")

        self.user_profile = None
        self.meal_logger = MealLogger()
        self.diet_recommender = None
        self.data_storage = None

        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Create the widgets
        self.create_widgets()

    def create_widgets(self):
        # Create the user profile widgets
        self.create_user_profile_widgets()

        # Create the meal logging widgets
        self.create_meal_logging_widgets()

        # Create the diet recommendation widgets
        self.create_diet_recommendation_widgets()

    def create_user_profile_widgets(self):
        # Create a frame for the user profile widgets
        self.user_profile_frame = tk.LabelFrame(self.main_frame, text="User Profile")
        self.user_profile_frame.pack(fill="x", padx=10, pady=10)

        # Create the user profile labels and entry fields
        self.age_label = tk.Label(self.user_profile_frame, text="Age:")
        self.age_label.grid(row=0, column=0, sticky="w")
        self.age_entry = tk.Entry(self.user_profile_frame)
        self.age_entry.grid(row=0, column=1)

        self.gender_label = tk.Label(self.user_profile_frame, text="Gender:")
        self.gender_label.grid(row=1, column=0, sticky="w")
        self.gender_entry = tk.Entry(self.user_profile_frame)
        self.gender_entry.grid(row=1, column=1)

        self.height_label = tk.Label(self.user_profile_frame, text="Height (cm):")
        self.height_label.grid(row=2, column=0, sticky="w")
        self.height_entry = tk.Entry(self.user_profile_frame)
        self.height_entry.grid(row=2, column=1)

        self.weight_label = tk.Label(self.user_profile_frame, text="Weight (kg):")
        self.weight_label.grid(row=3, column=0, sticky="w")
        self.weight_entry = tk.Entry(self.user_profile_frame)
        self.weight_entry.grid(row=3, column=1)

        self.health_goals_label = tk.Label(self.user_profile_frame, text="Health Goals:")
        self.health_goals_label.grid(row=4, column=0, sticky="w")
        self.health_goals_entry = tk.Entry(self.user_profile_frame)
        self.health_goals_entry.grid(row=4, column=1)

        self.activity_level_label = tk.Label(self.user_profile_frame, text="Activity Level:")
        self.activity_level_label.grid(row=5, column=0, sticky="w")
        self.activity_level_entry = tk.Entry(self.user_profile_frame)
        self.activity_level_entry.grid(row=5, column=1)

        self.work_schedule_label = tk.Label(self.user_profile_frame, text="Work Schedule:")
        self.work_schedule_label.grid(row=6, column=0, sticky="w")
        self.work_schedule_entry = tk.Entry(self.user_profile_frame)
        self.work_schedule_entry.grid(row=6, column=1)

        self.sleep_patterns_label = tk.Label(self.user_profile_frame, text="Sleep Patterns:")
        self.sleep_patterns_label.grid(row=7, column=0, sticky="w")
        self.sleep_patterns_entry = tk.Entry(self.user_profile_frame)
        self.sleep_patterns_entry.grid(row=7, column=1)

        self.dietary_preferences_label = tk.Label(self.user_profile_frame, text="Dietary Preferences:")
        self.dietary_preferences_label.grid(row=8, column=0, sticky="w")
        self.dietary_preferences_entry = tk.Entry(self.user_profile_frame)
        self.dietary_preferences_entry.grid(row=8, column=1)

        self.medical_history_label = tk.Label(self.user_profile_frame, text="Medical History:")
        self.medical_history_label.grid(row=9, column=0, sticky="w")
        self.medical_history_entry = tk.Entry(self.user_profile_frame)
        self.medical_history_entry.grid(row=9, column=1)

        self.budget_label = tk.Label(self.user_profile_frame, text="Budget:")
        self.budget_label.grid(row=10, column=0, sticky="w")
        self.budget_entry = tk.Entry(self.user_profile_frame)
        self.budget_entry.grid(row=10, column=1)

        # Create the save user profile button
        self.save_user_profile_button = tk.Button(self.user_profile_frame, text="Save User Profile", command=self.save_user_profile)
        self.save_user_profile_button.grid(row=11, column=0, columnspan=2, pady=10)

    def create_meal_logging_widgets(self):
        # Create a frame for the meal logging widgets
        self.meal_logging_frame = tk.LabelFrame(self.main_frame, text="Meal Logging")
        self.meal_logging_frame.pack(fill="x", padx=10, pady=10)

        # Create the meal logging buttons
        self.log_meal_from_image_button = tk.Button(self.meal_logging_frame, text="Log Meal from Image", command=self.log_meal_from_image)
        self.log_meal_from_image_button.pack(side="left", padx=10, pady=10)

        self.log_meal_from_voice_button = tk.Button(self.meal_logging_frame, text="Log Meal from Voice", command=self.log_meal_from_voice)
        self.log_meal_from_voice_button.pack(side="left", padx=10, pady=10)

        self.log_meal_from_barcode_button = tk.Button(self.meal_logging_frame, text="Log Meal from Barcode", command=self.log_meal_from_barcode)
        self.log_meal_from_barcode_button.pack(side="left", padx=10, pady=10)

    def create_diet_recommendation_widgets(self):
        # Create a frame for the diet recommendation widgets
        self.diet_recommendation_frame = tk.LabelFrame(self.main_frame, text="Diet Recommendation")
        self.diet_recommendation_frame.pack(fill="x", padx=10, pady=10)

        # Create the generate meal plan button
        self.generate_meal_plan_button = tk.Button(self.diet_recommendation_frame, text="Generate Meal Plan", command=self.generate_meal_plan)
        self.generate_meal_plan_button.pack(pady=10)

        # Create the meal plan text area
        self.meal_plan_text = tk.Text(self.diet_recommendation_frame, height=10, width=50)
        self.meal_plan_text.pack(padx=10, pady=10)

    def save_user_profile(self):
        age = int(self.age_entry.get())
        gender = self.gender_entry.get()
        height = int(self.height_entry.get())
        weight = int(self.weight_entry.get())
        health_goals = {"calorie_target": int(self.health_goals_entry.get())}
        activity_level = self.activity_level_entry.get()
        work_schedule = self.work_schedule_entry.get()
        sleep_patterns = self.sleep_patterns_entry.get()
        dietary_preferences = self.dietary_preferences_entry.get().split(",")
        medical_history = self.medical_history_entry.get().split(",")
        budget = int(self.budget_entry.get())

        self.user_profile = UserProfile(
            age,
            gender,
            height,
            weight,
            health_goals,
            activity_level,
            work_schedule,
            sleep_patterns,
            dietary_preferences,
            medical_history,
            budget
        )

        self.data_storage = DataStorage(f"{gender}_{age}")
        self.data_storage.save_user_profile(self.user_profile)

        self.diet_recommender = DietRecommender(self.user_profile)

    def log_meal_from_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            meal_log = self.meal_logger.log_meal_from_image(file_path)
            self.data_storage.save_meal_log(meal_log)

    def log_meal_from_voice(self):
        meal_log = self.meal_logger.log_meal_from_voice()
        self.data_storage.save_meal_log(meal_log)

    def log_meal_from_barcode(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            meal_log = self.meal_logger.log_meal_from_barcode(file_path)
            self.data_storage.save_meal_log(meal_log)

    def generate_meal_plan(self):
        if self.diet_recommender:
            meal_plan = self.diet_recommender.generate_meal_plan()
            self.meal_plan_text.delete("1.0", tk.END)
            for meal, food in meal_plan.items():
                self.meal_plan_text.insert(tk.END, f"{meal.capitalize()}: {food}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = DietPlannerGUI(root)
    root.mainloop()
