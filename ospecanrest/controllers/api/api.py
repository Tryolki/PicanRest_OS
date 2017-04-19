from ospecanrest.controllers.api import star_catalog


class ApiController(object):

    def __init__(self, stars):
        self.stars = star_catalog.StarCatalogController(stars)
