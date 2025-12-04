"""
Simple parallel runner with max concurrency.

Instead of waiting for all 40 to finish before starting the next 40,
this starts a new task as soon as one finishes.
"""
import asyncio


async def run_parallel(tasks, max_concurrent=40):
    """
    Run tasks with max concurrency. New task starts as soon as one finishes.
    
    Args:
        tasks: List of coroutines to run
        max_concurrent: Max running at once (default 40)
    
    Returns:
        List of results in same order as input tasks
    """
    semaphore = asyncio.Semaphore(max_concurrent)
    
    async def run_one(task):
        async with semaphore:
            return await task
    
    return await asyncio.gather(*[run_one(t) for t in tasks])

