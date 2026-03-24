# average weekly temperature 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 
temperatures = [] 
for day in days: 
    temp = float(input(f"Enter temperature for {day} (in °C): ")) 
    temperatures.append(temp) 
average_temp = sum(temperatures) / len(temperatures) 

print(f"\nTemperatures for the week:") 
for day, temp in zip(days, temperatures): 
    print(f"{day}: {temp}°C") 

print(f"\nThe average temperature this week is: {average_temp:.2f}°C")
