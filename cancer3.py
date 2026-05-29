# dict
India_Stats = {
    "Mumbai": {"Avg_Temperature": 30, "AQI": 95},
    "Delhi": {"Avg_Temperature": 33, "AQI": 180},
    "Bengaluru": {"Avg_Temperature": 24, "AQI": 65},
    "Hyderabad": {"Avg_Temperature": 32, "AQI": 110},
    "Chennai": {"Avg_Temperature": 31, "AQI": 85},
    "Kolkata": {"Avg_Temperature": 29, "AQI": 135},
    "Ahmedabad": {"Avg_Temperature": 34, "AQI": 140},
    "Pune": {"Avg_Temperature": 27, "AQI": 90},
    "Jaipur": {"Avg_Temperature": 33, "AQI": 120},
    "Lucknow": {"Avg_Temperature": 31, "AQI": 130}
}
# city search
search_city = input("Enter the name of the city to retrieve details: ").title()
if search_city in India_Stats:
    # output
    stats = India_Stats[search_city]
    print(f"Statistics for {search_city} are:")
    print(f"Average Temperature: {stats['Avg_Temperature']}degree Celsius")
    print(f"Pollution Index (AQI): {stats['AQI']}")
else:
    print(f"Data for '{search_city}' is not available.")