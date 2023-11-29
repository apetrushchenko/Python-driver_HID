from src.ControlBox import ConcreteControl
from src.HIDBase import HIDBase
from src.Motors import ConcreteMotors

dev = None

try:
    cb     = ConcreteControl(True)
    motors = ConcreteMotors()

    dev = HIDBase( cb, motors )
    # dev.HID_Send_CMD_TopLight(111)

    dev.open()

    #dev.HID_Send_Comand(50, 0x07)

    if( input("Do you want test controlbox[0] or motors[1]=>") == "0" ) :
        dev.HID_Send_CMD_SpotLight(  int( input("Spot light, set value as 0=500 =>") ) )
        dev.HID_Send_CMD_TopLight( int( input("Top light, set value as 0=500 =>") ) )
        dev.HID_Send_CMD_BackLight(int( input("Back light, set value as 0=500 =>") ) )
        dev.HID_Send_CMD_CoaxLight(int(input("Coax light, set value as 0=500 =>") ) )
        dev.HID_Send_CMD_SpotLight( int( input("VibroTablet, set value as 0=500 =>") ) )
        dev.HID_Send_CMD_Frequency( int( input("Frecency, set value as 0=500 =>") ) )
    else:

        #var = input("Before need turn on power on[0]/off[1]=>")
        if( input("Before need turn on power on[0]/off[1]=>") == "0" ):
            try:
                dev.power()
                dev.motor_id = 0
                dev.position = 3000
                dev.speed_max = 60
                dev.speed_min = 600
                dev.ACC = 1000

                dev.Abort()   # try funcs abort/stop wrote are correct
                dev.Stop()

                is_loop   = True
                while (is_loop):
                    motor = int(input("Set current motor for test, as [ 0-2 / 9 exit]=>"))
                    if(motor != 9):
                        dev.get_Device()
                        dev.motor_id = motor
                       # dev.set_position( int(input("Set needed position for motor =>")) )
                        if( input("Are you ready to GO [O yes/1 not]:") == "0" ):
                            #dev.JPlus()
                            dev.JMinus()
                            if ( input(  "Stop , press 0" ) == "0"):
                                dev.Abort()
                            else:
                                dev.Stop()
                    else:
                        is_loop = False

            except Exception as AnyError:
                print(f"Unexpected {AnyError} ")

            finally:
                dev.power()

        else:
            input( "You don't turn on motor, without energy work not possible , press any key for exit")

except Exception as AnyError:
    print(f"Unexpected {AnyError} ")

finally:

    if dev is None:
        pass
    else:
        dev.stop()
        del dev