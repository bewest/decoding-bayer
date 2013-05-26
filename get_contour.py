import usb.core
import usb.util
import sys
import time
interface = 0

# Bayer
# dev = usb.core.find(idVendor=0x1a79, idProduct=0x6200)
dev = usb.core.find(idVendor=0x1a79, idProduct=0x6002)
 
def main():

        if dev is None:
            print "device not found"

        else:
          print "device found"
          if dev.is_kernel_driver_active(interface) is True:
            print "but we need to detach kernel driver"
            dev.detach_kernel_driver(interface)
            print "claiming device"
            usb.util.claim_interface(dev, interface)


          for cfg in dev:
            for i in cfg:
              for end in i:
                print "end point", end
                #end.read(64)
                time.sleep(2)
          print "release claimed interface"
          usb.util.release_interface(dev, interface)
          print "now attaching the kernel driver again"
          dev.attach_kernel_driver(interface)
          print "all done"
          return 0

if __name__ == '__main__':
    main()

######
# EOF
