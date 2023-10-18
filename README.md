# AWS-Service-Latency-Diagnostic-Tool
Python tool for diagnosing AWS IoT Core &amp; API Gateway latencies across AWS regions. Measures service response times, providing insights for optimal deployments based on region responsiveness.

## Script Overview

This script is designed to measure the latency of two AWS services - AWS IoT Core and AWS API Gateway - across multiple AWS regions. By sending requests to these services and gauging the response time, it provides insights into their respective performances.

### Key Components and Functionalities:

#### 1. **Region Data**:
- A predefined list of AWS regions with their corresponding human-readable names.

#### 2. **Latency Measurement Functions**:
- **`check_latency_iot`**: Measures the latency for the AWS IoT Core service in a designated region.
- **`check_latency_api_gateway`**: Gauges the latency for the AWS API Gateway service in a designated region.

  Both functions undertake a simple service-specific task multiple times (defaulted to 10 iterations) and then compute the average time taken (latency) for that task in the mentioned region. If a service isn't supported in a region, it's denoted as "Not supported".

#### 3. **Latency Compilation Function**:
- **`get_all_region_latencies`**: Processes all regions, fetches latency values using the given service-specific function, and yields a sorted list of latencies.

#### 4. **Execution and Display**:
- During execution, the script determines latencies for both AWS services across all regions and then showcases the results in an easy-to-understand manner. It also provides real-time updates on the iterations left, giving a clear picture of the progress.

This diagnostic tool is instrumental in understanding the responsiveness of these AWS services across diverse geographical zones. It stands beneficial for system architects and cloud strategists when making deployment choices.

## Sample Output

The below output is a result of running the script from Edinburgh:

```
...
API Gateway Iteration 9 for eu-north-1: 0.0849 seconds. Total Remaining iterations: 1
API Gateway Iteration 10 for eu-north-1: 0.0820 seconds. Total Remaining iterations: 0
------------------------------------
Latencies for AWS IoT Core:
------------------------------------
Europe (London) (eu-west-2): 0.0309 seconds
Europe (Paris) (eu-west-3): 0.0378 seconds
Europe (Frankfurt) (eu-central-1): 0.0428 seconds
Europe (Ireland) (eu-west-1): 0.0496 seconds
Europe (Stockholm) (eu-north-1): 0.0674 seconds
Canada (Central) (ca-central-1): 0.1209 seconds
US East (Ohio) (us-east-2): 0.1289 seconds
US East (N. Virginia) (us-east-1): 0.1398 seconds
US West (N. California) (us-west-1): 0.1979 seconds
US West (Oregon) (us-west-2): 0.2094 seconds
Asia Pacific (Singapore) (ap-southeast-1): 0.2252 seconds
Asia Pacific (Mumbai) (ap-south-1): 0.2371 seconds
Asia Pacific (Tokyo) (ap-northeast-1): 0.3076 seconds
Asia Pacific (Seoul) (ap-northeast-2): 0.3292 seconds
Asia Pacific (Sydney) (ap-southeast-2): 0.3404 seconds
Asia Pacific (Osaka) (ap-northeast-3): Not supported
------------------------------------

Latencies for AWS API Gateway:
------------------------------------
Europe (London) (eu-west-2): 0.0611 seconds
Europe (Paris) (eu-west-3): 0.0622 seconds
Europe (Ireland) (eu-west-1): 0.0631 seconds
Europe (Frankfurt) (eu-central-1): 0.0700 seconds
Europe (Stockholm) (eu-north-1): 0.0979 seconds
Canada (Central) (ca-central-1): 0.1429 seconds
US East (N. Virginia) (us-east-1): 0.1477 seconds
US East (Ohio) (us-east-2): 0.1505 seconds
US West (Oregon) (us-west-2): 0.2191 seconds
US West (N. California) (us-west-1): 0.2243 seconds
Asia Pacific (Mumbai) (ap-south-1): 0.2601 seconds
Asia Pacific (Singapore) (ap-southeast-1): 0.3195 seconds
Asia Pacific (Osaka) (ap-northeast-3): 0.3255 seconds
Asia Pacific (Seoul) (ap-northeast-2): 0.3328 seconds
Asia Pacific (Tokyo) (ap-northeast-1): 0.3337 seconds
Asia Pacific (Sydney) (ap-southeast-2): 0.3587 seconds

Process finished with exit code 0
```



