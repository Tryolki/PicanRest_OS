from ospecanrest.controllers.api import star_catalog
from pecan import rest


class ApiController(rest.RestController):

    stars = star_catalog.StarCatalogController()
