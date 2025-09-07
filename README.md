# DNS Speed Test Tool 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![GitHub stars](https://img.shields.io/github/stars/proars/Test-DNS-Speed.svg)](https://github.com/proars/Test-DNS-Speed/stargazers)

A high-performance DNS resolver benchmarking tool that helps you identify the fastest DNS servers for your infrastructure. Built with Python, this tool performs concurrent testing of multiple DNS resolvers against popular domains, providing detailed performance metrics and intelligent failure handling.

## 🎯 Key Features

- **Real-time Performance Testing**: Measures DNS response times in milliseconds
- **Parallel Processing**: Tests multiple DNS resolvers simultaneously
- **Smart Failure Detection**: Automatically identifies and drops unreliable DNS servers
- **Rich Visualization**: Beautiful progress bars and color-coded results
- **Comprehensive Analytics**: Statistical analysis including min/max/avg response times
- **Production-Ready**: Built-in error handling and retry mechanisms

## 🌟 Why Choose DNS Speed Test?

- **Infrastructure Optimization**: Perfect for DevOps engineers and system administrators
- **Network Troubleshooting**: Quickly identify DNS-related performance issues
- **Cloud Performance**: Optimize DNS settings for cloud-based applications
- **ISP Comparison**: Compare DNS performance across different service providers
- **Latency Monitoring**: Track DNS response times over time

## 📊 Technical Details

### Performance Features

- **Parallel Execution**: Uses Python's `concurrent.futures` for optimal performance
- **Smart Caching**: Maintains resolver history across runs
- **Adaptive Testing**: Drops unreliable resolvers to optimize testing time
- **Configurable Timeouts**: Customize query timeouts and retry attempts
- **Rich Statistics**: Comprehensive performance metrics and error tracking

### Reliability Features

- **Error Recovery**: Automatic retry mechanism for transient failures
- **Failure Tracking**: Persistent tracking of resolver reliability
- **Quick Fail**: Stops testing unreliable resolvers early
- **Success Rate Analysis**: Calculates resolver health metrics
- **Detailed Logging**: Comprehensive error and performance logging

## 🚀 Quick Start

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Getting Started

First, set up the project:

1. Clone the repository:

```bash
git clone https://github.com/proars/Test-DNS-Speed.git
cd Test-DNS-Speed
```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

### Basic Usage

Run with default settings:

```bash
python main.py
```

### Advanced Configuration

Customize the testing parameters:

```bash
python main.py --timeout 3.0 --retries 3 --workers 15 --max-failures 5
```

Available options:

| Option | Description | Default |
|--------|-------------|---------|
| `--timeout` | DNS query timeout (seconds) | 1.0 |
| `--retries` | Maximum query retries | 1 |
| `--workers` | Parallel worker count | 10 |
| `--max-failures` | Failures before dropping resolver | 3 |
| `--min-success-rate` | Minimum acceptable success rate | 0.5 |
| `--quick-fail` | Quick fail threshold | 3 |

## 📈 Example Output

```plaintext
Testing DNS resolvers... ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100%

✅ 1.1.1.1 (Cloudflare DNS): Average response time: 17.53 ms (15/15 successful queries)
✅ 8.8.8.8 (Google Public DNS): Average response time: 18.36 ms (15/15 successful queries)
✅ 9.9.9.9 (Quad9 DNS): Average response time: 16.31 ms (15/15 successful queries)
❌ Custom DNS: No successful queries (Failed 3 times, 0 attempts remaining)

╭──────────── DNS Resolver Performance Summary ────────────╮
│         Resolver         │ Min  │ Max  │ Avg  │ Success │
├────────────────────────┼──────┼──────┼──────┼─────────┤
│ Cloudflare DNS         │ 14ms │ 24ms │ 17ms │   100%  │
│ Google Public DNS      │ 13ms │ 26ms │ 18ms │   100%  │
│ Quad9 DNS             │ 10ms │ 26ms │ 16ms │   100%  │
╰────────────────────────────────────────────────────────╯
```

## 🔧 Advanced Features

### Custom DNS Resolvers

Add your own DNS resolvers by modifying the `DNS_RESOLVERS` list in `main.py`:

```python
DNS_RESOLVERS = [
    DNSResolver('8.8.8.8', 'Google Public DNS'),
    DNSResolver('1.1.1.1', 'Cloudflare DNS'),
    # Add your custom resolvers here
]
```

### Test Domains

Customize the test domains in `main.py`:

```python
TEST_DOMAINS = [
    "example.com",
    "google.com",
    # Add your domains here
]
```

## 📝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Star the Project

If you find this tool useful, please consider giving it a star on GitHub! It helps others discover the project and motivates further development.

## 📚 Related Projects

