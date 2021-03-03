''' Make a function that takes in a list of movie times and the length
of a flight and returns movies that can be watched within the flight time.'''


#first impulse

def flight_movies(movies_in_mins, flight_time):
    current_best_time = None
    current_best_movies = []
    curent = None
    for i in range(len(movies_in_mins)-1):
        current = flight_time - movies_in_mins[i] + movies_in_mins[i+1]
        if current_best_time is None or current_best_time > current:
            current_best_time = current
            current_best_movies.append(movies_in_mins[i])
            current_best_movies.append(movies_in_mins[i+1])
    return current_best_movies

