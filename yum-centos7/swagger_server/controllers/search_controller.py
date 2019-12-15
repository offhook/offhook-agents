
from swagger_server.models.download_spec import DownloadSpec  # noqa: E501
from swagger_server.models.search_results import SearchResults  # noqa: E501
from .base_controller import BaseController
#from swagger_server import util


class SearchController(BaseController):

    def search():  # noqa: E501
        """Search for packages

         # noqa: E501

        :param body:
        :type body: dict | bytes

        :rtype: List[SearchResults]
        """
        return 'do some magic!'

    def add_url_rules(self):
        self._add_url_rule('/', SearchController.search, methods=['POST'])