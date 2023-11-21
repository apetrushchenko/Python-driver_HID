from __future__ import annotations
from abc import ABC, abstractmethod

class IHIDBase(ABC):

    def open(self):
        pass

    # @property
    def get_Device(self) -> None:
        pass

    # @property.setter
    def set_Device(self, value):
        pass

    def ReadDevice(self) -> None:
        pass

    def start(self):
        pass

    def stop(self):
        pass

    def HID_Send_Comand(self, comand: int, data: int) -> None:
        pass


    def __hID_Write(self, buffer: bytearray) -> None:
        pass

