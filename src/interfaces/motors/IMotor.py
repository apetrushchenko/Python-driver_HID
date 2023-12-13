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

    @position.setter
    @abstractmethod
    def position(self, value) :
        pass

    @property
    @abstractmethod
    def motor_id(self)->int:
        pass

    @motor_id.setter
    @abstractmethod
    def motor_id(self, value) :
        pass

    @property
    @abstractmethod
    def speed_max(self) -> int:
        pass

    @speed_max.setter
    @abstractmethod
    def speed_max(self, value) :
        pass

    @property
    @abstractmethod
    def speed_min(self) -> int:
        pass

    @speed_min.setter
    @abstractmethod
    def speed_min(self, value) :
        pass

    @property
    @abstractmethod
    def  ACC(self) -> int:
        pass
    @ACC.setter
    @abstractmethod
    def ACC(self, value) :
        pass
