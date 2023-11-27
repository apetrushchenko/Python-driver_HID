import threading
import sys

import usb.core
import usb.util

from IControlBox import IControl
from IHIDBase import IHIDBase

#from HidDeviceData import HidDeviceData
#from HidReport import HidReport


from Utils import Utils
from src.HIDConst import HID_CONST
from src.IMotor import IMotor


class HIDBase(IHIDBase):


    def __init__(self, control : IControl , motors : IMotor = None):

        self.__buffer_usb_rx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)  # array/buffer for write to HID
        self.__buffer_usb_tx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)

        self.__control = control
        self.__motors  = motors

        if motors == None:
            self.__motor = None
        else:
            motors.set_buffer( self.__buffer_usb_rx )
            self._motor = motors


        self.timer_interval = 100

        self.__device = None  # our divice
        self.__devices = None # list of anabled devices
        self.endpoint = None  # this param for divice.Write( endpoint, ... )

        self.__attached = False



        self.__timer = None


    def open(self):
        # dev = usb.core.find(idVendor=0x03f0  , idProduct=0x0024)
        dev = usb.core.find(idVendor=0x0483, idProduct=0x5750)
        vid = dev.idVendor
        pid = dev.idProduct
        prt = dev.parent

        # was it found?
        if dev is None:
            raise ValueError('Device not found')

        # ep = dev[0].interfaces()[1].endpoints()[0]

        i = 0  # i = dev[0].interfaces()[0].bInterfaceNumber

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
        intf = cfg[(0, 0)]

        ep = usb.util.find_descriptor(
            intf,
            # match the first OUT endpoint
            custom_match= \
                lambda e: \
                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                    usb.util.ENDPOINT_OUT)

        assert ep is not None

        self.__device = dev
        self.endpoint = ep
        #  d = [random.randint(0, 1) for _ in range(4)]

        # print("Sended: [{}]: {}".format(ep.write(d), d))
        # sleep(0.3)

    # @property
    def get_Device(self) -> None:
        return self.__device

    # @property.setter
    def set_Device(self, value):
        self.__device = value

    # @property
    def get_Attached(self) -> bool:
        return self.__attached

    # @property.setter
    def set_Attached(self, value):
        self.__attached = value
        if (self.__attached):
            self.__timer.Start()
        else:
            self.__temer.Stop()

    def ReadDevice(self) -> None:

        self.__devices = (Utils.newArray(4, None))

        counter = 0
        for prod_id in self.product_array_pid:

            self.__devices[counter] = usb.core.find(self._device_vid, prod_id)

            if str(self.__devices[counter]) is not None:
                self.__devNN = self.product_array_nm[counter]
                self.set_Device(self.__devices[counter])

            print("HID.ReadDevice(): dev = " + str(counter) + ", vid=" + str(self.__devices[counter]) + ", pid=" + str(
                prod_id), str(self.__devices[counter]))
            counter = counter + 1

        return self.__devices

    def start(self):
        self.__timer = threading.Timer(self.timer_interval, self.timer_OnTick)
        self.__timer.start()
        self.__attached = True

    def stop(self):
        self.__attached = False
        self.HID_Send_Comand(0, 0)

    def HID_Send_Comand(self, comand: int, data: int) -> None:
        # conv_array = Utils.newArrayOfBytes(4, 0)
        conv_array = data.to_bytes(4, "little")
        control = int.from_bytes(conv_array, "little")

        if (comand == 0):
            self.__buffer_usb_rx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)
            self.__buffer_usb_tx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)

        self.__buffer_usb_rx[HID_CONST.REG_40] = (0)
        self.__buffer_usb_rx[50] = (0)

        swichVal = comand
        if (swichVal == 0):
            self.__buffer_usb_rx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)
            self.__buffer_usb_tx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)
            pass
        elif (swichVal == HID_CONST.REG_1):
            self.__buffer_usb_rx[1] = conv_array[0]
            self.__buffer_usb_rx[2] = conv_array[1]
        elif (swichVal == HID_CONST.REG_2):
            self.__buffer_usb_rx[3] = conv_array[0]
            self.__buffer_usb_rx[4] = conv_array[1]
        elif (swichVal == HID_CONST.REG_3):
            self.__buffer_usb_rx[5] = conv_array[0]
            self.__buffer_usb_rx[6] = conv_array[1]
        elif (swichVal == HID_CONST.REG_4):
            self.__buffer_usb_rx[7] = conv_array[0]
            self.__buffer_usb_rx[8] = conv_array[1]
        elif (swichVal == HID_CONST.REG_5):
            self.__buffer_usb_rx[9] = conv_array[0]
            self.__buffer_usb_rx[10] = conv_array[1]
        elif (swichVal == HID_CONST.REG_6):
            self.__buffer_usb_rx[11] = conv_array[0]
            self.__buffer_usb_rx[12] = conv_array[1]
        elif (swichVal == HID_CONST.REG_7):
            self.__buffer_usb_rx[13] = conv_array[0]
            self.__buffer_usb_rx[14] = conv_array[1]
        elif (swichVal == HID_CONST.REG_8):
            self.__buffer_usb_rx[15] = conv_array[0]
            self.__buffer_usb_rx[16] = conv_array[1]
        elif (swichVal == HID_CONST.REG_9):
            self.__buffer_usb_rx[17] = conv_array[0]
            self.__buffer_usb_rx[18] = conv_array[1]
        elif (swichVal == HID_CONST.REG_10):
            self.__buffer_usb_rx[19] = conv_array[0]
            self.__buffer_usb_rx[20] = conv_array[1]
        elif (swichVal == HID_CONST.REG_11):
            self.__buffer_usb_rx[21] = conv_array[0]
            self.__buffer_usb_rx[22] = conv_array[1]
        elif (swichVal == HID_CONST.REG_12):
            self.__buffer_usb_rx[23] = conv_array[0]
            self.__buffer_usb_rx[24] = conv_array[1]
        elif (swichVal == HID_CONST.REG_13):
            self.__buffer_usb_rx[25] = conv_array[0]
            self.__buffer_usb_rx[26] = conv_array[1]
        elif (swichVal == HID_CONST.REG_14):
            self.__buffer_usb_rx[27] = conv_array[0]
            self.__buffer_usb_rx[28] = conv_array[1]
        elif (swichVal == HID_CONST.REG_15):
            self.__buffer_usb_rx[29] = conv_array[0]
            self.__buffer_usb_rx[30] = conv_array[1]
        elif (swichVal == HID_CONST.REG_16):
            self.__buffer_usb_rx[HID_CONST.REG_45] = conv_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_46] = conv_array[1]
        elif (swichVal == HID_CONST.REG_17):
            self.__buffer_usb_rx[HID_CONST.REG_47] = conv_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_48] = conv_array[1]

        elif (swichVal == HID_CONST.REG_33):
            self.__buffer_usb_rx[HID_CONST.REG_33] = conv_array[0]
        elif (swichVal == HID_CONST.REG_34):
            self.__buffer_usb_rx[HID_CONST.REG_34] = conv_array[0]
        elif (swichVal == HID_CONST.REG_35):
            self.__buffer_usb_rx[HID_CONST.REG_35] = conv_array[0]

        elif (swichVal == HID_CONST.REG_36):
            self.__buffer_usb_rx[HID_CONST.REG_36] = conv_array[0]

        elif (swichVal == HID_CONST.REG_37):
            self.__buffer_usb_rx[HID_CONST.REG_37] = conv_array[0]

        elif (swichVal == HID_CONST.REG_38):
            self.__buffer_usb_rx[HID_CONST.REG_38] = conv_array[0]

        elif (swichVal == HID_CONST.REG_39):
            self.__buffer_usb_rx[HID_CONST.REG_39] = conv_array[0]

        elif (swichVal == HID_CONST.REG_40):
            self.__buffer_usb_rx[HID_CONST.REG_40] = conv_array[0]

        elif (swichVal == HID_CONST.REG_41):
            self.__buffer_usb_rx[HID_CONST.REG_41] = conv_array[0]

        elif (swichVal == HID_CONST.REG_42):
            self.__buffer_usb_rx[HID_CONST.REG_42] = conv_array[0]

        elif (swichVal == HID_CONST.REG_43):
            self.__buffer_usb_rx[HID_CONST.REG_43] = conv_array[0]

        elif (swichVal == HID_CONST.REG_44):
            self.__buffer_usb_rx[HID_CONST.REG_44] = conv_array[0]

        elif (swichVal == HID_CONST.REG_47):
            self.__buffer_usb_rx[HID_CONST.REG_47] = conv_array[0]

        elif (swichVal == HID_CONST.REG_48):
            self.__buffer_usb_rx[HID_CONST.REG_48] = conv_array[0]

        elif (swichVal == HID_CONST.REG_49):
            self.__buffer_usb_rx[HID_CONST.REG_49] = conv_array[0]

        # motors *****************************************************************************************************
        elif (swichVal == HID_CONST.REG_50):

            self.__buffer_usb_rx[HID_CONST.REG_50] = conv_array[0]


            position_array = (self.__motors.position if self.__motors is not None else 0).to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_51] = position_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_52] = position_array[1]
            self.__buffer_usb_rx[HID_CONST.REG_53] = position_array[2]
            self.__buffer_usb_rx[HID_CONST.REG_54] = position_array[3]

            # set speed max
            spin_max_array = (self.__motors.speed_max if self.__motors is not None else 0).to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_55] = spin_max_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_56] = spin_max_array[1]

            # set speed minJ
            spin_min_array = (self.__motors.speed_min if self.__motors is not None else 0).to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_57] = spin_min_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_58] = spin_min_array[1]

            # set acceler
            acceler_array = (self.__motors.ACC if self.__motors is not None else 0).to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_59] = acceler_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_60] = acceler_array[1]

            # set number of motor
            motor_id_array = self.__curr_motor_id.to_bytes(4, "little")
            mn = motor_id_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_61] = motor_id_array[0]

        self.__hID_Write(self.__buffer_usb_rx)


    def __hID_Write(self, buffer: bytearray) -> None:
        buffer[0] = (2)
        # tmt = HidReport(self.__report_length, HidDeviceData(buffer, HidDeviceData.ReadStatus.SUCCESS))
        # self.__device.write( HidReport( self.__report_length, HidDeviceData(  buffer, HidDeviceData.ReadStatus.SUCCESS)))
        self.__device.write(self.endpoint, buffer)
        return buffer

    def timer_OnTick(self) -> None:
        if (len(self.__buffer_usb_tx) > 60):
            pass

    @staticmethod
    def onReport(self, report) -> None:
        """ Читати USB буфер
        Args:
            report(HidReport):
        """
        if (self.__attached):
            self.__buffer_usb_tx = report.Data

    @staticmethod
    def deviceAttachedHandler(self) -> None:
        """ Включити Подію читання USB """
        self.__attached = True
        self.__device.ReadReport(self.OnReport)  # error

    @staticmethod
    def deviceRemovedHandler(self, a=2, b=1) -> None:
        """ USB відключено(помилка) """
        self.__attached = False

    # call IMotors *****************************************************************************************************

    # implementation methods  IControl *******************************************************************************
    def HID_Send_CMD_TopLight(self, value):
        if (self.__control) :
            cmd_data = self.__control.set_TopLigth( value )
            self.HID_Send_Comand( cmd_data[0], cmd_data[1] )

    def HID_Send_CMD_BackLight(self, value):
        if (self.__control):
            cmd_data = self.__control.set_BackLigth(value)
            self.HID_Send_Comand( cmd_data[0], cmd_data[1] )


    def HID_Send_CMD_CoaxLight(self, value):
        if (self.__control):
            cmd_data = self.__control.set_CoaxLigth(value)
            self.HID_Send_Comand(cmd_data[0], cmd_data[1])

    def HID_Send_CMD_SpotLight(self, value):
        if (self.__control):
            cmd_data = self.__control.set_SpotLigth(value)
            self.HID_Send_Comand(cmd_data[0], cmd_data[1])

    def HID_Send_CMD_VibrationTable(self, value):
        if (self.__control):
            cmd_data = self.__control.set_VibrationTable(value)
            self.HID_Send_Comand(cmd_data[0], cmd_data[1])

    def HID_Send_CMD_Frequency(self, value):
        if (self.__control):
            cmd_data = self.__control.set_Frequency(value)
            self.HID_Send_Comand(cmd_data[0], cmd_data[1] )

    def ReadAndWriteToDevice(self, top_light_level: int, back_light_level: int, frequency: int, front_blow_level: int,
                             back_blow_levelint: int, PWM: int = 0):
        self.HID_Send_CMD_TopLight( top_light_level )
        self.HID_Send_CMD_BackLight(back_light_level)
        self.HID_Send_CMD_Frequency(frequency)
        # ...

        #self.__buffer_usb_rx =  self.__buffer_usb_rx  #Utils.newArrayOfBytes(HID_CONST.PAGE, 0)

        self.__buffer_usb_rx[HID_CONST.REG_50] = cmd

        position_array = position.to_bytes(4, "little")
        self.__buffer_usb_rx[HID_CONST.REG_51] = position_array[0]
        self.__buffer_usb_rx[HID_CONST.REG_52] = position_array[1]
        self.__buffer_usb_rx[HID_CONST.REG_53] = position_array[2]
        self.__buffer_usb_rx[HID_CONST.REG_54] = position_array[3]

        # set speed max
        spin_max_array = spid_max.to_bytes(4, "little")
        self.__buffer_usb_rx[HID_CONST.REG_55] = spin_max_array[0]
        self.__buffer_usb_rx[HID_CONST.REG_56] = spin_max_array[1]

        # set speed min
        spin_min_array = spid_min.to_bytes(4, "little")
        self.__buffer_usb_rx[HID_CONST.REG_57] = spin_min_array[0]
        self.__buffer_usb_rx[HID_CONST.REG_58] = spin_min_array[1]

        # set acceler
        acceler_array = acceler. to_bytes(4, "little")
        self.__buffer_usb_rx[HID_CONST.REG_57] = acceler_array[0]
        self.__buffer_usb_rx[HID_CONST.REG_58] = acceler_array[1]

        # set number of motor
        self.__buffer_usb_rx[HID_CONST.REG_61] = motor_number.to_byte(4, "littele")[0]
        return   self.__buffer_usb_rx

    def power(self)->int:
         return self.__motors.power() if self.__motors else False

    def SetMotorNumb(self, numb:int):
        if self.__motors :
           cmd_data = self.__motors.SetMotorNumb( numb )

        self.HID_Send_Comand(HID_CONST.REG_61, numb )
        self.HID_Send_Comand(HID_CONST.REG_50, 0x00)
        
    def listenMotor(self, numb:int):
        self.HID_Send_Comand(HID_CONST.REG_61, numb)
        self.HID_Send_Comand(HID_CONST.REG_50, 0x00)

    def JPlus(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x01)

    def Stop(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x02)

    def JMinus(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x03)

    def Abort(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x04)

    def inc(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x05)

    def abs(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x06)

    def res(self):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x09)

    def set_step(self, value : int ):
        self.HID_Send_Comand(HID_CONST.REG_50, 0x09)

    def set_motor(self, value):
        self.__motors.__motor_id = value
        
    def get_motor(self):
        return self.__motors.__motor_id

    def set_speed_max(self, value):
        self.__motots.__speed_max = value

    def get_speed_max(self):
        return self.__motots.__speed_max

    def set_speed_min(self, value):
        self.__motors__speed_min = value

    def get_speed_min(self):
        return self.__motors.__speed_min
    
    def set_acceler(self, value):
        self.__motors.__acceler = value

    def get_acceler(self):
        return self.__motors.__acceler
    
    def set_position(self, value):
        self.__motors.__position = value

    def get_position(self):
        return self.__motors.__position



