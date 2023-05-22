import requests
import threading

def send_request(url):
    try:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending request to {url}: {e}")

# Define the URL of your server
url = "http://localhost:8000/"

# Define the number of requests and concurrent connections
num_requests = 10000
num_concurrent = 100

# Create a list of threads to handle the requests
threads = []

# Start the load test
for _ in range(num_concurrent):
    t = threading.Thread(target=send_request, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

print("Load test completed.")
