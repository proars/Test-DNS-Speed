#!/usr/bin/env python3
"""
DNS Resolver Speed Test Tool
Tests the response time of multiple DNS resolvers against popular domains.
"""

import dns.resolver
import time
import concurrent.futures
import json
import argparse
from typing import Dict, List, Optional, Tuple, Set, NamedTuple
from dataclasses import dataclass
from datetime import datetime
import os
import sys
from statistics import mean, median, stdev
import logging
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

# Configuration
DEFAULT_TIMEOUT = 1.0  # seconds for each query
DEFAULT_MAX_RETRIES = 1  # Only retry once
DEFAULT_MAX_WORKERS = 10  # for parallel processing
DEFAULT_MAX_CONSECUTIVE_FAILURES = 3  # Number of consecutive test runs with no successful queries before dropping a resolver
DEFAULT_MIN_SUCCESS_RATE = 0.5  # Minimum success rate (50%) to consider a resolver healthy
DEFAULT_QUICK_FAIL_THRESHOLD = 3  # Number of quick consecutive timeouts before skipping remaining domains
HISTORY_FILE = "dns_test_history.json"  # File to store test history
LOG_FILE = "dns_test.log"  # File to store detailed logs
STATS_FILE = "dns_stats.json"  # File to store historical statistics

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

class DNSResult(NamedTuple):
    """Stores the result of a DNS query."""
    response_time: Optional[float]
    error: Optional[str]
    timestamp: datetime

@dataclass
class Config:
    """Configuration settings for DNS testing."""
    timeout: float = DEFAULT_TIMEOUT
    max_retries: int = DEFAULT_MAX_RETRIES
    max_workers: int = DEFAULT_MAX_WORKERS
    max_consecutive_failures: int = DEFAULT_MAX_CONSECUTIVE_FAILURES
    min_success_rate: float = DEFAULT_MIN_SUCCESS_RATE
    quick_fail_threshold: int = DEFAULT_QUICK_FAIL_THRESHOLD  # Number of quick failures before giving up

@dataclass
class DNSResolver:
    """Represents a DNS resolver with its description and statistics."""
    ip: str
    description: str
    success_rate: float = 1.0
    avg_response_time: float = 0.0
    last_checked: Optional[datetime] = None
    total_queries: int = 0
    successful_queries: int = 0

@dataclass
class Statistics:
    """Statistics for a DNS resolver's performance."""
    min_time: float
    max_time: float
    avg_time: float
    median_time: float
    std_dev: float
    success_rate: float
    total_queries: int
    timestamp: datetime

    @classmethod
    def from_results(cls, results: List[DNSResult]) -> 'Statistics':
        """Create Statistics from a list of DNS results."""
        valid_times = [r.response_time for r in results if r.response_time is not None]
        if not valid_times:
            return cls(0, 0, 0, 0, 0, 0, len(results), datetime.now())
        
        return cls(
            min_time=min(valid_times),
            max_time=max(valid_times),
            avg_time=mean(valid_times),
            median_time=median(valid_times),
            std_dev=stdev(valid_times) if len(valid_times) > 1 else 0,
            success_rate=len(valid_times) / len(results),
            total_queries=len(results),
            timestamp=datetime.now()
        )

# List of DNS resolvers to test
DNS_RESOLVERS = [
    DNSResolver('8.8.8.8', 'Google Public DNS'),
    DNSResolver('1.1.1.1', 'Cloudflare DNS'),
    DNSResolver('9.9.9.9', 'Quad9 DNS'),
    DNSResolver('208.67.222.222', 'OpenDNS'),
    DNSResolver('xxx.xxx.xxx.xxx', 'Custom DNS 1'),
  
]

# Popular domains for testing
TEST_DOMAINS = [
    "example.com", "google.com", "amazon.com", "apple.com", "microsoft.com",
    "facebook.com", "yahoo.com", "wikipedia.org", "github.com", "stackoverflow.com",
    "netflix.com", "reddit.com", "linkedin.com", "bing.com", "quora.com",
    "twitter.com", "instagram.com", "nytimes.com", "cnn.com", "bbc.com",
    "whatsapp.com", "tiktok.com", "paypal.com", "ebay.com", "adobe.com",
    "dropbox.com", "cloudflare.com", "spotify.com", "pinterest.com", "zoom.us",
    "salesforce.com", "wordpress.com", "medium.com", "bitbucket.org", "archive.org",
    "live.com", "msn.com", "weebly.com", "mozilla.org", "oracle.com",
    "booking.com", "airbnb.com", "twitch.tv", "imgur.com", "duckduckgo.com",
    "ikea.com", "hulu.com", "bloomberg.com", "forbes.com", "telegram.org"
]

