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


from bs4 import BeautifulSoup
from bs4.element import Tag
from urllib.parse import parse_qs, urlencode, urlparse


class Resource:

    _html = {}

    _page = None

    def __init__(self, id, client, page=None, data=None):
        """

        :param str id: The resource ID.
        :param client: The associated forum client instance.
        :type client: :py:class:`~tmo.ForumClient`
        :param dict data: Initial data.

        """

        self.id = id
        self._client = client
        self._data = data or {}

        if page is not None:
            self.page = page

    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__, self)

    def __str__(self):
        return '{0}'.format(self.get_url())

    @classmethod
    def from_link(class_, client, link, data=None):
        if data is None:
            data = {}
        if isinstance(link, Tag):
            href = link.get('href')
            data.update({'name': link.text})
        else:
            href = link

        querystring = parse_qs(urlparse(href).query)

        # TODO - why is this sometimes None?
        try:
            id_ = querystring[class_._querystring_id_key][0]
        except (KeyError, IndexError):
            id_ = None

        kwargs = {'id': id_, 'client': client, 'data': data}
        if querystring.get('page', False):
            kwargs.update({'page': querystring['page'][0]})
        return class_(**kwargs)

    def _get_html(self, refresh=False):
        """Get the parsed html content for this resource.

        :param bool refresh: If True, any cached data is ignored and data is
          fetched from the client. Default: False.

        """

        url = self.get_url()
        if not self._html.get(url, False) or refresh:
            response = self._client.session.get(url)
            assert response.status_code == 200
            self._html[url] = BeautifulSoup(response.content)
        return self._html[url]

    def get_url(self, **kwargs):
        kwargs.update({self._querystring_id_key: self.id})
        if self._page:
            kwargs.update({'page': self._page})
        return self._client._construct_url(
            '{path}?{querystring}'.format(path=self._url_path,
                                          querystring=urlencode(kwargs)))

    @property
    def page(self):
        if self._page is None:
            # Determine page from html
            matches = self._get_html().select('.pagenav strong')
            self._page = int(matches[0].text) if matches else 1
            matches = 1
        return self._page

    @page.setter
    def page(self, value):
        self._page = value

    @property
    def has_next_page(self):
        nav = self._get_html().find(class_='pagenav')
        return bool(nav.find(name='a', text='Next >')) if nav else False

    @property
    def has_previous_page(self):
        nav = self._get_html().find(class_='pagenav')
        return bool(nav.find(name='a', text='< Prev')) if nav else False
