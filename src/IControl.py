from __future__ import annotations
from abc import ABC, abstractmethod

class IControl(ABC):



     @abstractmethod
     def ReadAndWriteToDevice(self, top_light_level:int, back_light_level:int, frequency:int, front_blow_level:int, back_blow_levelint:int,  PWM:int = 0) :
       pass


     @property
     @abstractmethod
     def TopLight(self) -> int:
          pass

     @property
     @abstractmethod
     def BackLigth(self)-> int:
          pass

     @property
     @abstractmethod
     def Frequency(self)-> int:
          pass

     @property
     @abstractmethod
     def PWMMax(self)->int:
          pass

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

