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


from .resources import Resource
from .threads import Thread


class Forum(Resource):
    """A forum."""

    _querystring_id_key = 'f'

    _url_path = 'forumdisplay.php'

    def __str__(self):
        return '{0}'.format(self.name)

    def get_threads(self, refresh=False):
        """Get the threads for this forum.

        :param bool refresh: If True, any cached data is ignored and data is
          fetched from the client. Default: False.

        :returns: List of :py:class:`~tmo.threads.Thread` instances.
        :rtype: list

        """

        links = self._get_html(refresh=refresh).select(
            '.page .DiscussionTopic > .threadTitle > a[href^="showthread"]')

        return [Thread.from_link(client=self._client, link=link)
                for link in links]

    @property
    def name(self):
        return self._data.get('name', self.id)
