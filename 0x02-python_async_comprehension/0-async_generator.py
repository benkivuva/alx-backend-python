#!/usr/bin/env python3
""" Asynchronous Generator Example """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous generator that yields random numbers between 0 and 10.

    This generator loops 10 times, and in each iteration, it asynchronously
    waits for 1 second using asyncio.sleep, and then yields a random float
    between 0 and 10.

    Yields:
        float: A random float between 0 and 10.

    Raises:
        None: This generator does not raise any exceptions.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
