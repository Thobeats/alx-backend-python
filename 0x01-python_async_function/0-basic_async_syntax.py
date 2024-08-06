#!/usr/bin/env python3
"""A basic aync module"""

from asyncio import run, sleep
from random import uniform


async def wait_random(max_delay=10):
    """A function to generate a random number"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
