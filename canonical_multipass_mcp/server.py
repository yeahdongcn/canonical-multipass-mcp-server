from .multipass_client import MultipassClient


def main():
    client = MultipassClient(server_addr="unix:///var/run/multipass_socket")
    for reply in client.list():
        print(reply)

if __name__ == "__main__":
    main()