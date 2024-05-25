import socket


def location_with_ip():
    try:
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        print(f"Internal IPv4 Address for {hostname}: {ipv4_address}")
    except socket.gaierror:
        print("There was an error resolving the hostname.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
