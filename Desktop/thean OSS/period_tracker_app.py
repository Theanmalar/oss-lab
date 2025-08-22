import json
import os
from datetime import datetime, timedelta
from tkinter import *
from tkinter import messagebox
from plyer import notification

DATA_FILE = "cycle_data.json"

# ======= Core Functions =======

def get_phase_meal(day, cycle_length):
    phase_day = day % cycle_length
    if 0 <= phase_day <= 5:
        return "🩸 Menstrual Phase", [
            "Spinach, beans, red meat",
            "Warm soup, dates, iron-rich foods"
        ]
    elif 6 <= phase_day <= 13:
        return "🌱 Follicular Phase", [
            "Eggs, oats, fresh fruits",
            "Avocados, nuts, yogurt"
        ]
    elif 14 <= phase_day <= 16:
        return "🌸 Ovulation Phase", [
            "Pumpkin seeds, bananas",
            "Berries, lots of water"
        ]
    elif 17 <= phase_day <= cycle_length - 1:
        return "🌙 Luteal Phase", [
            "Sweet potatoes, dark chocolate",
            "Chicken, whole grains"
        ]
    else:
        return "Unknown", []

def save_data(start_date, cycle_length):
    with open(DATA_FILE, 'w') as f:
        json.dump({
            "start_date": start_date,
            "cycle_length": cycle_length
        }, f)

def load_data():
    if not os.path.exists(DATA_FILE):
        return None
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def export_meal_plan(filename, day, cycle_length):
    phase, meals = get_phase_meal(day, cycle_length)
    with open(filename, "w") as f:
        f.write(f"Day {day % cycle_length} of your cycle\n")
        f.write(f"Phase: {phase}\n\nMeals:\n")
        for meal in meals:
            f.write(f"- {meal}\n")

def send_notification():
    data = load_data()
    if not data:
        return
    start = datetime.strptime(data["start_date"], "%Y-%m-%d")
    days = (datetime.today() - start).days
    phase, meals = get_phase_meal(days, data["cycle_length"])
    meal_str = "\n- ".join(meals)
    notification.notify(
        title="🩺 Period Tracker Reminder",
        message=f"Day {days % data['cycle_length']} - {phase}\n- {meal_str}",
        timeout=10
    )

# ======= GUI Setup =======

def setup_gui():
    window = Tk()
    window.title("🩸 Period Tracker")
    window.geometry("450x400")
    window.config(bg="#fce4ec")

    # ----- Labels & Inputs -----
    Label(window, text="Last Period Start Date (YYYY-MM-DD):", bg="#fce4ec").pack()
    entry_date = Entry(window)
    entry_date.pack()

    Label(window, text="Average Cycle Length (in days):", bg="#fce4ec").pack()
    entry_cycle = Entry(window)
    entry_cycle.pack()

    # ----- Handlers -----
    def save_user_data():
        try:
            start_date = entry_date.get()
            cycle_length = int(entry_cycle.get())
            datetime.strptime(start_date, "%Y-%m-%d")
            save_data(start_date, cycle_length)
            messagebox.showinfo("Saved", "User data saved successfully!")
        except:
            messagebox.showerror("Error", "Please enter a valid date and number.")

    def show_today_info():
        data = load_data()
        if not data:
            messagebox.showerror("No Data", "Please save your cycle data first.")
            return
        start = datetime.strptime(data["start_date"], "%Y-%m-%d")
        today = datetime.today()
        days_passed = (today - start).days
        phase, meals = get_phase_meal(days_passed, data["cycle_length"])
        info = f"📅 Day {days_passed % data['cycle_length']} of your cycle\n\nPhase: {phase}\n\nMeals:\n"
        info += "\n".join(f"- {meal}" for meal in meals)
        messagebox.showinfo("Today's Suggestion", info)

    def export_plan():
        data = load_data()
        if not data:
            messagebox.showerror("No Data", "Please save your cycle data first.")
            return
        start = datetime.strptime(data["start_date"], "%Y-%m-%d")
        days = (datetime.today() - start).days
        filename = "today_meal_plan.txt"
        export_meal_plan(filename, days, data["cycle_length"])
        messagebox.showinfo("Exported", f"Today's meal plan saved to {filename}")

    # ----- Buttons -----
    Button(window, text="💾 Save Data", command=save_user_data).pack(pady=5)
    Button(window, text="📋 Show Today's Meals", command=show_today_info).pack(pady=5)
    Button(window, text="📁 Export Meal Plan", command=export_plan).pack(pady=5)
    Button(window, text="🔔 Test Daily Reminder", command=send_notification).pack(pady=5)

    window.mainloop()

# ======= Run the App =======
if __name__ == "__main__":
    setup_gui()
