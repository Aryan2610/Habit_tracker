from datetime import datetime
from habit import break_habit
import pandas as pd 
from tabulate import tabulate

habits = []
n = int(input("Enter number of habits you want to track: "))
m = int(input("Enter your monthly wage: "))
for i in range(n):
    habit = input(f"Enter name of habit {i+1}: ")
    year = int(input("Enter year of quitting habit: "))
    month = int(input("Enter month of quitting habit: "))
    day = int(input("Enter day of quitting habit: "))
    g = int(input("Enter number of days in which you want to quit the habit: "))
    cost = int(input("Enter the approximate cost of the habit per day: "))
    minutes = int(input("Enter the approximate time wasted in minutes on the habit per day: "))
    habits.append(break_habit(habit,datetime(year,month,day),cost,m,minutes,g))

df = pd.DataFrame(habits)

print(tabulate(df,headers='keys',tablefmt='psql'))