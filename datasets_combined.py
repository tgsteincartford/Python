# weather lookup dictionary
weather_dict = {item['city']: item for item in weather_data}

#merge the data
merged_data = []
for city in cities_data:
    city_name = ["city"]
    if city_name in weather_dict:
        merged_item = {
            'City': city_name,
            'Population': city['population'],
            'Region': city['region'],
            'Temperature': weather_dict[city_name]['temperature'],
            'Humidity': weather_dict[city_name]['humidity']
        }
        merged_data.append(merged_item)

#print first record to check it
print("First merged record:", merged_data[0])

