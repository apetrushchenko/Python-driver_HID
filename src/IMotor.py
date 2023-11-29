from __future__ import annotations
from abc import ABC, abstractmethod

class IMotor(ABC):

    @abstractmethod
    def power(self)->int:
        pass
    @abstractmethod
    def SetMotorNumb(self, numb:int):
        pass

    @abstractmethod
    def JPlus(self):
        pass

    @abstractmethod
    def JMinus(self):
        pass

    @abstractmethod
    def Abort(self):
        pass

    @abstractmethod
    def Stop(self):
        pass

    @abstractmethod
    def inc(self):
        pass

    @abstractmethod
    def abs(self):
        pass

    #@abstractmethod
    #def listenMotor(self):
    #   pass

    @abstractmethod
    def res(self):
        pass

    @property
    @abstractmethod
    def position(self)->int:
        pass

    @abstractmethod
    def set_position(self, value) :
        pass

    @abstractmethod
    def get_motor_id(self)->int:
        pass

    @abstractmethod
    def set_motor_id(self, value) :
        pass

    @property
    @abstractmethod
    def speed_max(self) -> int:
        pass

    @abstractmethod
    def set_speed_max(self, value) :
        pass

    @property
    @abstractmethod
    def speed_min(self) -> int:
        pass

    @abstractmethod
    def set_speed_min(self, value) :
        pass

    @property
    @abstractmethod
    def  ACC(self) -> int:
        pass

    @abstractmethod
    def set_ACC(self, value) :
        pass