def test_resolver_speed(resolver: DNSResolver, domain: str, config: Config) -> DNSResult:
    """
    Test the speed of a single DNS query.
    
    Args:
        resolver: DNSResolver object containing IP and description
        domain: Domain name to resolve
        config: Configuration settings
        
    Returns:
        DNSResult containing response time and error information
    """
    dns_resolver = dns.resolver.Resolver()
    dns_resolver.nameservers = [resolver.ip]
    dns_resolver.timeout = config.timeout
    dns_resolver.lifetime = config.timeout
    
    for attempt in range(config.max_retries + 1):
        try:
            start_time = time.time()
            dns_resolver.resolve(domain, "A")
            end_time = time.time()
            return DNSResult(
                response_time=(end_time - start_time) * 1000,  # Convert to milliseconds
                error=None,
                timestamp=datetime.now()
            )
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer) as e:
            return DNSResult(None, str(e), datetime.now())
        except (dns.resolver.Timeout, dns.exception.Timeout) as e:
            if attempt == config.max_retries:
                return DNSResult(None, f"Timeout after {config.max_retries} retries", datetime.now())
            continue
        except Exception as e:
            error_msg = f"Error testing {resolver.ip} with {domain}: {str(e)}"
            logging.error(error_msg)
            return DNSResult(None, error_msg, datetime.now())

# Removing duplicate function definition

def load_test_history() -> Dict[str, int]:
    """Load the test history from file."""
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}

def save_test_history(history: Dict[str, int]) -> None:
    """Save the test history to file."""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(history, f, indent=2)

def parse_arguments() -> Config:
    """Parse command-line arguments and return configuration."""
    parser = argparse.ArgumentParser(
        description="DNS Resolver Speed Test Tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT,
                      help="Timeout for DNS queries in seconds")
    parser.add_argument("--retries", type=int, default=DEFAULT_MAX_RETRIES,
                      help="Maximum number of retries for failed queries")
    parser.add_argument("--workers", type=int, default=DEFAULT_MAX_WORKERS,
                      help="Number of parallel workers")
    parser.add_argument("--max-failures", type=int, default=DEFAULT_MAX_CONSECUTIVE_FAILURES,
                      help="Maximum consecutive failures before dropping resolver")
    parser.add_argument("--min-success-rate", type=float, default=DEFAULT_MIN_SUCCESS_RATE,
                      help="Minimum success rate to consider resolver healthy")
    parser.add_argument("--quick-fail", type=int, default=DEFAULT_QUICK_FAIL_THRESHOLD,
                      help="Number of quick timeouts before skipping remaining domains")
    args = parser.parse_args()
    
    return Config(
        timeout=args.timeout,
        max_retries=args.retries,
        max_workers=args.workers,
        max_consecutive_failures=args.max_failures,
        min_success_rate=args.min_success_rate,
        quick_fail_threshold=args.quick_fail
    )

def should_drop_resolver(ip: str, failure_history: Dict[str, int]) -> bool:
    """Check if a resolver should be dropped based on failure history."""
    return failure_history.get(ip, 0) >= DEFAULT_MAX_CONSECUTIVE_FAILURES

def update_failure_history(ip: str, success: bool, history: Dict[str, int]) -> None:
    """Update the failure history for a resolver."""
    if success:
        history[ip] = 0
    else:
        history[ip] = history.get(ip, 0) + 1

def test_resolver(resolver: DNSResolver, config: Config) -> Tuple[DNSResolver, List[DNSResult]]:
    """
    Test a resolver against all domains and gather results.
    
    Args:
        resolver: DNSResolver object to test
        config: Configuration settings
        
    Returns:
        Tuple of (resolver, list of results)
    """
    results = []
    quick_fail_count = 0
    
    for domain in TEST_DOMAINS:
        # If we've had too many quick failures, skip remaining domains
        if quick_fail_count >= DEFAULT_QUICK_FAIL_THRESHOLD:
            logging.warning(f"Skipping remaining domains for {resolver.ip} due to multiple quick failures")
            # Add empty results for remaining domains
            remaining_domains = len(TEST_DOMAINS) - len(results)
            results.extend([DNSResult(None, "Skipped after multiple failures", datetime.now()) 
                          for _ in range(remaining_domains)])
            break
            
        result = test_resolver_speed(resolver, domain, config)
        results.append(result)
        
        # Check if this was a timeout failure
        if result.error and "timeout" in result.error.lower():
            quick_fail_count += 1
        else:
            quick_fail_count = 0  # Reset counter if we get any non-timeout response
            
    return resolver, results

def calculate_statistics(results: List[DNSResult]) -> Tuple[Optional[float], int]:
    """Calculate average response time and success count from results."""
    valid_times = [r.response_time for r in results if r.response_time is not None]
    success_count = len(valid_times)
    avg_time = mean(valid_times) if valid_times else None
    return avg_time, success_count

