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


from tmo import ForumClient
from tmo.forums import Forum
from tmo.threads import Thread
import logging


# Debug
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


client = ForumClient()


def get_forums():
    forums = client.get_forums()
    return [{'url': forum.get_url(), 'name': forum.name} for forum in forums]


def get_threads(forum_url, page):
    forum = Forum.from_link(client=client, link=forum_url)
    forum.page = page
    threads = forum.get_threads()
    return [[{'url': thread.get_url(), 'title': thread.title}
            for thread in threads], forum.has_next_page]


def get_posts(thread_url, page):
    thread = Thread.from_link(client=client, link=thread_url)
    thread.page = page
    posts = thread.get_posts()
    return [[{'url': post.get_url(), 'content': post.content,
              'member': '{}'.format(post.member), 'datetime': post.datetime}
             for post in posts], thread.has_next_page]
