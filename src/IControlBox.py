from __future__ import annotations
from abc import ABC, abstractmethod

class IControl(ABC):


     @abstractmethod
     def get_TopLight(self) -> int:   # return property value
          pass

     @abstractmethod
     def set_TopLigth(self, new_value)->int:                           # save value & return command foe write to HID
          pass

     @abstractmethod
     def get_BackLigth(self)-> int  : # return property value
          pass

     @abstractmethod
     def set_BackLigth(self, value)->int:                              # save value & return command foe write to HID
          pass

     @abstractmethod
     def get_CoaxLigth(self)-> int:   # return property value
          pass

     @abstractmethod
     def set_CoaxLigth(self, value) ->int:                             # save value & return command foe write to HID
          pass

     @abstractmethod
     def get_SpotLigth(self)-> int:   # return property value
          pass

     @abstractmethod
     def set_SpotLigth(self, value) ->int:                            # save value & return command foe write to HID
          pass


     @abstractmethod
     def get_Frequency(self)-> int:   # return property value
          pass

     @abstractmethod
     def set_Frequency(self, value)->int:                              # save value & return command foe write to HID
          pass

     @abstractmethod
     def get_PWMMax(self)->int:      # return property value
          pass
     @abstractmethod
     def set_PWMMax(self, value)->int:                                # save value & return command foe write to HID
          pass

     @abstractmethod
     def get_VibrationTable(self)-> int:    # return property value
          pass

     @abstractmethod
     def set_VibrationTable(self, value)->int:                        # save value & return command foe write to HID
          pass

     #@abstractmethod
     #def ReadAndWriteToDevice(self, top_light_level: int, back_light_level: int, frequency: int, front_blow_level: int,
     #                         back_blow_levelint: int, PWM: int = 0):
     #    pass




     """

     @abstractmethod
     def HID_Send_CMD_TopLight(self, value):
          pass

     @abstractmethod
     def HID_Send_CMD_BackLight(self, value):
          pass

     @abstractmethod
     def HID_Send_CMD_CoaxLight(self, value):
          pass

     @abstractmethod
     def HID_Send_CMD_SpotLight(self, value):
          pass

     @abstractmethod
     def HID_Send_CMD_VibrationTable(self, value):
          pass

     @abstractmethod
     def HID_Send_CMD_Frequency(self, value):
          pass
    
     """

