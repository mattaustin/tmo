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


from datetime import datetime


class Post:

    _data = {}

    def __init__(self, client, id=None, data=None):
        self.client = client
        self._id = id
        if data is not None:
            self._data = data

    def __repr__(self):
        return '<{0}: {1}>'.format(self.__class__.__name__, self)

    def __str__(self):
        return self.title or self.id

    @property
    def content(self):
        return str(self._data.get('post_content'))

    @property
    def datetime(self):
        # TODO - Does API always return datetime in UTC?
        return datetime.strptime(self._data['post_time'].value,
                                 '%Y%m%dT%H:%M:%S+00:00')

    @property
    def id(self):
        return self._id or self._data.get('post_id')

    @property
    def title(self):
        return str(self._data.get('post_title'))
