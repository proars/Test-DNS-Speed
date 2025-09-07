# DNS Speed Test Tool 🚀

A Python-based utility for measuring and comparing DNS resolver performance across multiple providers.

## Overview

This tool helps system administrators, network engineers, and developers benchmark different DNS resolvers by measuring their response times across popular domains. It provides accurate metrics to help you choose the fastest DNS resolver for your infrastructure.

## Features

- 🔍 Tests multiple DNS resolvers simultaneously
- 📊 Measures response times in milliseconds
- 📈 Calculates average response times
- 🎯 Tests against popular domains
- 📋 Provides sorted results from fastest to slowest
- ⚠️ Handles failed queries gracefully

## Requirements

- Python 3.x
- `dnspython` library

## Installation

1. Clone this repository:

```bash
git clone https://github.com/proars/Test-DNS-Speed.git
cd Test-DNS-Speed
```

1. Install the required dependency:

```bash
pip install dnspython
```

## Usage

1. Run the script:

```bash
python main.py
```

The tool will test each configured DNS resolver against a list of popular domains and display:

- Average response times for each resolver
- Success rate of queries
- Sorted results from fastest to slowest

## Configuration

The script includes default DNS resolvers:

- Google Public DNS (8.8.8.8)
- Custom DNS resolvers can be added in the `dns_resolvers` list

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
