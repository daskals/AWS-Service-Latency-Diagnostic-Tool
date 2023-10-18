#######################################################
#     Spiros Daskalakis                               #
#     last Revision: 18/10/2023                       #
#     Python Version:  3.9                            #
#     Email: daskalakispiros@gmail.com                #
#     Website: www.daskalakispiros.com                #
#######################################################

# This script measures and displays the latency of AWS IoT Core and AWS API Gateway across multiple AWS regions.
# It sends service-specific requests to these AWS services in each region,
# gauges the response time, and then presents the results in a user-friendly manner.

import boto3
import time


# Define a global variable to hold the total iterations count
total_remaining_iterations = 0

# A dictionary containing the AWS regions and their respective descriptive names
region_data = {
    'us-east-1': 'US East (N. Virginia)',
    'us-east-2': 'US East (Ohio)',
    'us-west-1': 'US West (N. California)',
    'us-west-2': 'US West (Oregon)',
    'ap-south-1': 'Asia Pacific (Mumbai)',
    'ap-northeast-3': 'Asia Pacific (Osaka)',
    'ap-northeast-2': 'Asia Pacific (Seoul)',
    'ap-southeast-1': 'Asia Pacific (Singapore)',
    'ap-southeast-2': 'Asia Pacific (Sydney)',
    'ap-northeast-1': 'Asia Pacific (Tokyo)',
    'ca-central-1': 'Canada (Central)',
    'eu-central-1': 'Europe (Frankfurt)',
    'eu-west-1': 'Europe (Ireland)',
    'eu-west-2': 'Europe (London)',
    'eu-west-3': 'Europe (Paris)',
    'eu-north-1': 'Europe (Stockholm)'
}


def check_latency_iot(region_code, num_iterations=5):
    # Reference the global variable
    global total_remaining_iterations

    # List to hold latency values for each iteration
    latencies = []

    # Establish a boto3 client for the IoT service
    client = boto3.client('iot', region_name=region_code)

    # Loop for each iteration to measure latency
    for i in range(num_iterations):
        start_time = time.time()
        try:
            # Send a request to the IoT service and record the time taken
            client.list_things(maxResults=1)
            end_time = time.time()
            latencies.append(end_time - start_time)
            print(
                f"IoT Core Iteration {i + 1} for {region_code}: {latencies[-1]:.4f} seconds. Total Remaining iterations: {total_remaining_iterations - 1}")
            total_remaining_iterations -= 1
        except Exception as e:
            # Handle exceptions, particularly the one indicating a non-supported endpoint
            if "Could not connect to the endpoint URL" in str(e):
                total_remaining_iterations -= num_iterations
                return "Not supported"
            else:
                print(f"Error in Iteration {i + 1} checking IoT latency in {region_code}: {e}")
                latencies.append(float('inf'))
    return sum(latencies) / len(latencies)

# Similar function to the above but for the API Gateway service
def check_latency_api_gateway(region_code, num_iterations=5):
    global total_remaining_iterations
    latencies = []
    client = boto3.client('apigateway', region_name=region_code)
    for i in range(num_iterations):
        start_time = time.time()
        try:
            client.get_rest_apis(limit=1)
            end_time = time.time()
            latencies.append(end_time - start_time)
            print(
                f"API Gateway Iteration {i + 1} for {region_code}: {latencies[-1]:.4f} seconds. Total Remaining iterations: {total_remaining_iterations - 1}")
            total_remaining_iterations -= 1
        except Exception as e:
            if "Could not connect to the endpoint URL" in str(e):
                total_remaining_iterations = total_remaining_iterations - num_iterations
                return "Not supported"


            else:
                print(f"Error in Iteration {i + 1} checking API Gateway latency in {region_code}: {e}")
                latencies.append(float('inf'))

    return sum(latencies) / len(latencies)


def get_all_region_latencies(service_check_function):
    # Dictionary to store the latency results for each region
    latencies = {}

    # Iterate through each region and record its latency
    for region_code, region_name in region_data.items():
        latencies[(region_name, region_code)] = service_check_function(region_code)

    # Return the latencies sorted first by unsupported regions and then by latency values
    return sorted(latencies.items(), key=lambda x: (isinstance(x[1], str), x[1]))


if __name__ == "__main__":
    print("Please Wait...")
    iteration_var = 10
    # Calculate total iterations based on regions and the functions used
    total_regions = len(region_data)  # Dynamically get the number of regions
    # Functions one for IoT Core and One for Gateway API
    num_functions_running = 2
    total_remaining_iterations = total_regions * iteration_var * num_functions_running
    # Obtain latencies for each service
    iot_latencies = get_all_region_latencies(lambda x: check_latency_iot(x, iteration_var))
    api_gateway_latencies = get_all_region_latencies(lambda x: check_latency_api_gateway(x, iteration_var))#

    print("------------------------------------")
    print("Latencies for AWS IoT Core:")
    print("------------------------------------")
    for (region_name, region_code), latency in iot_latencies:
        print(f"{region_name} ({region_code}): {latency if isinstance(latency, str) else f'{latency:.4f} seconds'}")
    print("------------------------------------")
    print("\nLatencies for AWS API Gateway:")
    print("------------------------------------")
    for (region_name, region_code), latency in api_gateway_latencies:
        print(f"{region_name} ({region_code}): {latency if isinstance(latency, str) else f'{latency:.4f} seconds'}")
