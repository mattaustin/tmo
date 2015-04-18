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


from .posts import Post
from .resources import Resource


class Thread(Resource):
    """A thread."""

    _querystring_id_key = 't'

    _url_path = 'showthread.php'

    def __str__(self):
        return '{0}'.format(self.title)

    def get_posts(self, refresh=False):
        """Get the posts for this thread.

        :param bool refresh: If True, any cached data is ignored and data is
          fetched from the client. Default: False.

        :returns: List of :py:class:`~tmo.posts.Post` instances.
        :rtype: list

        """

        elements = self._get_html(refresh=refresh).select('#posts .page')
        return [Post.from_html(client=self._client, html=html)
                for html in elements]

    @property
    def title(self):
        return self._data.get('name', self.id)
