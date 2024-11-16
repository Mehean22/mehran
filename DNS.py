import socket

def get_ip_by_domain(domain):
    # ایجاد یک سوکت UDP
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # سعی در دریافت IP از دامنه
    try:
        # با استفاده از تابع getaddrinfo برای دریافت اطلاعات مربوط به دامنه
        addr_info = socket.getaddrinfo(domain, None)
        ip_addresses = []

        for info in addr_info:
            ip_addresses.append(info[4][0])  # فقط IP را از اطلاعات بگیریم

        return ip_addresses
    except socket.gaierror:
        return None
    finally:
        udp_socket.close()  # بستن سوکت

# استفاده از تابع
domain = 'basalam.com'  # دامنه‌ای که می‌خواهید IP آن را بگیرید
ips = get_ip_by_domain(domain)

if ips:
    print(f"IP addresses for {domain}: {', '.join(ips)}")
else:
    print(f"Could not find IP addresses for {domain}.")