import numpy as np
import json

names_list =  np.load('final_list_names.npy', allow_pickle=True)

names_list = [item.tolist() if isinstance(item, np.ndarray) else item for item in names_list]


# Convert the list to a JSON-formatted string
json_data = json.dumps(names_list, indent=2)

# Write the JSON string to a file
with open("names.json", "w") as json_file:
    json_file.write(json_data)

print("JSON file created successfully: names.json")