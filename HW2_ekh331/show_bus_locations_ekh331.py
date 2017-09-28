#!/usr/bin/env python

import argparse
import urllib2
import json


def do_thing(mta_key, bus_line):
    response = query_api(mta_key, bus_line)
    vehicle_activities = response['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']    

    print "Bus Line : %s" % (bus_line)
    print "Number of Active Buses : %s" % (len(vehicle_activities))
    for i, vehicle_activity in enumerate(vehicle_activities):
        lat = vehicle_activity['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
        lon = vehicle_activity['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
        print "Bus %s is at latitude %s and longitude %s" % (i + 1, lat, lon)

###################################


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
    do_thing(args.MTA_KEY, args.BUS_LINE)

def parser():
    p = argparse.ArgumentParser()
    p.add_argument("MTA_KEY")
    p.add_argument("BUS_LINE")
    return p   

if __name__ == "__main__":
    main()

