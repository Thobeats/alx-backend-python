#!/usr/bin/env python3
"""A basic aync module"""

from asyncio import run, sleep
from random import random


async def wait_random(max_delay: int=10) -> float:
    """A function to generate a random number"""
    delay = random() * max_delay
    await sleep(delay)
    return delay
