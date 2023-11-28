import os.path

from src.HIDConst import HID_CONST
from src.IControlBox import IControl
import pickle


class ConcreteControl(IControl)    :

    def __init__(self, isSeriable=False):
        self.__TopLigth = 0
        self.__BackLigth = 0
        self.__CoaxLigth = 0
        self.__SpotLigth = 0
        self.__Frequency = 0
        self.__VibroTable = 0
        self.__PWMMax = 0
        self.__cmd = -1

        self.__isNeedSave = isSeriable

        if( self.__isNeedSave ):
            self.load()

    def __del__(self):
        if (self.__isNeedSave):
            #self.save()
            pass

    def get_TopLight(self) -> int:
        return self.__TopLigth

    def set_TopLigth(self, value):
        self.__validate_set(value)
        self.__TopLigth = value
        self.__cmd = HID_CONST.REG_2
        return (self.__cmd, value)

    def get_BackLigth(self) -> int:
        return self.__BackLigth

    def set_BackLigth(self, value):
        self.__validate_set(value)
        self.__BackLigth = value
        self.__cmd = HID_CONST.REG_3
        return (self.__cmd, value)

    def get_CoaxLigth(self) -> int:
        return self.__CoaxLigth


    def set_CoaxLigth(self, value):
        self.__validate_set(value)
        self.__CoaxLigth = value
        self.__cmd = HID_CONST.REG_4
        return (self.__cmd, value )

    def get_SpotLigth(self) -> int:
        return self.__SpotLigth

    def set_SpotLigth(self, value):
        self.__validate_set(value)
        self.__SpotLigth = value
        self.__cmd = HID_CONST.REG_1
        return (self.__cmd, value )

    def get_Frequency(self) -> int:
        return self.__Frequency

    def set_Frequency(self, value):
        self.__validate_set(value)
        self.__Frequency = value
        self.__cmd = HID_CONST.REG_17
        return (self.__cmd, value)

    def get_PWMMax(self) -> int:
        return self.__PWMMax

    def set_PWMMax(self, value):
        self.__validate_set(value)
        self.__PWMMax = value
        self.__cmd = HID_CONST.REG_6
        return (self.__cmd, value)

    def get_VibrationTable(self) -> int:
        return self.__VibroTable

    def set_VibrationTable(self, value):
        self.__validate_set( value )
        self.__VibroTable = value
        self.__cmd = HID_CONST.REG_5
        return (self.__cmd, value )


    def __validate_set(self,  value : int )->bool:
        res = True
        if( value < 0 ):
           res = False
           raise ValueError( "Value cannot be negative " )

        elif ( value > 500):
           res = False
           raise ValueError( "Value cannot be more then 500 " )

        return res


    def save(self, file_name = None  ):
        if (file_name is None) :
            file_name = HID_CONST.FNM_SERIALIZATION

        directory = os.path.dirname( file_name )
        if (  os.path.exists(  directory  )  ):
            os.makedirs( directory )

        with open( file_name, "wb") as f:
            pickle.dump( self, f )


    def load(self,  file_name = None):
        if (file_name is None):
            file_name = HID_CONST.FNM_SERIALIZATION

        if( not os.path.exists( file_name ) ):
            #raise FileExistsError("File not exist")
            return

        with open( file_name , "rb") as f:
            tmp = pickle.load(f)

        for attr_nm in vars(type(self)):
            setattr(self, attr_nm, getattr(tmp, attr_nm))

            """
            self.__TopLigth = tmp.__TopLigth
            self.__BackLigth = tmp.__BackLigth
            self.__CoaxLigth = tmp.__CoaxLigth
            self.__SpotLigth = tmp.__SpotLigth
            self.__Frequency = tmp.___Frequency
            self.__VibroTable = tmp.__VibroTable
            self.__PWMMax = tmp.__PWMMax
            self.__cmd = -2
            """
