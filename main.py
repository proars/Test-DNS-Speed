import dns.resolver
import time


# List of DNS resolvers to test
dns_resolvers = [
    '8.8.8.8',   # Google Public DNS
    '192.168.10.17',   # DNS2
    '192.168.10.38',   # DNS2

]

# Preloaded list of 100 domains for testing
test_domains = [
    "example.com", "google.com", "amazon.com", "apple.com", "microsoft.com",
    "facebook.com", "yahoo.com", "wikipedia.org", "github.com", "stackoverflow.com",
    "netflix.com", "reddit.com", "linkedin.com", "bing.com", "quora.com",
]

# Function to test a single resolver for a single domain
def test_resolver_speed(resolver_ip, domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [resolver_ip]
    try:
        start_time = time.time()
        resolver.resolve(domain, "A")
        end_time = time.time()
        return (end_time - start_time) * 1000  # Convert to milliseconds
    except Exception as e:
        return None  # Return None if query fails

# Test all resolvers across all domains
print(f"Testing DNS resolvers across {len(test_domains)} domains...\n")
results = {}

for dns_ip in dns_resolvers:
    total_time = 0
    success_count = 0
    for domain in test_domains:
        response_time = test_resolver_speed(dns_ip, domain)
        if response_time is not None:
            total_time += response_time
            success_count += 1
    average_time = total_time / success_count if success_count > 0 else None
    results[dns_ip] = average_time
    if average_time is not None:
        print(f"{dns_ip}: Average response time: {average_time:.2f} ms ({success_count}/{len(test_domains)} successful queries)")
    else:
        print(f"{dns_ip}: No successful queries")

# Print sorted results
print("\nSorted results (fastest to slowest):")
sorted_results = sorted(results.items(), key=lambda x: x[1] if x[1] is not None else float('inf'))
for dns_ip, average_time in sorted_results:
    if average_time is not None:
        print(f"{dns_ip}: {average_time:.2f} ms")
    else:
        print(f"{dns_ip}: No successful queries")
