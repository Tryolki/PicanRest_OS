from oslo_config import cfg
from oslo_log import log as logging
from oslo_service import service, wsgi
from ospecanrest.controllers.api import api

CONF = cfg.CONF
opt_group = cfg.OptGroup(name="pecan_group")
simple_opts = [
    cfg.StrOpt('host'),
    cfg.StrOpt('port')
]
CONF.register_group(opt_group)
CONF.register_opts(simple_opts, opt_group)
LOG = logging.getLogger(__name__)


class WSGIService(service.ServiceBase):

    def start(self):
        print(self.pecan_server)
        print(CONF.pecan_group.host)
        self.pecan_server.start()

    def wait(self):
        self.pecan_server.wait()

    def stop(self):
        self.pecan_server.stop()

    def reset(self):
        self.pecan_server.reset()

CONF(default_config_files=['config.conf'])
serv = WSGIService()
launcher = service.launch(CONF, serv)
launcher.wait()
