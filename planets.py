planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")

planet_list.append("Saturn")

print(planet_list)

last_planets = ["Uranus", "Neptune"]

planet_list.extend(last_planets)

print(planet_list)

planet_list.insert(1, "Venus")

planet_list.insert(2, "Earth")

print(planet_list)

planet_list.append("Pluto")

print(planet_list)

rocky_planets = planet_list[:4]

print(rocky_planets)

# del planet_list[-1]

print(planet_list)

spacecraft = [
    ("Mariner 2", "Venus"),
    ("Mariner 4", "Mars"),
    ("Mariner 5", "Venus"),
    ("Mariner 6", "Mars"),
    ("Mariner 7", "Mars"),
    ("Mariner 9", "Mars"),
    ("Mariner 10", "Mercury", "Venus"),
    ("MESSENGER", "Mercury", "Venus"),
    ("Venera 1", "Venus"),
    ("Venera 2", "Venus"),
    ("Venera 3", "Venus"),
    ("Venera 4", "Venus"),
    ("Venera 5", "Venus"),
    ("Venera 6", "Venus"),
    ("Venera 7", "Venus"),
    ("Venera 8", "Venus"),
    ("Venera 9", "Venus"),
    ("Venera 10", "Venus"),
    ("Venera 11", "Venus"),
    ("Venera 12", "Venus"),
    ("Venera 13", "Venus"),
    ("Venera 14", "Venus"),
    ("Venera 15", "Venus"),
    ("Venera 16", "Venus"),
    ("Pioneer Venus 1", "Venus"),
    ("Pioneer Venus 2", "Venus"),
    ("Vega 1", "Venus"),
    ("Vega 2", "Venus"),
    ("Galileo", "Venus", "Jupiter"),
    ("Magellan", "Venus"),
    ("Cassini", "Venus", "Jupiter", "Saturn"),
    ("Venus Express", "Venus"),
    ("Parker Solar Probe", "Venus"),
    ("Viking 1", "Mars"),
    ("Viking 2", "Mars"),
    ("Mars Pathfinder", "Mars"),
    ("Mars Odyssey", "Mars"),
    ("Spirit", "Mars"),
    ("Opportunity", "Mars"),
    ("Phoenix", "Mars"),
    ("Dawn", "Mars"),
    ("Curiosity", "Mars"),
    ("Insight", "Mars"),
    ("Perseverance", "Mars"),
    ("Pioneer 10", "Jupiter"),
    ("Pioneer 11", "Jupiter", "Saturn"),
    ("Voyager 1", "Jupiter", "Saturn"),
    ("Voyager 2", "Jupiter", "Saturn", "Uranus", "Neptune"),
    ("New Horizons", "Jupiter", "Pluto"),
    ("Juno", "Jupiter")

]

planet_visits = {planet: [] for planet in planet_list}

for craft in spacecraft:
    name = craft[0]
    visited_planets = craft[1:]
    for planet in visited_planets:
        if planet in planet_visits:
            planet_visits[planet].append(name)

for planet, crafts in planet_visits.items():
    if crafts:
        print(f"{planet} has been visited by")
        print("---------------------------")
        for craft in crafts:
            print(craft)
            print()