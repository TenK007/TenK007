import tkinter as tk

class DietPlannerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Diet Planner")

        # Create the main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        # Create the widgets
        self.create_widgets()

    def create_widgets(self):
        # In a real application, this would be a much more complex and
        # visually appealing GUI.
        # For now, we'll just create a few simple widgets.
        self.label = tk.Label(self.main_frame, text="Welcome to the AI Diet Planner!")
        self.label.pack()

        self.meal_plan_button = tk.Button(self.main_frame, text="View Meal Plan")
        self.meal_plan_button.pack()

        self.dashboard_button = tk.Button(self.main_frame, text="View Dashboard")
        self.dashboard_button.pack()

        self.grocery_list_button = tk.Button(self.main_frame, text="View Grocery List")
        self.grocery_list_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = DietPlannerGUI(root)
    root.mainloop()
