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


from .members import Member
from .resources import Resource
from datetime import datetime, timedelta


class Post(Resource):
    """A post."""

    _querystring_id_key = 'p'

    _url_path = 'showpost.php'

    def __str__(self):
        return '{0} {1}'.format(self.member, self.datetime)

    @classmethod
    def from_html(class_, client, html):
        member_link = html.select('.username [href^="member"]')[0]
        member = Member.from_link(client=client, link=member_link)
        postdate = html.select('.postdate')[0]
        postdetails = html.select('.postdetails')[0]
        for signature in postdetails.select('.signature'):
            signature.decompose()
        content = postdetails.text.strip()
        link = html.select('a[href^="showpost"]')[0]
        return class_.from_link(client=client, link=link,
                                data={'content': content, 'member': member,
                                      'postdate': postdate})

    @property
    def content(self):
        return self._data.get('content')

    @property
    def datetime(self):
        d = self._data.get('postdate')
        postdate = ' '.join([i.strip() for i in d.text.split(',')])
        today = datetime.today().strftime('%Y-%m-%d')
        yesterday = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
        postdate = postdate.replace('Today', today)
        postdate = postdate.replace('Yesterday', yesterday)
        return datetime.strptime(postdate, '%Y-%m-%d %H:%M')

    @property
    def member(self):
        return self._data.get('member')
