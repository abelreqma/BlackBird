import socket
import argparse

def scan_ports(host, start_port, end_port):
    print(f"Scanning ports on {host} from {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a timeout for the connection attempt

        try:
            sock.connect((host, port))
            print(f"Port {port} is open")
        except socket.error:
            pass
        finally:
            sock.close()

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", help="Target host to scan")
    parser.add_argument("start_port", type=int, help="Start port for the scan")
    parser.add_argument("end_port", type=int, help="End port for the scan")

    args = parser.parse_args()
    host = args.host
    start_port = args.start_port
    end_port = args.end_port

    scan_ports(host, start_port, end_port)

if __name__ == "__main__":
    main()
