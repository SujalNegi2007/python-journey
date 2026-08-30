import time

def fake_fetch_url(url, delay):
    print(f"Fetching {url}")
    time.sleep(delay)
    return f'{url} -> data took {delay}s'

def main():
    urls_with_delays = [
        ("home/sujal/doucments", 4),
        ("home/sujal/downloads", 1),
        ("home/sujal/music", 3.5),
        ("home/sujal/video", 2),
        ("home/sujal/onedrive", 1.5),
        ("home/sujal/e", 3)
    ]
    start = time.time()

    results = []
    for url, delay in urls_with_delays:
        results.append(fake_fetch_url(url, delay))

    elapsed = time.time() - start
    for r in results:
        print(' -', r)
    print(f"\nsync Time: {elapsed:.2f}s")

main()
