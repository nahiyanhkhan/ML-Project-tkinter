import tkinter as tk
from tkinter import ttk
import pickle
import pandas as pd

# Load the pickled model
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Define teams and cities
teams = sorted(['Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 'England', 'West Indies',
                'Afghanistan', 'Pakistan', 'Sri Lanka'])

cities = sorted(['Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 'London', 'Pallekele',
                 'Barbados', 'Sydney', 'Melbourne', 'Durban', 'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton',
                 'Centurion', 'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 'Mount Maunganui',
                 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore',
                 'St Kitts', 'Cardiff', 'Christchurch', 'Trinidad'])

# Create Tkinter window
root = tk.Tk()
root.title('Cricket Score Predictor')


# Function to predict score
def predict_score():
    overs_value = int(overs.get())  # Convert overs value to integer
    balls_left = 120 - (overs_value * 6)  # Calculate balls left
    wickets_left = 10 - int(wickets.get())  # Convert wickets value to integer
    crr = int(current_score.get()) / overs_value  # Convert current score value to integer and calculate CRR

    input_df = pd.DataFrame({'batting_team': [batting_team.get()], 'bowling_team': [bowling_team.get()],
                             'city': [city.get()], 'current_score': [int(current_score.get())],
                             'balls_left': [balls_left], 'wickets_left': [int(wickets.get())], 'crr': [crr],
                             'last_five': [int(last_five.get())]})
    result = pipe.predict(input_df)
    predicted_score_label.config(text="Predicted Score: " + str(int(result[0])))


# Create widgets
batting_team_label = ttk.Label(root, text="Select batting team:")
batting_team = ttk.Combobox(root, values=teams, state="readonly")

bowling_team_label = ttk.Label(root, text="Select bowling team:")
bowling_team = ttk.Combobox(root, values=teams, state="readonly")

city_label = ttk.Label(root, text="Select city:")
city = ttk.Combobox(root, values=cities, state="readonly")

overs_label = ttk.Label(root, text="Overs done(works for over>5):")
overs = ttk.Spinbox(root, from_=0, to=50)

current_score_label = ttk.Label(root, text="Current Score:")
current_score = ttk.Entry(root)

wickets_label = ttk.Label(root, text="Wickets out:")
wickets = ttk.Spinbox(root, from_=0, to=10)

last_five_label = ttk.Label(root, text="Runs scored in last 5 overs:")
last_five = ttk.Entry(root)

predict_button = ttk.Button(root, text="Predict Score", command=predict_score)
predicted_score_label = ttk.Label(root, text="")

# Grid layout
batting_team_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
batting_team.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

bowling_team_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
bowling_team.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

city_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
city.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

overs_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
overs.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

current_score_label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
current_score.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

wickets_label.grid(row=5, column=0, padx=5, pady=5, sticky=tk.W)
wickets.grid(row=5, column=1, padx=5, pady=5, sticky=tk.W)

last_five_label.grid(row=6, column=0, padx=5, pady=5, sticky=tk.W)
last_five.grid(row=6, column=1, padx=5, pady=5, sticky=tk.W)

predict_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)
predicted_score_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Start Tkinter event loop
root.mainloop()
