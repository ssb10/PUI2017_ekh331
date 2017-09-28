#!/usr/bin/env/python

import argparse
import urllib2
import json
import csv

from show_bus_locations_ekh331 import get_vehicle_activities

def get_bus_info(mta_key, bus_line, output_path):
    vehicle_activities = get_vehicle_activities(mta_key, bus_line)

    with open(output_path, 'wb') as f:
        header = "Latitude,Longitude,Stop Name,Stop Status\n"
        f.write(header)

        for vehicle_activity in vehicle_activities:
            location = vehicle_activity['MonitoredVehicleJourney']['VehicleLocation']
            lat, lon = location['Latitude'], location['Longitude']
        
            onward_call_info = vehicle_activity['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
    
            try:
                stop_name = onward_call_info['StopPointName']
            except KeyError:
                stop_name = "N/A"

            try:
                stop_status = onward_call_info['Extensions']['Distances']['PresentableDistance']
            except KeyError:
                stop_status = "N/A"

            f.write("%s,%s,%s,%s\n" % (lat, lon, stop_name, stop_status))


def main():
    args = parser().parse_args()
    get_bus_info(args.mta_key, args.bus_line, args.output_path)

def parser():
    p = argparse.ArgumentParser()
    p.add_argument("mta_key")
    p.add_argument("bus_line")
    p.add_argument("output_path")

    return p


if __name__ == "__main__":
    main()
