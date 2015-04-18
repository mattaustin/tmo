===
tmo
===

A Python client for talk.maemo.org.


In early development stages. Initially aiming to cover basic functionality for
reading of the forum.


Example
=======

.. code-block:: python

    import tmo

    client = tmo.ForumClient()

    client.get_forums()
    # [<Forum: General>,
    #  <Forum: Brainstorm>,
    #  ...]

    forum = client.get_forums()[0]

    forum.get_threads()
    # [<Thread: New members say hello!>,
    #  <Thread: READ THIS before posting a new thread>,
    #  ...]

    thread = forum.get_threads()[1]

    thread.get_posts()
    # [<Post: johndoe 2001-02-03 04:05:06>,
    #  ...]

    post = thread.get_posts()[0]

    post.content
    # 'Welcome to Internet Tablet Talk (soon to become talk.maemo.org)! ...'