def main():
    """Main function to run DNS resolver speed tests."""
    try:
        # Parse command line arguments
        config = parse_arguments()
        
        # Set up rich console for main output
        console = Console()
        progress_console = Console(stderr=True)  # Separate console for progress
        
        # Load test history
        failure_history = load_test_history()
        active_resolvers = [r for r in DNS_RESOLVERS if not should_drop_resolver(r.ip, failure_history)]
        dropped_resolvers = [r for r in DNS_RESOLVERS if should_drop_resolver(r.ip, failure_history)]
        
        if dropped_resolvers:
            console.print("[yellow]⚠️  The following DNS resolvers have been dropped due to consistent failures:[/]")
            for resolver in dropped_resolvers:
                console.print(f"   - {resolver.ip} ({resolver.description}): {failure_history[resolver.ip]} consecutive failures")
            console.print()
        
        all_results: Dict[str, List[DNSResult]] = {}
        resolver_stats: Dict[str, Statistics] = {}
        console_output = []  # Store results for later display
        
        # Test resolvers in parallel with progress bar
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("[cyan]{task.fields[current_resolver]}"),
            TimeElapsedColumn(),
            console=progress_console,
            expand=True,
            refresh_per_second=4  # Slower refresh rate for more stable display
        ) as progress:
            task = progress.add_task(
                "[cyan]Testing DNS resolvers...", 
                total=len(active_resolvers),
                current_resolver="Starting..."
            )
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=config.max_workers) as executor:
                # Submit all tasks first
                futures = {
                    executor.submit(test_resolver, resolver, config): resolver 
                    for resolver in active_resolvers
                }
                
                completed = 0
                for future in concurrent.futures.as_completed(futures):
                    resolver = futures[future]
                    # Update progress before starting to process results
                    progress.update(
                        task,
                        completed=completed,
                        current_resolver=f"Testing {resolver.ip} ({resolver.description})"
                    )
                    progress.refresh()
                    
                    # Now process the results
                    resolver, results = future.result()
                    all_results[resolver.ip] = results
                    completed += 1
                    
                    # Calculate statistics
                    avg_time, success_count = calculate_statistics(results)
                    stats = Statistics.from_results(results)
                    resolver_stats[resolver.ip] = stats
                    
                    # Update failure history
                    success = avg_time is not None and success_count > 0
                    update_failure_history(resolver.ip, success, failure_history)
                    
                    # Store formatted output
                    if success:
                        console_output.append(
                            f"[green]✅ {resolver.ip} ({resolver.description}): "
                            f"Average response time: {avg_time:.2f} ms "
                            f"({success_count}/{len(TEST_DOMAINS)} successful queries)[/]"
                        )
                    else:
                        failure_count = failure_history.get(resolver.ip, 0)
                        remaining_attempts = config.max_consecutive_failures - failure_count
                        console_output.append(
                            f"[red]❌ {resolver.ip} ({resolver.description}): No successful queries "
                            f"(Failed {failure_count} times, {remaining_attempts} attempts remaining)[/]"
                        )
                    
                    progress.advance(task)
        
        # Display results
        console.print("\n")  # Add space after progress bar
        for output in console_output:
            console.print(output)
            console.print()  # Add blank line between results
        
        # Create and display results table
        table = Table(title="DNS Resolver Performance")
        table.add_column("Resolver", style="cyan")
        table.add_column("Min (ms)", justify="right", style="green")
        table.add_column("Max (ms)", justify="right", style="red")
        table.add_column("Avg (ms)", justify="right", style="yellow")
        table.add_column("Success Rate", justify="right", style="blue")
        
        # Sort resolvers by average response time
        sorted_resolvers = sorted(
            resolver_stats.items(),
            key=lambda x: x[1].avg_time if x[1].avg_time > 0 else float('inf')
        )
        
        for ip, stats in sorted_resolvers:
            if stats.avg_time > 0:
                resolver = next(r for r in DNS_RESOLVERS if r.ip == ip)
                table.add_row(
                    f"{ip} ({resolver.description})",
                    f"{stats.min_time:.2f}",
                    f"{stats.max_time:.2f}",
                    f"{stats.avg_time:.2f}",
                    f"{stats.success_rate:.1%}"
                )
        
        console.print("\n")
        console.print(Panel.fit(table, title="DNS Resolver Performance Summary", padding=(1, 2)))
        
        # Save test history
        save_test_history(failure_history)
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Test interrupted by user[/]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/]")
        logging.error(f"Unexpected error: {str(e)}", exc_info=True)
        sys.exit(1)

    # No duplicate progress bar implementations needed - they are already handled in the previous section

if __name__ == '__main__':
    main()
