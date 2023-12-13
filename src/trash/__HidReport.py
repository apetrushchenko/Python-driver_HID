#from src.HIDBase import Utils
from Misc import RefOutArgWrapper
from src.pickle.__HidDeviceData import HidDeviceData

def Resize(  arr1 : bytearray(), newSize : int )-> None:

    # Create a new bytearray with the desired length
    arr2 = bytearray(newSize)

    # Copy the contents of arr1 to arr2
    arr2[:len(arr1)] = arr1

    return arr2


def Copy (source_array, start_index_source, target_array, start_index_target, len_array )->None:

    target_array = source_array[start_index_source:len_array + 1]

    return target_array




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
        Resize( self.__data)
        wrap_data1 = RefOutArgWrapper(self.__data,report_size-1)
        self.__data = wrap_data1.value
        return self.__data
    
    def __init__(self, report_size : int, device_data : 'HidDeviceData') -> None:
        self.__report_id = 0
        self.__data   = Utils.newArrayOfBytes(0, 0)
        self.__status = HidDeviceData.ReadStatus.SUCCESS
        self.__exists = False
        self.__status = device_data.status

        self.__data = Resize( self.__data, report_size-1)
        wrap_data2 = RefOutArgWrapper(self.__data)
        self.__data = wrap_data2.value
        if (device_data.data is not None): 
            if (len(device_data.data) != 0): 
                self.__report_id = device_data.data[0]
                self.exists = True
                if (len(device_data.data) > 1): 
                    length = report_size - 1
                    if (len(device_data.data) < (report_size - 1)): 
                        length = (len(device_data.data))
                    self.__data = Copy(device_data.data,1, self.__data, 0, length)
                else:
                    self.exists = False
        else: 
            self.exists = False
    
    def getBytes(self) -> bytearray:
        array0_ = None
        wraparray3 = RefOutArgWrapper(array0_)
        Resize( array0_, self.__data.Length + 1 )
        array0_ = wraparray3.value
        array0_[0] = self.__report_id
        Copy (self.__data, 0, array0_, 1, self.__data.Length)
        return array0_

