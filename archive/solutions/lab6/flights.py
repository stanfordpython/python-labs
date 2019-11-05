import argparse
import collections
import csv

# For the meaning of these identifiers, read https://openflights.org/data.html
Airport = collections.namedtuple('Airport', ['id', 'name', 'city', 'country', 'faa_iata', 'icao', 'lat', 'long', 'alt', 'utc_offset', 'dst', 'tz', 'type', 'source'])
Airline = collections.namedtuple('Airline', ['id', 'name', 'alias', 'iata', 'icao', 'callsign', 'country', 'active'])
Route = collections.namedtuple('Route', ['airline', 'airline_id', 'source_airport', 'source_airport_id', 'dest_airport', 'dest_airport_id', 'codeshare', 'stops', 'equipment'])

def load_data():
    with open('airports.dat') as f:
        airports = {}
        for line in csv.reader(f):
            airport = Airport._make(line)
            airports[airport.id] = airport

    with open('airlines.dat') as f:
        airlines = {}
        for line in csv.reader(f):
            airline = Airline._make(line)
            airlines[airline.id] = airline

    with open('routes.dat') as f:
        # top-level keyed by source airport ID, next level keyed by destination airport ID
        routes = collections.defaultdict(lambda: collections.defaultdict(list))
        for line in csv.reader(f):
            route = Route._make(line)
            routes[route.source_airport][route.dest_airport].append(route)

    return airports, airlines, routes

# def get_adjacent_airports(routes, airport):
#     return itertools.chain(*(.values() for x in d.values()))

def find_flights(routes, source_airport, destination_airport, max_segments):
    # We implement a basic BFS algorithm for following the routes
    # Taken from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
    queue = [(source_airport, [source_airport])]
    while queue:
        airport, path = queue.pop(0)
        if len(path) > max_segments:
            return
        for next_airport in set(routes[airport].keys()) - set(path):
            if next_airport == destination_airport:
                yield path + [next_airport]
            else:
                queue.append((next_airport, path + [next_airport]))

def build_parser():
    parser = argparse.ArgumentParser(description='Find flights.')
    parser.add_argument('source', help='source airport (e.g. SFO)')
    parser.add_argument('destination', help='destination airport (e.g. JFK)')
    parser.add_argument('segments', type=int, help='maximum number of segments')
    return parser

if __name__ == '__main__':
    import sys
    parser = build_parser()
    args = parser.parse_args(sys.argv[1:])

    _airports, _airlines, routes = load_data()
    for flight in find_flights(routes, args.source, args.destination, args.segments):
        print(' -> '.join(flight))

