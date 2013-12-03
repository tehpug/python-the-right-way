from operator import attrgetter, itemgetter
from pelican import signals

def sort_py(generator):
    generator.articles.sort(key=attrgetter('slug'))

def register():
    signals.article_generator_finalized.connect(sort_py)
