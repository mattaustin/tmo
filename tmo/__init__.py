# -*- coding: utf-8 -*-

# Copyright 2015 Matt Austin

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from .forums import Forum
import logging
import requests

from . import lib
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter


__title__ = 'tmo'
__version__ = '0.1.0'
__url__ = 'https://github.com/mattaustin/tmo'
__author__ = 'Matt Austin <mail@mattaustin.me.uk>'
__copyright__ = 'Copyright 2015 Matt Austin'
__license__ = 'Apache 2.0'


class ForumClient:
    """Forum client.

    http://talk.maemo.org/

    """

    _user_agent = '{name}/{version} ({name}; +{url})'.format(
        name=__title__, version=__version__, url=__url__)

    endpoint = 'http://talk.maemo.org/'

    logged_in = False

    max_retries = 5

    def __init__(self, endpoint=None, username=None, password=None):
        """

        :param str endpoint: Client endpoint URL. Defaults to 'talk.maemo.org'.
        :param str username: Your forum account username.
        :param str password: Your forum account password.

        """

        self._logger = self._get_logger()

        self._set_endpoint(endpoint)

        self.username = username
        self.password = password

        self.session = self._create_session()

        if self.username and self.password:
            self.login()

    def __repr__(self):
        username = self.username or ''
        return '<{0}: {1}>'.format(self.__class__.__name__, username)

    def _get_logger(self):
        return logging.getLogger(__name__)

    def _create_session(self):
        session = requests.Session()
        session.mount(self.endpoint, HTTPAdapter(max_retries=self.max_retries))
        session.headers = {'User-Agent': self._user_agent}
        return session

    def _set_endpoint(self, endpoint):
        self.endpoint = endpoint or self.endpoint
        self._logger.debug('Client endpoint set to: {0}'.format(self.endpoint))

    def _construct_url(self, path):
        return '{endpoint}{path}'.format(endpoint=self.endpoint,
                                         path=path.strip())

    def get_forums(self, refresh=False):
        """Get the forums for this site.

        :param bool refresh: If True, any cached data is ignored and data is
          fetched from the client. Default: False.

        :returns: List of :py:class:`~tmo.forums.Forum` instances.
        :rtype: list

        """

        if not hasattr(self, '_forums') or refresh:
            response = self.session.get(self.get_url())
            assert response.status_code == 200
            html = BeautifulSoup(response.content, 'html.parser')
            links = html.select(
                '#forumlist .forum_sub a[href^="forumdisplay"]')
            self._forums = [Forum.from_link(client=self, link=link)
                            for link in links]
        return self._forums

    def get_url(self):
        return self._construct_url('index.php')

    def login(self, *args, **kwargs):
        """Login using session (cookie) authentication."""
        raise NotImplementedError()

    def logout(self, *args, **kwargs):
        """Logout."""
        raise NotImplementedError()
