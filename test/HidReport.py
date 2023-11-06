from src.utils import Utils
from src.Misc import RefOutArgWrapper

class HidReport:
    
    @property
    def exists(self) -> bool:
        return self.__exists
    @exists.setter
    def exists(self, value) -> bool:
        self.__exists = value
        return self.__exists
    
    @property
    def read_status(self) -> 'ReadStatus':
        return self.__status
    
    @property
    def report_id(self) -> int:
        return self.__report_id
    @report_id.setter
    def report_id(self, value) -> int:
        self.__report_id = value
        self.exists = True
        return value
    
    @property
    def data(self) -> bytearray:
        return self.__data
    @data.setter
    def data(self, value) -> bytearray:
        self.__data = value
        self.exists = True
        return value
    
    def __init__(self, report_size : int) -> None:
        self.__report_id = 0
        self.__data = Utils.newArrayOfBytes(0, 0)
        self.__status = HidDeviceData.ReadStatus.SUCCESS
        self.__exists = False
        wrap_data1 = RefOutArgWrapper(self.__data)
         ERROR(type=Array).ERROR: Resize(?, int) void not supported in Python
        self.__data = wrap_data1.value
    
    def __init__(self, report_size : int, device_data : 'HidDeviceData') -> None:
        self.__report_id = 0
        self.__data = Utils.newArrayOfBytes(0, 0)
        self.__status = HidDeviceData.ReadStatus.SUCCESS
        self.__exists = False
        self.__status = device_data.status
        wrap_data2 = RefOutArgWrapper(self.__data)
         ERROR(type=Array).ERROR: Resize(?, int) void not supported in Python
        self.__data = wrap_data2.value
        if (device_data.data is not None): 
            if (len(device_data.data) != 0): 
                self.__report_id = device_data.data[0]
                self.exists = True
                if (len(device_data.data) > 1): 
                    length = report_size - 1
                    if (len(device_data.data) < (report_size - 1)): 
                        length = (len(device_data.data))
                     ERROR(type=Array).ERROR: Copy(?, int, ?, int, int) void not supported in Python
            else: 
                self.exists = False
        else: 
            self.exists = False
    
    def getBytes(self) -> bytearray:
        array0_ = None
        wraparray3 = RefOutArgWrapper(array0_)
         ERROR(type=Array).ERROR: Resize(?, int) void not supported in Python
        array0_ = wraparray3.value
        array0_[0] = self.__report_id
         ERROR(type=Array).ERROR: Copy(?, int, ?, int, int) void not supported in Python
        return array0_