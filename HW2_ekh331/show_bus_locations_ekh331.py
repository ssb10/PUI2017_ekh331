#!/usr/bin/env python

import argparse
import urllib2
import json


def show_bus_locations(mta_key, bus_line):
    vehicle_activities = get_vehicle_activities(mta_key, bus_line)

    print "Bus Line : %s" % (bus_line)
    print "Number of Active Buses : %s" % (len(vehicle_activities))
    for i, vehicle_activity in enumerate(vehicle_activities):
        location = vehicle_activity['MonitoredVehicleJourney']['VehicleLocation']
        lat, lon = location['Latitude'], location['Longitude']
        print "Bus %s is at latitude %s and longitude %s" % (i + 1, lat, lon)

###################################

def get_vehicle_activities(mta_key, bus_line):
    response = query_api(mta_key, bus_line)
    return response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

def query_api(mta_key, bus_line):
    """ Returns a dictionary """
    url_format = "".join(
                 ["http://bustime.mta.info/api/siri/",
                  "vehicle-monitoring.json?key={0}",
                  "&VehicleMonitoringDetailLevel=calls",
                  "&LineRef={1}"
                 ])

    url = url_format.format(mta_key, bus_line)
    f = urllib2.urlopen(url)
    response = json.loads(f.read())
    return response
 

#################################################
def main():
    args = parser().parse_args()
    show_bus_locations(args.mta_key, args.bus_line)

def parser():
    p = argparse.ArgumentParser()
    p.add_argument("mta_key")
    p.add_argument("bus_line")
    return p   

if __name__ == "__main__":
    main()

