import sys
import usb.core
 
var_usb_device = usb.core.find(find_all = True)
print(var_usb_device)
print()
 
for var_dev in var_usb_device:
    var_usb = usb.core.find(idVendor=var_dev.idVendor, idProduct=var_dev.idProduct)
    var_manu = usb.util.get_string(var_usb, 256, var_dev.iManufacturer)
    var_product = usb.util.get_string(var_usb, 256, var_dev.iProduct)
    var_serial = usb.util.get_string(var_usb, 256, var_dev.iSerialNumber)
    var_drv = var_usb.is_kernel_driver_active(0)
 
    var_cfg = var_usb.get_active_configuration()
    var_int = var_cfg[(0,0)].bInterfaceNumber
    
    print("IdVendor: ", var_dev.idVendor, hex(var_dev.idVendor))
    print("IdProduct: ", var_dev.idProduct, hex(var_dev.idProduct))
    print("Manufacturer: ", var_manu)
    print("Product: ", var_product)
    print("Serial: ", var_serial)
    print("Interface #: ", var_int)
    print("Kernel Driver: ", var_drv)
 
    for var_config in var_usb:
        for var_i in var_config:
            for var_e in var_i:
                print("Endpoint Address: ", var_e.bEndpointAddress)
  
    print()

#####
# EOF
