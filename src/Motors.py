from src.HIDConst import HID_CONST
from src.IMotor import IMotor

class ConcreteMotors( IMotor ):

    @property
    def position(self) -> int:
        return self.__position

    @position.setter
    def set_position(self, value):
        self.__position = value

    @property
    def motor_id(self) -> int:
        return self.__curr_motor_id

    @motor_id.setter
    def set_motor_id(self, value):
        self.__motor_id = value

    @property
    def speed_max(self) -> int:
        return self.__speed_max

    @speed_max.setter
    def set_speed_max(self, value ):
        self.__speed_max = value

    @property
    def speed_min(self) -> int:
        return self.__speed_min

    @speed_min.setter
    def set_speed_min(self, value ):
        self.__speed_min = value

    @property
    def ACC(self) -> int:
        return self.__acceler

    @ACC.setter
    def set_ACC(self, value ):
        self.__acceler = value

    def __init__(self, buffer = None):
        self.__buffer_usb_rx = buffer
        self.__speed_max = 3000
        self.__speed_min = 100
        self.__acceler = 500
        self.__curr_motor_id = 1
        self.__position = 2000
        self.__motor_power_status = False
        self.read = 0



    def set_buffer(self, buffer ):
        self.__buffer_usb_rx = buffer

    def power(self) -> bool:
        res = (HID_CONST.REG_50, -3 )
        if (not self.__motor_power_status):
            res = (HID_CONST.REG_50, 0x07)
            self.__motor_power_status = True
        else:
            res = (HID_CONST.REG_50,  0x08)
            self.__motor_power_status = False
        return res

    def SetMotorNumb(self, numb: int)->int:                                                # ret tulip ( command, data )
        #        self.curr_motor_id = numb;
        return (HID_CONST.REG_50, 0x00 )
        # self.HID_Send_Comand(HID_CONST.REG_61, numb)
        # return #self.HID_Send_Comand(HID_CONST.REG_50, 0x00)

    def JPlus(self)-> 'tulip':
        # self.HID_Send_Comand(HID_CONST.REG_50, 0x01)
        return (HID_CONST.REG_50, 0x01 )

    def JMinus(self):
        return (HID_CONST.REG_50, 0x03)
        # self.HID_Send_Comand(HID_CONST.REG_50, 0x03)

    def Abort(self):
        return (HID_CONST.REG_50, 0x04)
        # self.HID_Send_Comand(HID_CONST.REG_50, 0x04)

    def Stop(self):
        return (HID_CONST.REG_50, 0x02)
        # self.HID_Send_Comand(HID_CONST.REG_50, 0x02)

    def inc(self):
        return (HID_CONST.REG_50, 0x05)
        #self.HID_Send_Comand(HID_CONST.REG_50, 0x05)

    def abs(self):
        return (HID_CONST.REG_50, 0x06)
        #self.HID_Send_Comand(HID_CONST.REG_50, 0x06)

    def res(self):
        #self.HID_Send_Comand(HID_CONST.REG_50, 0x09)
        return (HID_CONST.REG_50, 0x09)





