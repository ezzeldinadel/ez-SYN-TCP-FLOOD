#!/usr/bin/env python3

import logging
import threading

from scapy.all import *

FORMAT = '%(asctime)s - %(name)s %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT)

logger = logging.getLogger("SYN-flood-stats")
logger.setLevel(logging.DEBUG)


EXIT_SIGNAL = False


def _on_syn_sent(pkt):
    print(pkt)


def _on_ack_rcvd(pkt):
    pass


def _sniff(filter_str, callback):

    logger.info(f"Sniff launched for filter: {filter_str}")

    while not EXIT_SIGNAL:
        sniff(filter=filter_str, prn=callback, timeout=2)


def _main():

    logger.info("Start sniffing")

    try:
        pass
    except KeyboardInterrupt:
        logger.info("Keyboard signal received")

    logger.info("Stopped sniffing")


def _launch():

    global EXIT_SIGNAL

    dst = "103.117.132.245"

    threads = [
        # threading.Thread(target=_sniff, args=(f"dst {dst} and tcp[13] & 2 != 0", _on_syn_sent)),
        threading.Thread(target=_sniff, args=(f"src {dst} and tcp[13] & 16 != 0", _on_syn_sent)),
        # threading.Thread(target=_sniff, args=(f"tcp and src {dst}", _on_packet)),
    ]

    for t in threads:
        t.start()

    while True:
        try:
            for t in threads:
                t.join()
            break
        except KeyboardInterrupt:
            EXIT_SIGNAL = True
            logger.info("Quit signal received...")

    logger.info("Finished")


if __name__ == "__main__":
    _launch()


