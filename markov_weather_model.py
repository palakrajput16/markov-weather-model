import random
import matplotlib.pyplot as plt

states = ['S', 'C', 'R']
matrix_weather = {
    'S': [0.6, 0.3, 0.1],
    'C': [0.4, 0.3, 0.3],
    'R': [0.2, 0.1, 0.7]
}

current_state = 'S'
time_step = 1000  # days

weather_sequence = current_state
count = {'S': 0, 'C': 0, 'R': 0}

# Lists to store cumulative counts over time
sunny_counts = []
cloudy_counts = []
rainy_counts = []

# Initialize counts
sunny = cloudy = rainy = 0

for day in range(time_step):
    if current_state == 'S':
        sunny += 1
    elif current_state == 'C':
        cloudy += 1
    else:  # 'R'
        rainy += 1

    sunny_counts.append(sunny)
    cloudy_counts.append(cloudy)
    rainy_counts.append(rainy)

    probs = matrix_weather[current_state]
    next_state = random.choices(states, weights=probs)[0]
    weather_sequence += next_state
    current_state = next_state

# Final stats print
print("Full Predicted Weather Sequence:")
print(weather_sequence)

print("\nWeather Counts and Fractions After 1000 Days:")
print(f"S : {sunny} days : {sunny / time_step:.4f}")
print(f"C : {cloudy} days : {cloudy / time_step:.4f}")
print(f"R : {rainy} days : {rainy / time_step:.4f}")

# Plotting the cumulative weather counts
plt.figure(figsize=(14, 6))
plt.plot(sunny_counts, label='Sunny (S)', color='orange')
plt.plot(cloudy_counts, label='Cloudy (C)', color='gray')
plt.plot(rainy_counts, label='Rainy (R)', color='blue')
plt.xlabel('Day')
plt.ylabel('Cumulative Count')
plt.title('Cumulative Weather Count Over 1000 Days')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
