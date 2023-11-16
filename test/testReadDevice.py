import struct
import threading

import usb.core
import usb.util

from HidDeviceData import HidDeviceData
from HidReport import HidReport
from utils import Utils

# ctypes.CDLL('[my path to the DLL]\\hidapi.dll')

class hidTest:

    def __init__(self):

        self.timer_interval = 10

        self.__report_length = 64

        self.__device = None
        self.__devices = None
        self._device_vid = 1155
        self._device_pid = 22352
        self._v1_pid = 22351
        self._c1_pid = 22352
        self._cms_pid = 22353
        self._ga_pid = 22354
        self.product_array_pid = [ self._v1_pid, self._c1_pid, self._cms_pid, self._ga_pid]
        self.product_array_nm  = [ "V1", "C1", "CMS", "GLA"]
        self.__attached = False

        self.__report_id_read = 1
        self.__report_id_write = 2
        self.__test_tim = 0

        self.__page = 66
        self.__buffer_usb_rx = None
        self.__buffer_usb_tx = None
        self.__output0_bit = 0
        self.__output1_bit = 0
        self.__output2_bit = 0
        self.__bit0_res = 0xFE
        self.__bit1_res = 0xFD
        self.__bit2_res = 0xFB
        self.__bit3_res = 0xF7
        self.__bit4_res = 0xEF
        self.__bit5_res = 0xDF
        self.__bit6_res = 0xBF
        self.__bit7_res = 0x7F
        self.__bit0_set = 0x01
        self.__bit1_set = 0x02
        self.__bit2_set = 0x04
        self.__bit3_set = 0x08
        self.__bit4_set = 0x10
        self.__bit5_set = 0x20
        self.__bit6_set = 0x40
        self.__bit7_set = 0x80
    
        self.__reg_1 = 1
        self.__reg_2 = 2
        self.__reg_3 = 3
        self.__reg_4 = 4
        self.__reg_5 = 5
        self.__reg_6 = 6
        self.__reg_7 = 7
        self.__reg_8 = 8
        self.__reg_9 = 9
        self.__reg_10 = 10
        self.__reg_11 = 11
        self.__reg_12 = 12
        self.__reg_13 = 13
        self.__reg_14 = 14
        self.__reg_15 = 15
        self.__reg_16 = 16
        self.__reg_17 = 17
        self.__reg_30 = 30
        self.__reg_31 = 31
        self.__reg_32 = 32
        self.__reg_33 = 33
        self.__reg_34 = 34
        self.__reg_35 = 35
        self.__reg_36 = 36
        self.__reg_37 = 37
        self.__reg_38 = 38
        self.__reg_39 = 39
        self.__reg_40 = 40
        self.__reg_41 = 41
        self.__reg_42 = 42
        self.__reg_43 = 43
        self.__reg_44 = 44
        self.__reg_45 = 45
        self.__reg_46 = 46
        self.__reg_47 = 47
        self.__reg_48 = 48
        self.__reg_49 = 49
        self.__reg_50 = 50
        self.__reg_51 = 51
        self.__reg_52 = 55
        self.__reg_53 = 57
        self.__reg_54 = 59
        self.__reg_59 = 59
        self.__reg_60 = 60
        self.__on = 0xFFFF
        self.__off = 0
        self.__timer = None

    #@property
    def get_Device(self)->None:
        return self.__device

    #@property.setter
    def set_Device(self, value):
        self.__device = value

    #@property
    def get_Attached(self)->bool:
        return self.__attached

    #@property.setter
    def set_Attached(self, value):
        self.__attached  = value
        if( self.__attached ):
            self.__timer.Start()
        else:
            self.__temer.Stop()

    def ReadDevice(self) -> None:

        self.__devices = (Utils.newArray(4, None))

        counter = 0
        for prod_id in self.product_array_pid:

            self.__devices[ counter ] = usb.core.find(self._device_vid, prod_id )

            if str(self.__devices[counter]) is not None:
                self.__devNN = self.product_array_nm[counter]
                self.set_Device( self.__devices[ counter ])

            print("HID.ReadDevice(): dev = " + str(counter)+", vid="+str(self.__devices[counter])+", pid=" + str(prod_id), str(self.__devices[counter]))
            counter = counter + 1

        return self.__devices

    def start(self):
        self.__timer = threading.Timer(self.timer_interval, self.timer_OnTick)
        self.__timer.start()
        self.__attached = True

    def stop(self):
        self.__attached = False

    def HID_Send_CMD_TopLight(self, value ):
        self.HID_Send_Comand( self.__reg_2, int(value))

    def HID_Send_CMD_BackLight(self, value ):
        self.HID_Send_Comand( self.__reg_3, int(value))

    def HID_Send_CMD_VibrationTable(self, value ):
        #self.HID_Send_Comand( self.__reg_5, int(value))
        pass

    def HID_Send_CMD_Frequency(self, value ):
        #self.HID_Send_Comand( self.__reg_17, int(value))
        pass

    def HID_Send_Comand(self, comand: int, data: int) -> None:

        conv_array = Utils.newArrayOfBytes(4, 0)
        conv_array = (data).to_bytes(4, byteorder="little")

        self.__buffer_usb_rx = Utils.newArrayOfBytes(self.__page, 0)
        self.__buffer_usb_rx = Utils.newArrayOfBytes(self.__page, 0)

        self.__buffer_usb_rx[self.__reg_40] = (0)
        self.__buffer_usb_rx[50] = (0)

        swichVal = comand
        if (swichVal == self.__reg_1):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[1] = conv_array[0]
            self.__buffer_usb_rx[2] = conv_array[1]
        elif (swichVal == self.__reg_2):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[3] = conv_array[0]
            self.__buffer_usb_rx[4] = conv_array[1]
        elif (swichVal == self.__reg_3):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[5] = conv_array[0]
            self.__buffer_usb_rx[6] = conv_array[1]
        elif (swichVal == self.__reg_4):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[7] = conv_array[0]
            self.__buffer_usb_rx[8] = conv_array[1]
        elif (swichVal == self.__reg_5):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[9] = conv_array[0]
            self.__buffer_usb_rx[10] = conv_array[1]
        elif (swichVal == self.__reg_6):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[11] = conv_array[0]
            self.__buffer_usb_rx[12] = conv_array[1]
        elif (swichVal == self.__reg_7):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[13] = conv_array[0]
            self.__buffer_usb_rx[14] = conv_array[1]
        elif (swichVal == self.__reg_8):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[15] = conv_array[0]
            self.__buffer_usb_rx[16] = conv_array[1]
        elif (swichVal == self.__reg_9):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[17] = conv_array[0]
            self.__buffer_usb_rx[18] = conv_array[1]
        elif (swichVal == self.__reg_10):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[19] = conv_array[0]
            self.__buffer_usb_rx[20] = conv_array[1]
        elif (swichVal == self.__reg_11):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[21] = conv_array[0]
            self.__buffer_usb_rx[22] = conv_array[1]
        elif (swichVal == self.__reg_12):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[23] = conv_array[0]
            self.__buffer_usb_rx[24] = conv_array[1]
        elif (swichVal == self.__reg_13):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[25] = conv_array[0]
            self.__buffer_usb_rx[26] = conv_array[1]
        elif (swichVal == self.__reg_14):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[27] = conv_array[0]
            self.__buffer_usb_rx[28] = conv_array[1]
        elif (swichVal == self.__reg_15):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[29] = conv_array[0]
            self.__buffer_usb_rx[30] = conv_array[1]
        elif (swichVal == self.__reg_16):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[self.__reg_45] = conv_array[0]
            self.__buffer_usb_rx[self.__reg_46] = conv_array[1]
        elif (swichVal == self.__reg_17):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[self.__reg_47] = conv_array[0]
            self.__buffer_usb_rx[self.__reg_48] = conv_array[1]

        elif (swichVal == self.__reg_33):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[self.__reg_33] = conv_array[0]
        elif (swichVal == self.__reg_34):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[self.__reg_34] = conv_array[0]
        elif (swichVal == self.__reg_35):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[self.__reg_35] = conv_array[0]

        elif (swichVal == self.__reg_36):
            conv_array = (data).to_bytes(4, byteorder="little")
            self.__buffer_usb_rx[self.__reg_36] = conv_array[0]

        elif (swichVal == self.__reg_37):
            self.__buffer_usb_rx[self.__reg_37] = conv_array[0]

        elif (swichVal == self.__reg_38):
            self.__buffer_usb_rx[self.__reg_38] = conv_array[0]

        elif (swichVal == self.__reg_39):
            self.__buffer_usb_rx[self.__reg_39] = conv_array[0]

        elif (swichVal == self.__reg_40):
            self.__buffer_usb_rx[self.__reg_40] = conv_array[0]

        elif (swichVal == self.__reg_41):
            self.__buffer_usb_rx[self.__reg_41] = conv_array[0]

        elif (swichVal == self.__reg_42):
            self.__buffer_usb_rx[self.__reg_42] = conv_array[0]

        elif (swichVal == self.__reg_43):
            self.__buffer_usb_rx[self.__reg_43] = conv_array[0]

        elif (swichVal == self.__reg_44):
            self.__buffer_usb_rx[self.__reg_44] = conv_array[0]

        elif (swichVal == self.__reg_47):
            self.__buffer_usb_rx[self.__reg_47] = conv_array[0]

        elif (swichVal == self.__reg_48):
            self.__buffer_usb_rx[self.__reg_48] = conv_array[0]

        elif (swichVal == self.__reg_49):
            self.__buffer_usb_rx[self.__reg_49] = conv_array[0]


        """
        elif (swichVal == self.__reg_30):
            self.__buffer_usb_rx[self.__reg_30] = (.ToByte(self.__output0_bit)  # error )
        elif (swichVal == self.__reg_31):
            self.__buffer_usb_rx[self.__reg_31] = (.ToByte(self.__output1_bit)  # error )
        elif (swichVal == self.__reg_32):
            self.__buffer_usb_rx[self.__reg_32] = (.ToByte(self.__output2_bit)  # error )
        """


        """   
        elif (swichVal == self.__reg_50):
        self.__buffer_usb_rx[50] = conv_array[0]
        conv_array = (.ERROR: ToInt32(?)
        int
        not supported in Python).to_bytes(4, byteorder="little")
        self.__buffer_usb_rx[51] = conv_array[0]
        self.__buffer_usb_rx[52] = conv_array[1]
        self.__buffer_usb_rx[53] = conv_array[2]
        self.__buffer_usb_rx[54] = conv_array[3]
        if (numericUpDown12.Value > numericUpDown13.Value):
            numericUpDown12.Value = (numericUpDown13.Value)
        conv_array = (.ERROR: ToInt32(?)
        int
        not supported in Python).to_bytes(4, byteorder="little")
        self.__buffer_usb_rx[55] = conv_array[0]
        self.__buffer_usb_rx[56] = conv_array[1]
        if (numericUpDown13.Value < numericUpDown12.Value):
            numericUpDown13.Value = (numericUpDown12.Value)
        conv_array = (.ERROR: ToInt32(?)
        int
        not supported in Python).to_bytes(4, byteorder="little")
        self.__buffer_usb_rx[57] = conv_array[0]
        self.__buffer_usb_rx[58] = conv_array[1]
        conv_array = (.ERROR: ToInt32(?)
        int
        not supported in Python).to_bytes(4, byteorder="little")
        self.__buffer_usb_rx[59] = conv_array[0]
        self.__buffer_usb_rx[60] = conv_array[1]
        self.__buffer_usb_rx[61] = (.ToByte(comboBox1.Text)  # error )
        self.__hID_Write(self.__buffer_usb_rx)
        """


    def __hID_Write(self, buffer: bytearray) -> None:
        buffer[0] = (2)
        self.__device.WriteReport( HidReport( self.__report_length, HidDeviceData(  buffer, HidDeviceData.ReadStatus.SUCCESS)))
        return buffer

    def timer_OnTick(self) -> None:
        # **** INPUT *****////
        if (len(self.__buffer_usb_tx) > 60):
            pass

    @staticmethod
    def onReport(self, report: HidReport) -> None:
        """ Читати USB буфер
        Args:
            report(HidReport):
        """
        if (self.__attached):
            self.__buffer_usb_tx =  report.Data

    @staticmethod
    def deviceAttachedHandler(self) -> None:
        """ Включити Подію читання USB """
        self.__attached = True
        self.__device.ReadReport(self.OnReport)  # error
    
    
    @staticmethod
    def deviceRemovedHandler(self,a=2, b=1) -> None:
        """ USB відключено(помилка) """
        self.__attached = False
    
