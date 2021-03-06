#!/usr/bin/env python
import asyncio
import uvloop
from novels_search.fetcher.cache import update_all_books


def update_all():
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(update_all_books())
    loop.run_until_complete(task)
    return task.result()

print(update_all())