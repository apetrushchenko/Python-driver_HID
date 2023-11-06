from enum import IntEnum
from src.utils import Utils

class HidDeviceData:
    
    class ReadStatus(IntEnum):
        SUCCESS = 0
        WAITTIMEDOUT = 1
        WAITFAIL = 2
        NODATAREAD = 3
        READERROR = 4
        NOTCONNECTED = 5
        
        @classmethod
        def has_value(cls, value):
            return any(value == item.value for item in cls)


    @property
    def data(self) -> bytearray:
        return self.__data
    @data.setter
    def data(self, value) -> bytearray:
        self.__data = value
        return self.__data
    
    @property
    def status(self) -> 'ReadStatus':
        return self.__status
    @status.setter
    def status(self, value) -> 'ReadStatus':
        self.__status = value
        return self.__status
    
    def __init__(self, status_ : 'ReadStatus') -> None:
        self.__data = None;
        self.__status = HidDeviceData.ReadStatus.SUCCESS
        self.data = Utils.newArrayOfBytes(0, 0)
        self.status = status_
    
    def __init__(self, data_ : bytearray, status_ : 'ReadStatus') -> None:
        self.__data = None;
        self.__status = HidDeviceData.ReadStatus.SUCCESS
        self.data = data_
        self.status = status_