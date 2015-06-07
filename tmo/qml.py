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


from tmo import Client
from tmo.forums import Forum
from tmo.threads import Thread
import logging


PAGINATE_BY = 50


# Debug
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


client = Client()


def get_forums():
    categories = client.get_forums()
    forums = []
    for category in categories:
        forums += category.get_forums()
    return [{'id': forum.id, 'name': forum.name} for forum in forums]


def get_threads(forum_id, page):
    forum = Forum(client=client, id=forum_id)
    end = (page * PAGINATE_BY) - 1
    start = (page * PAGINATE_BY) - PAGINATE_BY
    threads = forum.get_threads(start=start, end=end)
    return [[{'id': thread.id, 'title': thread.title}
             for thread in threads], True]  # forum.has_next_page]


def get_posts(thread_id, page):
    thread = Thread(client=client, id=thread_id)
    end = (page * PAGINATE_BY) - 1
    start = (page * PAGINATE_BY) - PAGINATE_BY
    posts = thread.get_posts(start=start, end=end)
    return [[{'id': post.id, 'content': post.content,
              'member': '{}'.format(post._data['post_author_name']),
              'datetime': post.datetime}
             for post in posts], True]  # thread.has_next_page]
