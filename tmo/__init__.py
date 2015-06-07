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
from .posts import Post
from .threads import Thread
from xmlrpc.client import ServerProxy
import logging


__title__ = 'tmo'
__version__ = '0.2'
__url__ = 'https://github.com/mattaustin/tmo'
__author__ = 'Matt Austin <mail@mattaustin.me.uk>'
__copyright__ = 'Copyright 2015 Matt Austin'
__license__ = 'Apache 2.0'


class Client:
    """Forum client.

    http://talk.maemo.org/

    """

    _forum_data = []

    endpoint = 'http://talk.maemo.org/mobiquo/mobiquo.php'

    def __init__(self, endpoint=None):
        self._logger = self._get_logger()
        self._set_endpoint(endpoint)
        self._serverproxy = ServerProxy(self.endpoint)

    def _set_endpoint(self, endpoint):
        self.endpoint = endpoint or self.endpoint
        self._logger.debug('Client endpoint set to: {0}'.format(self.endpoint))

    def _get_logger(self):
        return logging.getLogger(__name__)

    def get_forums(self):
        if not self._forum_data:
            self._forum_data = self._serverproxy.get_forum()
        return [Forum(client=self, data=data) for data in self._forum_data]

    def get_posts(self, thread, start, end):
        response = self._serverproxy.get_thread(thread.id, start, end).get(
            'posts', [])
        return [Post(client=self, data=data) for data in response]

    def get_threads(self, forum, start, end):
        response = self._serverproxy.get_topic(forum.id, start, end).get(
            'topics', [])
        return [Thread(client=self, data=data) for data in response]
