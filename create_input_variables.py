import json

input_variables = {
    "Ctt": 16,
    "Ce": 0.12,
    "Cf": 4,
    "r": 15**2,
    "Cm": 25,
    "ef_truck": 0.48,
    "ef_EV": 0.7,
    "frontal_surface": 5,
    "vehicle_curb_w": 3629,
    "vehicle_capacity": 9073
}

# Specify the file path where you want to save the JSON file
file_path = "./EVRP to LP/config.json"

# Write the input variables to the JSON file
with open(file_path, "w") as json_file:
    json.dump(input_variables, json_file, indent=4)

print(f"Input variables have been written to {file_path}")


