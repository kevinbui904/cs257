AUTHORS: Kevin Bui, Robbie Young

DATA: Information on current movies and TV shows on Disney+

FEATURES CURRENTLY WORKING:
- ('/') base endpoint, returns website url
- ('/help') help endpoint, returns this readme.txt file
- ('/recommended?[genre=genre_name]') A random recommendation of a movie or show, recommendation is based on a specific genre (Action, Comedy, Documentary, and Mystery are currently supported)
- ('/directors/<directors_name>') Search of content directed by a given director
- ('/titles/<titles_string>') Search of content which contain a given string in its title
- ('/cast/<cast_name>') Search of content containing a given cast member