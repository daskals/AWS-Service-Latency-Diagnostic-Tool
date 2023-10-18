# AWS-Service-Latency-Diagnostic-Tool
Python tool for diagnosing AWS IoT Core &amp; API Gateway latencies across AWS regions. Measures service response times, providing insights for optimal deployments based on region responsiveness.

Script Overview
This script is designed to measure the latency of two AWS services - AWS IoT Core and AWS API Gateway - across multiple AWS regions. By sending requests to these services and gauging the response time, it provides insights into their respective performances.

Key Components and Functionalities:
1. Region Data:
A predefined list of AWS regions with their corresponding human-readable names.
2. Latency Measurement Functions:
check_latency_iot: Measures the latency for the AWS IoT Core service in a designated region.

check_latency_api_gateway: Gauges the latency for the AWS API Gateway service in a designated region.

Both functions undertake a simple service-specific task multiple times (defaulted to 5 iterations) and then compute the average time taken (latency) for that task in the mentioned region. If a service isn't supported in a region, it's denoted as "Not supported".

3. Latency Compilation Function:
get_all_region_latencies: Processes all regions, fetches latency values using the given service-specific function, and yields a sorted list of latencies.
4. Execution and Display:
During execution, the script determines latencies for both AWS services across all regions, then showcases the results in an easy-to-understand manner. It also provides real-time updates on the iterations left, giving a clear picture of the progress.
This diagnostic tool is instrumental in understanding the responsiveness of these AWS services across diverse geographical zones. It stands beneficial for system architects and cloud strategists when making deployment choices.






