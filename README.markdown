
# Bayer Contour, Contour NextLink

Both are USB devices, and require a usb library to access.

## Bayer Contour

### lsusb
```
Bus 002 Device 008: ID 1a79:6002 Bayer Health Care LLC

```
Implemented by
[glucodump](https://bitbucket.org/iko/glucodump/src/ce8da3e63217/glucodump/usbcomm.py?at=default).
Includes a block storage device.
Advertises as an HID device.

### syslog
```
Jun  1 11:35:58 paragon kernel: [31023.517052] usb 2-2.2: USB disconnect, device number 6
Jun  1 11:36:53 paragon kernel: [31078.713849] usb 2-2.2: new full-speed USB device number 7 using uhci_hcd
Jun  1 11:36:54 paragon mtp-probe: checking bus 2, device 7: "/sys/devices/pci0000:00/0000:00:11.0/0000:02:00.0/usb2/2-2/2-2.2"
Jun  1 11:36:54 paragon kernel: [31078.946724] generic-usb 0003:1A79:6002.000E: hiddev0,hidraw2: USB HID v10.10 Device [Bayer HealthCare LLC Contour USB] on usb-0000:02:00.0-2.2/input0
Jun  1 11:36:54 paragon mtp-probe: bus: 2, device: 7 was not an MTP device
```

### usb-devices
```
T:  Bus=02 Lev=02 Prnt=03 Port=01 Cnt=02 Dev#=  7 Spd=12  MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=1a79 ProdID=6002 Rev=01.00
S:  Manufacturer=Bayer HealthCare LLC
S:  Product=Contour USB
S:  SerialNumber=0000000002902076
C:  #Ifs= 2 Cfg#= 1 Atr=80 MxPwr=500mA
I:  If#= 0 Alt= 0 #EPs= 2 Cls=03(HID  ) Sub=00 Prot=02 Driver=usbhid
I:  If#= 1 Alt= 0 #EPs= 2 Cls=08(stor.) Sub=06 Prot=50 Driver=usb-storage

```

See [ubuntu_sys_bus_usb.markdown] and [pci_tree.markdown].

```
$ find /dev/hid*
/dev/hidraw0
/dev/hidraw1
bewest@paragon:~/src/decoding-bayer$ 
```

## NextLink
Different device, no block storage


## SOCAT

What's the easiest way to provide socat with an interface to read/write data
from configured USB endpoint?

How to configure endpoint in python, connect it to one of:
  * unix domain socket
  * tcp port
  * [serial device/pty/tty](http://stackoverflow.com/questions/2500420/fake-serial-communication-under-linux)
    [loopback example](http://stackoverflow.com/questions/2192939/software-serial-port-loopback-on-linux?rq=1)

I had thinking to re-use the
[mail.sh](https://github.com/craSH/socat/blob/master/mail.sh),
and
[ftp.sh](https://github.com/craSH/socat/blob/master/ftp.sh) examples
* http://www.tldp.org/LDP/abs/html/ioredirintro.html
* http://stackoverflow.com/questions/11030766/one-virtual-serial-port-with-socat
* http://stackoverflow.com/questions/2174071/how-to-use-dev-ptmx-for-create-a-virtual-serial-port
* http://www.dest-unreach.org/socat/doc/socat.html#EXAMPLES



The reason I'd like to do all this is to connect the usb device to a
server implementation like this:
  * https://github.com/bewest/insulaudit-ssh-tools


## kernel
* http://www.linux-usb.org/USB-guide/x75.html
* http://code.activestate.com/recipes/576834-interrogating-linux-devusbhiddev0-in-python/
* https://www.kernel.org/pub/linux//kernel/people/marcelo/linux-2.4/Documentation/usb/hiddev.txt
* http://www.linux-usb.org/USB-guide/x194.html
* http://www.linux-usb.org/USB-guide/x173.html
* http://www.linuxjournal.com/article/6573?page=0,1 - example usbserial device driver
* https://www.kernel.org/doc/Documentation/usb/proc_usb_info.txt
* https://www.kernel.org/pub/linux//kernel/people/marcelo/linux-2.4/Documentation/usb/hiddev.txt
* http://www.linux-usb.org/gadget/usb.c
* http://www.linux-usb.org/gadget/
* http://www.linux-usb.org/usb.devices.txt
* http://www.linuxjournal.com/article/6434?page=0,1 - usb serial drivers explained

Because the Bayer advertises itself as an `HID` type, linux fails to hook it up
to usbserial for the generic serial adapter?
A simple kernel driver could fix this?

