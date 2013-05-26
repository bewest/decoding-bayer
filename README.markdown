
# Bayer Contour, Contour NextLink

Both are USB devices, and require a usb library to access.

## Bayer Contour

Implemented by
[glucodump](https://bitbucket.org/iko/glucodump/src/ce8da3e63217/glucodump/usbcomm.py?at=default).
Includes a block storage device.

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



