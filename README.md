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



## 📋 Output Files and Configuration

### Generated Files

- `dns_test_history.json`: Tracks resolver failures and success rates
- `dns_test.log`: Detailed error messages and events
- `dns_stats.json`: Comprehensive resolver statistics including:
  - Response time metrics (min/max/avg/median)
  - Standard deviation
  - Success rates
  - Query counts

### Default Resolvers

The tool comes pre-configured with popular DNS resolvers:

- Google Public DNS (8.8.8.8)
- Cloudflare DNS (1.1.1.1)
- Quad9 DNS (9.9.9.9)
- OpenDNS (208.67.222.222)

## ❓ Learn More

For detailed information about DNS resolver speed testing, visit [How to Test DNS Resolver Speed](https://arstech.net/how-to-test-dns-resolver-speed/)

## 🤝 Contributing

We welcome contributions! Here's how you can help:

- Report bugs and suggest features
- Improve documentation
- Submit pull requests
- Share your experience

Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## ⚖️ License

This project is open source under the [MIT License](LICENSE).

### Permissions

- ✔️ Use commercially
- ✔️ Modify
- ✔️ Distribute
- ✔️ Use privately

### License Terms

- Include the original license and copyright notice

---

Made with ❤️ by [proars](https://github.com/proars)

## 🔍 Keywords

DNS, Speed Test, Network Performance, DNS Resolver, Python, Network Tools, DNS Benchmark, DNS Performance, Network Monitoring, System Administration, DevOps, Network Optimization