SIMPLE PORT SCANNER IN PYTHON

A basic port scanner written in Python to identify open ports on a networked device. This tool uses multi-threading to efficiently scan a range of ports and can be customized with various command-line arguments.

Features

- Scans a range of ports on a specified host.
- Uses multi-threading to speed up the scanning process.
- Customizable timeout and thread count.
- Simple command-line interface.

Prerequisites

- Python 3.x
- No additional libraries are required beyond Python’s standard library.

Installation

1. Clone the Repository:

   ```sh
   git clone https://github.com/NATHIYA-S2/Simple_Python_PortScanner.git
   ```

3. Navigate to the Directory:

   ```sh
   cd Simple_Python_PortScanner
   ```

Usage

Run the port scanner from the command line with the following syntax:

sh
python python_portscanner.py <host> <start_port> <end_port> [--timeout TIMEOUT] [--threads THREADS]


Arguments:

- `<host>`: The IP address or hostname of the target machine (e.g., `localhost` or `192.168.1.1`).
- `<start_port>`: The starting port number to scan (integer).
- `<end_port>`: The ending port number to scan (integer).
- `--timeout TIMEOUT`: Optional. The timeout for each connection attempt in seconds (default is `1.0`).
- `--threads THREADS`: Optional. Number of concurrent threads to use (default is `10`).

Example Command:

To scan ports 1 through 1024 on `192.168.1.1` with a timeout of 2 seconds and 5 threads:

```sh
python port_scanner.py 192.168.1.1 1 1024 --timeout 2 --threads 5
```

Script Details

`check_port(host, port, timeout)`

Checks if a specific port on a given host is open. Returns the port number if it is open, otherwise returns `None`.

`scan_ports(host, start_port, end_port, timeout, max_threads)`

Scans a range of ports on the specified host. Uses multi-threading to speed up the scanning process. Returns a list of open ports.

`main()`

Parses command-line arguments, validates input, and initiates the port scanning process. Outputs the list of open ports or a message if no ports are open.

Example Output

If open ports are found:

```
Open ports: 22, 80, 443
```

If no open ports are found:

```
No open ports
