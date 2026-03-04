#!/usr/bin/env python3

import sys
import antigravity


def main():
    # Check number of parameters
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py <latitude> <longitude> <YYYY-MM-DD-DOW>")
        sys.exit(1)

    # Parse parameters
    try:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
    except ValueError:
        print("Error: latitude and longitude must be numbers.")
        sys.exit(1)

    datedow = sys.argv[3]

    try:
        # Encode string to bytes for Python 3.12+
        antigravity.geohash(lat, lon, datedow.encode())
    except Exception as e:
        print(f"Error: could not compute geohash ({e})")
        sys.exit(1)


if __name__ == "__main__":
    main()