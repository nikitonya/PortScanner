from tqdm import tqdm
import socket
from multiprocessing.pool import ThreadPool
from datetime import datetime

HOST = "localhost"
PORTS_COUNT = 2 ** 16
TIMEOUT = 1


def write_for_file(host, port):
    f.write(host + "\t" + str(datetime.now()) + "\t" + str(port) + "\n")


def is_opened_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(TIMEOUT)
        sock.connect((HOST, port))
        write_for_file(HOST, port)
        return port
    except:
        write_for_file(HOST, port)
        return None


if __name__ == '__main__':
    f = open('logi.txt', 'w')
    pool = ThreadPool(3000)
    scanned = list(
        tqdm(pool.imap(is_opened_port, range(0, PORTS_COUNT - 1)), total=PORTS_COUNT - 1, desc=f"Scanning {HOST}"))
    print(f"Open ports are: {[port for port in scanned if port]}")
    f.close()
