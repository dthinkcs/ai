import csv
import sys

from util import Node, StackFrontier, QueueFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}

# graph[actor0] -> [(actor1, filmv) ,  , ]
graph = {}

simple_graph = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} and {person2} starred in {movie}")


# Name: Emma Watson
# Name: Jennifer Lawrence
# 3 degrees of separation.
# 1: Emma Watson and Matthew Broderick starred in The Tale of Despereaux
# 2: Matthew Broderick and Michelle Pfeiffer starred in Ladyhawke
# 3: Michelle Pfeiffer and Jennifer Lawrence starred in Mother!

# Name: Emma Watson      
# Name: Jennifer Lawrence
# 3 degrees of separation.
# 1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
# 2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
# 3: Michael Fassbender and Jennifer Lawrence starred in X-Men: Apocalypse
def load_graph():
    for person in people:
        graph[person] = [] # HOW THE HELL ARE WE GETTING DIFFERENT RESULTS WITH A LIST
        for movie in people[person]['movies']: #was BUGGY
            for star in movies[movie]['stars']:
                if star != person: # was BUGGY
                    graph[person].append( (star, movie) )

# def load_simple_graph():
#     for person in people:
#         simple_graph[person] = set()
#         for movie in people[person]['movies']: #was BUGGY
#             for star in movies[movie]['stars']:
#                 if star != person: # was BUGGY
#                     simple_graph[person].add(star)


def shortest_path(source, target):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """
    

    load_graph()
    #load_simple_graph()

    visited = set()
    q = [source]
    parent = {source: None}
    visited.add(source)

    # bfs simpel graph
    q = [source]
    parent = {source: (None, None)}
    visited = set()
    visited.add(source)
    found = False
    while len(q) != 0:
        front = q.pop(0)
        
        for neighbour in graph[front]:
            if neighbour[0] not in visited:
                visited.add(neighbour[0])
                q.append(neighbour[0])
                parent[neighbour[0]] = (front, neighbour[1])
            if neighbour[0] == target:
                found = True
                break
    #print(found)
    path = []
    if found:
        curr = target
        #print(parent)
        while parent[curr] != (None, None):
            #print(curr, parent[curr])
            path.append((parent[curr][1], curr))
            curr = parent[curr][0]

        path.reverse()
    #print(path)
    return path





    #raise NotImplementedError


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
    #load_data("small")
    #shortest_path('102', '420')
    #load_graph()
    #load_simple_graph()
    
    #print(names) # names['kevin bacon'] -> {'102'}
    #print(movies) # movies['112384'] -> {'title': --- , 'year': ---, 'stars': {}}
    #print(people) #people['102'] -> {name: 'Kevin Bacon', movies{'104257', '112384'}}
    #print(simple_graph)
    #print(graph) # {'102': [('197', '104257'), ('129', '104257'), ('193', '104257'), ('641', '112384'), ('200', '112384'), ('158', '112384')], '129': [('197', '104257'), ('193', '104257'), ('102', '104257'), ('420', '95953'), ('163', '95953'), ('596520', '95953')], '144': [('705', '93779'), ('1597', '93779'), ('1697', '93779')], '158': [('705', '109830'), ('641', '109830'), ('398', '109830'), ('641', '112384'), ('200', '112384'), ('102', '112384')], '1597': [('705', '93779'), ('1697', '93779'), ('144', '93779')], '163': [('129', '95953'), ('420', '95953'), ('596520', '95953')], '1697': [('705', '93779'), ('1597', '93779'), ('144', '93779')], '193': [('197', '104257'), ('129', '104257'), ('102', '104257')], '197': [('129', '104257'), ('193', '104257'), ('102', '104257')], '200': [('641', '112384'), ('102', '112384'), ('158', '112384')], '398': [('705', '109830'), ('641', '109830'), ('158', '109830')], '420': [('129', '95953'), ('163', '95953'), ('596520', '95953')], '596520': [('129', '95953'), ('420', '95953'), ('163', '95953')], '641': [('705', '109830'), ('398', '109830'), ('158', '109830'), ('200', '112384'), ('102', '112384'), ('158', '112384')], '705': [('1597', '93779'), ('1697', '93779'), ('144', '93779'), ('641', '109830'), ('398', '109830'), ('158', '109830')], '914612': []}