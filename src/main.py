from src.HIDBase import HIDBase

objDev = None

try:
    objDev = HIDBase()
    # objDev.HID_Send_CMD_TopLight(111)

    objDev.open()


    objDev.HID_Send_CMD_SpotLight(input("Spot light, set value as 0=500 =>"))
    value = input("Top light, set value as 0=500 =>")
    objDev.HID_Send_CMD_TopLight(value)
    value = input("Back light, set value as 0=500 =>")
    objDev.HID_Send_CMD_BackLight(value)
    objDev.HID_Send_CMD_CoaxLight(input("Coax light, set value as 0=500 =>"))
    value = input("VibroTablet, set value as 0=500 =>")
    # objDev.HID_Send_CMD_TopLight(value)
    value = input("Frecency, set value as 0=500 =>")
    # objDev.HID_Send_CMD_TopLight(value)

except Exception as AnyError:
    print(f"Unexpected {AnyError} ")

finally:
    if objDev is None:
        pass
    else:
        objDev.stop()