- [DNS Performance Test](https://github.com/topics/dns-performance)
- [Network Tools](https://github.com/topics/network-tools)
- [DNS Tools](https://github.com/topics/dns-tools)

## 🔍 Keywords

DNS, Speed Test, Network Performance, DNS Resolver, Python, Network Tools, DNS Benchmark, DNS Performance, Network Monitoring, System Administration, DevOps, Network Optimization

## Requirements

- Python 3.x
- Required libraries (install via requirements.txt):
  - `dnspython`: DNS library for Python
  - `rich`: Terminal formatting and progress bars

## Installation

1. Clone this repository:

```bash
git clone https://github.com/proars/Test-DNS-Speed.git
cd Test-DNS-Speed
```

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the script with default settings:

```bash
python main.py
```

Or customize the behavior with command-line arguments:

```bash
python main.py --timeout 3.0 --retries 3 --workers 15 --max-failures 5 --min-success-rate 0.7
```

Available options:

- `--timeout`: DNS query timeout in seconds (default: 2.0)
- `--retries`: Maximum retries for failed queries (default: 2)
- `--workers`: Number of parallel workers (default: 10)
- `--max-failures`: Maximum consecutive failures before dropping a resolver (default: 3)
- `--min-success-rate`: Minimum success rate to consider resolver healthy (default: 0.5)

The tool will test each configured DNS resolver against a list of popular domains and display:

- Average response times for each resolver with description
- Success rate of queries (successful/total)
- Detailed error reporting for failed queries
- Sorted results from fastest to slowest
- Parallel processing status

Example output:

```plaintext
⚠️ The following DNS resolvers have been dropped due to consistent failures:
   - 192.168.10.38 (Custom DNS 2): 3 consecutive failures

Testing 5 DNS resolvers across 15 domains...

✅ 8.8.8.8 (Google Public DNS): Average response time: 45.23 ms (15/15 successful queries)
✅ 1.1.1.1 (Cloudflare DNS): Average response time: 38.12 ms (15/15 successful queries)
✅ 9.9.9.9 (Quad9 DNS): Average response time: 52.45 ms (14/15 successful queries)
❌ 192.168.10.17 (Custom DNS 1): No successful queries (Failed 2 times, 1 attempt remaining)

Sorted results (fastest to slowest):
🚀 1.1.1.1 (Cloudflare DNS): 38.12 ms
🚀 8.8.8.8 (Google Public DNS): 45.23 ms
🚀 9.9.9.9 (Quad9 DNS): 52.45 ms

⚠️ Warning: The following DNS resolvers will be dropped in the next run:
   - 192.168.10.17 (Custom DNS 1): 2 consecutive failures
```

## Configuration

The script includes several popular DNS resolvers by default:

- Google Public DNS (8.8.8.8)
- Cloudflare DNS (1.1.1.1)
- Quad9 DNS (9.9.9.9)
- OpenDNS (208.67.222.222)
- Custom DNS resolvers

You can customize the following settings in the script:

```python
TIMEOUT = 2.0                  # DNS query timeout in seconds
MAX_RETRIES = 2               # Number of retries for failed queries
MAX_WORKERS = 10              # Number of parallel workers
MAX_CONSECUTIVE_FAILURES = 3   # Number of failures before dropping a resolver
```

## Output Files

The tool generates several output files:

1. `dns_test_history.json`: History of DNS resolver failures and success rates
2. `dns_test.log`: Detailed log file with error messages and events
3. `dns_stats.json`: Historical statistics for each resolver including:
   - Minimum response time
   - Maximum response time
   - Average response time
   - Median response time
   - Standard deviation
   - Success rate
   - Total queries

When a resolver fails all queries in consecutive test runs (default: 3) or its success rate falls below the minimum threshold (default: 50%), it will be automatically dropped from future tests until manually re-added.

To add or modify DNS resolvers, edit the `DNS_RESOLVERS` list in the script:

```python
DNS_RESOLVERS = [
    DNSResolver('8.8.8.8', 'Google Public DNS'),
    DNSResolver('1.1.1.1', 'Cloudflare DNS'),
    # Add your custom resolvers here
]
```

## Learn More

For detailed information about DNS resolver speed testing, visit [How to Test DNS Resolver Speed](https://arstech.net/how-to-test-dns-resolver-speed/)

## Contributing

Contributions are welcome! Feel free to:

- Report issues
- Suggest improvements
- Submit pull requests

## License

This project is open-source and available under the [MIT License](LICENSE). This means you can:

- ✔️ Use it commercially
- ✔️ Modify it
- ✔️ Distribute it
- ✔️ Use it privately

The only requirement is to include the original copyright and license notice in any copy of the software/source.

---

## Keywords

DNS speed test, DNS resolver benchmark, Python DNS tools, network performance, DNS response time, DNS latency measurement
