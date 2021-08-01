#!/usr/bin/bash/env python3
"""
coroutines in asyncio
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    an asynchronous coroutine task that takes an integer
    argument that waits for a random delay between 0 and
    max_delay seconds and eventually returns it

    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay