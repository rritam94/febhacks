import googlemaps

#initialize api stuff and vars
gmaps = googlemaps.Client(key='AIzaSyA9Ii6BVbrVyZB0Pv0ri0QW4pXFGrE7kM0')
geocode_result = gmaps.geocode('Gainesville, Florida')
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']

def main():
    print(search('cardiologist'))

def search(specialization: str) -> list:
    doctors = []
    places_result = gmaps.places_nearby(location=(lat, lng), radius=5000,keyword=specialization, type='doctor')
    
    for result in places_result['results']:
        if(result['name'][0] == 'D'):
            doctors.append(result['name'])

    return doctors


if __name__ == '__main__':
    main()
