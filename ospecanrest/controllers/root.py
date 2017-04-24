from pecan import expose
from webob.exc import status_map
from ospecanrest.controllers.api import api


class RootController(object):

    api = api.ApiController()

    @expose('error.html')
    def error(self, status):
        try:
            status = int(status)
        except ValueError:  # pragma: no cover
            status = 500
        message = getattr(status_map.get(status), 'explanation', '')
        return dict(status=status, message=message)

