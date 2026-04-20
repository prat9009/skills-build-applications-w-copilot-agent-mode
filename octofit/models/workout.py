class Workout:
    def __init__(self, name, duration, calories_burned):
        self.name = name
        self.duration = duration  # duration in minutes
        self.calories_burned = calories_burned

    def get_summary(self):
        return f"Workout: {self.name}, Duration: {self.duration} min, Calories Burned: {self.calories_burned}"