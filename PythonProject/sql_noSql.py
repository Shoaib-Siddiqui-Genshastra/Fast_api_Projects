import pandas as pd
import json
# Create the DataFrame
data = pd.DataFrame({
    'User_ID': [1, 2, 3, 4],
    'Likes': [23, 45, 12, 37],
    'Shares': [5, 3, 8, 2],
    'Comments': [12, 34, 9, 21],
    'Clicks': [120, 300, 150, 90],
    'Engagement_with_Ads': [0.4, 0.6, 0.2, 0.5],
    'Time_Spent_on_Platform': [30, 45, 25, 40],
    'Purchase_History': [0, 1, 0, 1],
    'Engagement_Level': ['High', 'Medium', 'Low', 'Medium'],
    'Purchase_Like': [0, 1, 1, 1]
})

# View the DataFrame
print(data)

# Convert the DataFrame to JSON
json_data = data.to_json(orient='records', indent=4)

# View the JSON data
print(json_data)

# Save JSON data to a file
with open('data.json', 'w') as file:
    file.write(json_data)

