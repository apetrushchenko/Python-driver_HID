import threading
import sys

import usb.core
import usb.util

from IControl import IControl
from IHIDBase import IHIDBase

#from HidDeviceData import HidDeviceData
#from HidReport import HidReport


from Utils import Utils
from src.IMotor import IMotor


class HIDBase(IHIDBase, IControl, IMotor):

    def __init__(self):

        self.timer_interval = 10

        self.__device = None  # our divice
        self.__devices = None # list of anabled devices
        self.endpoint = None  # this param for divice.Write( endpoint, ... )

        self.__attached = False


        self.__buffer_usb_rx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0) # array/buffer for write to HID
        self.__buffer_usb_tx = Utils.newArrayOfBytes(HID_CONST.PAGE, 0)

        self.__timer = None

        self.PowerMotorStatus =  False
        self.__positon_of_motor = 10
        self.read = 0
        self.__speed_max = 3000
        self.__speed_min = 100
        self.__acceler  = 500
        self.__curr_motor_id = 1

    def ReadAndWriteToDevice(self, top_light_level: int, back_light_level: int, frequency: int, front_blow_level: int,
                             back_blow_levelint: int, PWM: int = 0):
        pass

    @property
    def TopLight(self) -> int:
        pass

    @property
    def BackLigth(self) -> int:
        pass

    @property
    def Frequency(self) -> int:
        pass

    @property
    def PWMMax(self) -> int:
        pass

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

    def HID_Send_CMD_TopLight(self, value):
        self.HID_Send_Comand(HID_CONST.REG_2, int(value))

    def HID_Send_CMD_BackLight(self, value):
        self.HID_Send_Comand(HID_CONST.REG_3, int(value))

    def HID_Send_CMD_CoaxLight(self, value):
        self.HID_Send_Comand(HID_CONST.REG_4, int(value))

    def HID_Send_CMD_SpotLight(self, value):
        self.HID_Send_Comand(HID_CONST.REG_1, int(value))

    def HID_Send_CMD_VibrationTable(self, value):
        # self.HID_Send_Comand( HID_CONST.REG_5, int(value))
        pass

    def HID_Send_CMD_Frequency(self, value):
        # self.HID_Send_Comand( HID_CONST.REG_17, int(value))
        pass

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

            position_array = self.__positon_of_motor.to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_51] = position_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_52] = position_array[1]
            self.__buffer_usb_rx[HID_CONST.REG_53] = position_array[2]
            self.__buffer_usb_rx[HID_CONST.REG_54] = position_array[3]

            # set speed max
            spin_max_array = self.__speed_max.to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_55] = spin_max_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_56] = spin_max_array[1]

            # set speed min
            spin_min_array = self.__speed_min.to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_57] = spin_min_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_58] = spin_min_array[1]

            # set acceler
            acceler_array = self.__acceler.to_bytes(4, "little")
            self.__buffer_usb_rx[HID_CONST.REG_59] = acceler_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_60] = acceler_array[1]

            # set number of motor
            motor_id_array = self.__curr_motor_id.to_bytes(4, "little")
            mn = motor_id_array[0]
            self.__buffer_usb_rx[HID_CONST.REG_61] = motor_id_array[0]

        self.__hID_Write( self.__buffer_usb_rx )

    def __hID_Write(self, buffer: bytearray) -> None:
        buffer[0] = (2)
        #tmt = HidReport(self.__report_length, HidDeviceData(buffer, HidDeviceData.ReadStatus.SUCCESS))
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
    def Prepare_CMD_Motor(self, cmd, motor_number, position, spid_max, spid_min, acceler ):

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
        if( not self.PowerMotorStatus ):
            self.HID_Send_Comand(HID_CONST.REG_50, 0x07)
            self.PowerMotorStatus = True
        else :
            self.HID_Send_Comand(HID_CONST.REG_50, 0x08)
            self.PowerMotorStatus = False
        return int( self.PowerMotorStatus )

    def SetMotorNumb(self, numb:int):
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
        self.__curr_motor_id = value
        
    def get_motor(self):
        return self.__curr_motor_id

    def set_speed_max(self, value):
        self.__speed_max = value

    def get_speed_max(self):
        return self.__speed_max

    def set_speed_min(self, value):
        self.__speed_min = value

    def get_speed_min(self):
        return self.__speed_min
    
    def set_acceler(self, value):
        self.__acceler = value

    def get_acceler(self):
        return self.__acceler
    
    def set_position(self, value):
        self.__positon_of_motor = value

    def get_position(self):
        return self.__positon_of_motor


class HID_CONST:
    DEVICE_VID = 1155
    DEVICE_PID = 22352
    V1_PID = 22351
    C1_PID = 22352
    CMS_PID = 22353
    GA_PID = 22354

    V1_S = "V1"
    C1_S = "C1"
    CMS_S = "CMS"
    GA_S = "GLA"

    PRODUCT_PID_ARRAY = [V1_PID, C1_PID, CMS_PID, GA_PID]
    PRODUCT_NM_ARRAY = [V1_S, C1_S, CMS_S, GA_S]

    PAGE = 66

    REPORT_LENGTH = 641

    REPORT_ID_READ = 1
    REPORT_ID_WRITE = 2
    TEST_TIM = 0

    ON = 0xFFFF
    OFF = 0

    REG_1 = 1
    REG_2 = 2
    REG_3 = 3
    REG_4 = 4
    REG_5 = 5
    REG_6 = 6
    REG_7 = 7
    REG_8 = 8
    REG_9 = 9
    REG_10 = 10
    REG_11 = 11
    REG_12 = 12
    REG_13 = 13
    REG_14 = 14
    REG_15 = 15
    REG_16 = 16
    REG_17 = 17
    REG_30 = 30
    REG_31 = 31
    REG_32 = 32
    REG_33 = 33
    REG_34 = 34
    REG_35 = 35
    REG_36 = 36
    REG_37 = 37
    REG_38 = 38
    REG_39 = 39
    REG_40 = 40
    REG_41 = 41
    REG_42 = 42
    REG_43 = 43
    REG_44 = 44
    REG_45 = 45
    REG_46 = 46
    REG_47 = 47
    REG_48 = 48
    REG_49 = 49
    REG_50 = 50
    REG_51 = 51
    REG_52 = 52
    REG_53 = 53
    REG_54 = 54
    REG_55 = 55
    REG_56 = 56
    REG_57 = 57
    REG_58 = 58
    REG_59 = 59
    REG_60 = 60
    REG_61 = 61

    OUTPUT0_BIT = 0
    OUTPUT1_BIT = 0
    OUTPUT2_BIT = 0
    BIT0_RES = 0xFE
    BIT1_RES = 0xFD
    BIT2_RES = 0xFB
    BIT3_RES = 0xF7
    BIT4_RES = 0xEF
    BIT5_RES = 0xDF
    BIT6_RES = 0xBF
    BIT7_RES = 0x7F
    BIT0_SET = 0x01
    BIT1_SET = 0x02
    BIT2_SET = 0x04
    BIT3_SET = 0x08
    BIT4_SET = 0x10
    BIT5_SET = 0x20
    BIT6_SET = 0x40
    BIT7_SET = 0x80

