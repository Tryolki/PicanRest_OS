import pecan
from pecan import rest, response
from ospecanrest.model import star

# Temporary solution. In the future will be add database and sqlalchemy
stars = {1: star.Star("Aldebaran", 0),
         2: star.Star("Sun", 0)}


class StarCatalogController(rest.RestController):
    key_index = 2

    @pecan.expose('json', content_type='application/json')
    def get(self, object_id):
        try:
            response.status = 200
            return stars[int(object_id)]
        except (IndexError, ValueError, KeyError) as ex:
            response.status = 404
            return

    @pecan.expose()
    def post(self):
        name = pecan.request.POST.get('name')
        weight = pecan.request.POST.get('weight')
        self.key_index += 1
        stars[self.key_index] = star.Star(name, weight)
        response.status = 200
        return

    @pecan.expose()
    def put(self, object_id):
        try:
            name = pecan.request.POST.get('name')
            weight = pecan.request.POST.get('weight')
            stars[int(object_id)] = star.Star(name, weight)
            response.status = 200
            return
        except (IndexError, ValueError, KeyError) as ex:
            response.status = 404
            return

    @pecan.expose()
    def delete(self, object_id):
        try:
            response.status = 200
            print(object_id)
            stars.pop(int(object_id))
            return
        except KeyError as ex:
            response.status = 404
            return
