
from urllib.request import urlopen, Request
from urllib.error import HTTPError, URLError
from time import perf_counter


def check_website(url):
    """Check whether a website responds."""

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    request = Request(
        url,
        headers={"User-Agent": "NetworkChecker/1.0"}
    )

    start_time = perf_counter()

    try:
        with urlopen(request, timeout=5) as response:
            status_code = response.status
            elapsed = perf_counter() - start_time

            print("\n--- Connection Result ---")
            print(f"Website: {url}")
            print(f"Status Code: {status_code}")
            print(f"Response Time: {elapsed:.2f} seconds")
            print("Result: SUCCESS")

    except HTTPError as error:
        elapsed = perf_counter() - start_time

        print("\n--- Connection Result ---")
        print(f"Website: {url}")
        print(f"Status Code: {error.code}")
        print(f"Response Time: {elapsed:.2f} seconds")
        print("Result: HTTP ERROR")

    except (URLError, TimeoutError, OSError) as error:
        print("\n--- Connection Result ---")
        print(f"Website: {url}")
        print("Result: FAILED")
        print(f"Reason: {error}")


def main():
    print("=== Network Checker v1.0 ===")
    print("Check whether a website responds.")

    url = input("\nEnter a website URL: ").strip()

    if not url:
        print("Error: URL cannot be empty.")
        return

    check_website(url)


if __name__ == "__main__":
    main()
