import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    val = input("Enter an IP address: ")
    if is_valid_ip(val):
        print(f"{val} is a valid IP address.")
    else:
        print(f"{val} is NOT a valid IP address.")
