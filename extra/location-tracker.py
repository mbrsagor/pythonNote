from ip2geotools.databases.noncommercial import DbIpCity


def location_tracker(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"IP Address: {res.ip_address}")
    print(f"Location: {res.city}, {res.region}, {res.country}")
    print(f"Coordinates: (Lat: {res.latitude}, Lng: {res.longitude})")


ip_add = input("Enter IP: ")
location_tracker(ip_add)
