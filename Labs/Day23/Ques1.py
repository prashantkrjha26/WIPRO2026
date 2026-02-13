# 1. Threading (I/O-bound tasks)

# Question:
# You need to download data from multiple URLs concurrently.

# You have a list of URLs:

# urls = [
# "https://example.com/data1",
# "https://example.com/data2",
# "https://example.com/data3",
# "https://example.com/data4"
# ]

# Write Python code to:
# 1. Use threading to download the content of all URLs concurrently.
# 2. Save each URL’s content to a separate text file (data1.txt, data2.txt, etc.).
# 3. Measure and print the total time taken to download all files using threading
# versus sequential downloads.
# Hint: Use requests library for HTTP requests and threading.Thread for concurrency.




# Import required libraries
import requests
import threading
import time

# List of real websites
urls = [
    "https://www.google.com",
    "https://www.rediff.com",
    "https://www.python.org",
    "https://www.microsoft.com"
]

# Function to download website content and save to file
def download_file(url):
    try:
        # Send HTTP GET request
        response = requests.get(url, timeout=10)

        # Raise exception if status is not 200
        response.raise_for_status()

        # Create a clean filename from URL
        filename = url.replace("https://", "").replace("www.", "").replace(".", "_") + ".txt"

        # Write page content to file
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"Downloaded: {url}")

    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")



# Sequential Download


start_time = time.perf_counter()

for url in urls:
    download_file(url)

sequential_time = time.perf_counter() - start_time
print("\nSequential Download Time:", sequential_time, "seconds")



# Threaded Download


threads = []
start_time = time.perf_counter()

for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

threading_time = time.perf_counter() - start_time
print("Threaded Download Time:", threading_time, "seconds")



# Comparison


print("\nComparison Result:")
print("Sequential Time:", sequential_time, "seconds")
print("Threaded Time:", threading_time, "seconds")
