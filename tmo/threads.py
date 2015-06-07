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


class Thread:

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
    def id(self):
        return self._id or self._data.get('topic_id')

    @property
    def title(self):
        return str(self._data.get('topic_title'))

    def get_posts(self, start, end):
        return self.client.get_posts(thread=self, start=start, end=end)
