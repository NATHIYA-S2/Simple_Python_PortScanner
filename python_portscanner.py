import socket
import concurrent.futures
import argparse

def check_port(host, port, timeout):
    """
    Checks if a specific port on a given host is open.
    
    :param host: The hostname or IP address to scan.
    :param port: The port number to check.
    :param timeout: Timeout for each connection attempt.
    :return: Port number if open, None otherwise.
    """
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set the timeout for the connection
        sock.settimeout(timeout)
        # Try to connect to the host and port
        result = sock.connect_ex((host, port))
        # Close the socket
        sock.close()
        # If result is 0, the port is open
        if result == 0:
            return port
    except socket.error:
        return None

def scan_ports(host, start_port, end_port, timeout, max_threads):
    """
    Scans a range of ports on a given host to find open ports.
    
    :param host: The hostname or IP address to scan.
    :param start_port: Starting port number.
    :param end_port: Ending port number.
    :param timeout: Timeout for each connection attempt.
    :param max_threads: Number of threads to use for scanning.
    :return: List of open ports.
    """
    open_ports = []

    # Create a ThreadPoolExecutor to handle concurrent port checks
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # List of future objects representing the port checks
        futures = [executor.submit(check_port, host, port, timeout) for port in range(start_port, end_port + 1)]
        
        # Iterate over the completed future objects
        for future in concurrent.futures.as_completed(futures):
            port = future.result()
            # If a port is open, add it to the list
            if port is not None:
                open_ports.append(port)
    
    return open_ports

def main():
    """
    Main function to parse arguments and initiate port scanning.
    """
    parser = argparse.ArgumentParser(description="A simple port scanner.")
    parser.add_argument('host', type=str, help="Host to scan (e.g., 'localhost' or '192.168.1.1')")
    parser.add_argument('start_port', type=int, help="Starting port number")
    parser.add_argument('end_port', type=int, help="Ending port number")
    parser.add_argument('--timeout', type=float, default=1.0, help="Timeout for each connection attempt (default: 1.0s)")
    parser.add_argument('--threads', type=int, default=10, help="Number of concurrent threads (default: 10)")
    
    args = parser.parse_args()

    # Validate port range
    if args.start_port < 1 or args.end_port > 65535 or args.start_port > args.end_port:
        print("Invalid port range. Ports must be between 1 and 65535 and start port must be less than or equal to end port.")
        return

    # Scan ports and get the list of open ports
    open_ports = scan_ports(args.host, args.start_port, args.end_port, args.timeout, args.threads)
    
    # Print the results
    if open_ports:
        print(f"Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
