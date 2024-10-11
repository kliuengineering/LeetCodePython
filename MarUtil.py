# Define a function to calculate production output with diminishing returns
def production_output(x):
    initial_output = 100  # Assume the initial production output is 100 units
    gain_factor = 1.1     # 10% gain for every 22-point increase
    return initial_output * (gain_factor ** (x // 22))

# Function to calculate the rate of diminishing return between two points
def diminishing_return(x1, x2):
    output1 = production_output(x1)
    output2 = production_output(x2)
    return (output2 - output1) / (x2 - x1)

# Compute the diminishing return from 0 to 22
x1_interval_1 = 0
x2_interval_1 = 22
dr_interval_1 = diminishing_return(x1_interval_1, x2_interval_1)

# Compute the diminishing return from 198 to 220
x1_interval_2 = 176
x2_interval_2 = 198
dr_interval_2 = diminishing_return(x1_interval_2, x2_interval_2)

# Display the results
# print(f"Diminishing Return from 0 to 22: {dr_interval_1}")
print(f"Diminishing Return from {x1_interval_2} to {x2_interval_2}: {dr_interval_2}")


