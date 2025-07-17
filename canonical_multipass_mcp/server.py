from .multipass_client import MultipassClient


def main():
    client = MultipassClient(server_addr="unix:///var/run/multipass_socket")
    response = client.list()
    print(response)

if __name__ == "__main__":
    main()