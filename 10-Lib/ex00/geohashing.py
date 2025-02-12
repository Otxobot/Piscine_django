import sys
import antigravity

def main():
    n = len(sys.argv)
    if n != 4:
        print("Wrong number of arguments")
        print("Usage: python3 geohashing.py <latitude> <longitude> <datedow>")
        sys.exit(1)

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = sys.argv[3]

        if not (-90 <= latitude <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees")
        if not (-180 <= longitude <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees")

        antigravity.geohash(latitude, longitude, datedow.encode())

    except ValueError as e:
        print(e)
        sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()