from geopy.distance import geodesic

# Device's current location
device_location = (21.4276496, 91.9979506)  # Replace with actual latitude and longitude

# Sample data with latitudes and longitudes
data = [
    {"name": "Location1", "lat": 21.42587910778771, "long": 91.99624124253678},
    {"name": "Location2", "lat": 21.413700627146227, "long": 92.00809923004863},
    {"name": "Location3", "lat": 21.50300982638072, "long": 92.06185728960365},
    {"name": "Location4", "lat": 21.456067312022716, "long": 91.92739867258632},
    # Add more data points as needed
]

# Radius in kilometers
radius_km = 5


# Function to filter locations within the radius
def filter_locations_within_radius(device_location, data, radius_km):
    filtered_data = []
    for location in data:
        location_point = (location['lat'], location['long'])
        distance = geodesic(device_location, location_point).kilometers
        if distance <= radius_km:
            filtered_data.append(location)
    return filtered_data


# Get locations within the 5 km radius
filtered_locations = filter_locations_within_radius(device_location, data, radius_km)

# Print the filtered locations
print(filtered_locations)
