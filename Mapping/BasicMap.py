from collections import defaultdict

emitter = lambda word: (word, 1)
counter = lambda (word, emissions): (work, sum(emissions))


def map_reduce_naive(my_input, mapper, reducer):
    map_results = map(mapper, my_input)

    shuffler = defaultdict