objDev = None

try:

    objDev = hidTest()

    objDev.start()



    devices = objDev.ReadDevice()

    print("Read detected device & try connect to him with product_id from correct list: ")

    for device in devices:
        print( "Device {0}", device )
        if str(device) != '[]' :
           if( objDev._device_vid == device[0]['vendor_id'] ) :
                for  product_id in product_array :
                    res = "Ok"
                    try:
                        device.Open()
                        res = "Ok"

                    except Exception as AnyError:
                        print( AnyError )
                        res = "Fail, error:" + str(AnyError)


                    finally:
                        print("Opening "+str(device[0]['vendor_id'])+","+str(product_id)+" result =>" +str(res))

    tmpDev = objDev.get_Device()
    if str(tmpDev) != "[]":
        vendor_idx = tmpDev[0]['vendor_id']
        product_idx = tmpDev[0]['product_id']
        device.open()

        #hid.Device(vendor_id, product_id)().Inserted += (objDev.deviceAttachedHandler)
        #hid.Device(vendor_id, product_id)().Removed += (objDev.deviceRemoveHandler)
        #hid.Device(vendor_id, product_id)().MonitorDeviceEvents = (True)
        #hid.Device(vendor_id, product_id)().ReadReport(objDev.OnReport)

    objDev.start()



    value = input( "Top light, set value as 0=500 =>"    )
    objDev.HID_Send_CMD_TopLight(value)
    value = input( "Back light, set value as 0=500 =>"   )
    objDev.HID_Send_CMD_TopLight(value)
    value = input( "VibroTablet, set value as 0=500 =>"  )
    #objDev.HID_Send_CMD_TopLight(value)
    value = input( "Frecency, set value as 0=500 =>"     )
    #objDev.HID_Send_CMD_TopLight(value)

except Exception as AnyError:
    print( f"Unexpected {AnyError} " )

finally:
    if objDev is None:
        pass
    else:
        objDev.stop()

