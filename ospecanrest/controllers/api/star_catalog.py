import pecan
from pecan import rest, response
from wsmeext.pecan import wsexpose
from ospecanrest.model import star

# Temporary solution. In the future will be add database and sqlalchemy
stars = [star.Star("Aldebaran", 0), star.Star("Sun", 0)]


class StarCatalogController(rest.RestController):

    @wsexpose([star.Star])
    def get(self):
        return stars

    @wsexpose(star.Star, int)
    def get(self, objectId):
        return star.Star("Aldebaran", 12)

    @pecan.expose()
    def post(self):
        response.status = 200
        return

    @pecan.expose(bool, star.Star)
    def put(self, new_star):
        stars.append(new_star)
        response.status = 200
        return

    @pecan.expose(bool, int)
    def delete(self):
        response.status = 200
        return

    @pecan.expose()
    def patch(self):
        response.status = 201
        return
