import requests
import concurrent.futures
import time

# Configuration
lb_dns = 'http://rapplb-607517949.us-east-1.elb.amazonaws.com/'  # Replace with your Load Balancer DNS
num_requests = 10000  # Total number of requests
concurrent_requests = 100  # Number of concurrent requests

# Function to make a single request
def make_request():
    try:
        response = requests.get(lb_dns)
        print(f'Response Code: {response.status_code}')
    except requests.RequestException as e:
        print(f'Request failed: {e}')

# Function to make concurrent requests
def make_concurrent_requests():
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(make_request) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f'Error in future: {e}')

if __name__ == '__main__':
    start_time = time.time()
    make_concurrent_requests()
    duration = time.time() - start_time
    print(f'Completed {num_requests} requests in {duration} seconds')
