import pecan
from pecan import rest, response, abort
from ospecanrest.model import star


class StarCatalogController(rest.RestController):
    key_index = 2
    # Temporary solution. In the future will be add database and sqlalchemy
    stars = {1: star.Star("Aldebaran", 0),
             2: star.Star("Sun", 0)}

    @pecan.expose('json', content_type='application/json')
    def get(self):
        try:
            response.status = 200
            return self.stars[1]
        except (IndexError, ValueError, KeyError) as ex:
            abort(404)

    @pecan.expose('json', content_type='application/json')
    def get(self, object_id):
        try:
            response.status = 200
            return self.stars[int(object_id)]
        except (IndexError, ValueError, KeyError) as ex:
            abort(404)

    @pecan.expose('json', content_type='application/json')
    def post(self):
        name = pecan.request.POST.get('name')
        weight = pecan.request.POST.get('weight')
        self.key_index += 1
        self.stars[self.key_index] = star.Star(name, weight)
        response.status = 200
        return self.stars[self.key_index]

    @pecan.expose('json', content_type='application/json')
    def put(self, object_id):
        try:
            self.stars[int(object_id)].name = pecan.request.POST.get('name')
            self.stars[int(object_id)].weight = pecan.request.POST.get('weight')
            response.status = 200
            return self.stars[int(object_id)]
        except (IndexError, ValueError, KeyError) as ex:
            abort(404)

    @pecan.expose()
    def delete(self, object_id):
        try:
            response.status = 200
            self.stars.pop(int(object_id))
            return
        except KeyError as ex:
            abort(404)
