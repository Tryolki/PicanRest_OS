from pecan import expose
from webob.exc import status_map
from ospecanrest.controllers.api import api
from ospecanrest.model import star


class RootController(object):
    # Temporary solution. In the future will be add database and sqlalchemy
    stars = {1: star.Star("Aldebaran", 0),
             2: star.Star("Sun", 0)}

    api = api.ApiController(stars)

    @expose(generic=True, template='json')
    def index(self):
        return [dict(id=key, name=value) for key, value in self.stars.items()]

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)
