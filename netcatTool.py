import os

def netcat_tool():
    print("1. Set up a Netcat listener")
    print("   This will start a Netcat listener on a specified port.")
    print("2. Connect to a Netcat listener")
    print("   This will connect to a Netcat listener at a specified IP address and port.")
    print("3. Transfer a file using Netcat")
    print("   This will send a file to a Netcat listener at a specified IP address and port.")
    choice = input("Choose an option: ")

    if choice == '1':
        port = input("Enter the port number for the listener: ")
        os.system(f"nc -lvp {port}")
    elif choice == '2':
        ip = input("Enter the IP address to connect to: ")
        port = input("Enter the port number to connect to: ")
        os.system(f"nc {ip} {port}")
    elif choice == '3':
        ip = input("Enter the IP address to send the file to: ")
        port = input("Enter the port number to send the file to: ")
        file_path = input("Enter the path to the file to send: ")
        os.system(f"nc {ip} {port} < {file_path}")
    else:
        print("Invalid option")

if __name__ == "__main__":
    netcat_tool()