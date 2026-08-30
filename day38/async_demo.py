import asyncio
import time

async def fake_fetch_url(url, delay):
    print(f"Fetching {url}")
    await asyncio.sleep(delay)
    return f'{url} -> data took {delay}s'

async def main():
    urls_with_delays = [
        ("home/sujal/doucments", 4),
        ("home/sujal/downloads", 1),
        ("home/sujal/music", 3.5),
        ("home/sujal/video", 2),
        ("home/sujal/onedrive", 1.5),
        ("home/sujal/e", 3)
    ]
    start = time.time()
    results = await asyncio.gather(
            *[fake_fetch_url(url, delay) for url, delay in urls_with_delays]
            )
    elapsed = time.time() - start
    for r in results:
        print(' -', r)
    print(f"\nAsync Time: {elapsed:.2f}s")

asyncio.run(main())
