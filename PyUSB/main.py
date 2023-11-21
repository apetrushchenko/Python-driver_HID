
import usb.core
import usb.util

from time import sleep
import random
import sys
import time

# find our device

#dev = usb.core.find(idVendor=0x03f0  , idProduct=0x0024)
dev = usb.core.find(idVendor=0x0483, idProduct=0x5750)
vid = dev.idVendor
pid = dev.idProduct
prt = dev.parent

# was it found?
if dev is None:
    raise ValueError('Device not found')

#ep = dev[0].interfaces()[1].endpoints()[0]

i = 0 #dev[0].interfaces()[0].bInterfaceNumber

dev.reset()

if dev.is_kernel_driver_active(i):
    try:
        dev.detach_kernel_driver(i)
    except usb.core.USBError as e:
        sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(i, str(e)))

# set the active configuration. With no arguments, the first
# configuration will be the active o1231ne
dev.set_configuration()

# get an endpoint instance
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None


d = [random.randint(0, 1) for _ in range(4)]
print("Sended: [{}]: {}".format(ep.write(d),d))
sleep(0.3)


sended = 0
d = [random.randint(0, 1) for _ in range(64)]
timestamp = int(time.time())

for _ in range(100000):
        sended += ep.write(d)

timestamp2 = int(time.time())
print("Speed: {} Bps".format(sended/(timestamp2-timestamp)))

# Зчитайте дані з пристрою
data = dev.read(endpoint_address, length, timeout)

