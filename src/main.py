import hid
import time
import "./utils"

class hidDev:
    __attached = None

    __device = None

    __devices = None

    __report_length = 64

    __random = None

    def __init__(self) -> None:

        InitializeComponent()  # error
        self.__readDevice()
        if (Form1.__device is None):
            InitializeComponent()  # error
            return
        else:
            Form1.__device.OpenDevice()  # error
            Form1.__device.Inserted += (DeviceAttach]edHandler)
            Form1.__device.Removed += (DeviceRemovedHandler)
            Form1.__device.MonitorDeviceEvents = (True)
            Form1.__device.ReadReport(OnReport)  # error

    __device_vid = 1155
    __device_pid = 22352
    __v1_pid = 22351
    __c1_pid = 22352
    __cms_pid = 22353
    __ga_pid = 22354
    __report_id_read = 1
    __report_id_write = 2
    __test_tim = 0

    __page = 66
    __buffer_usb_rx = None
    __buffer_usb_tx = None
    __output0_bit = 0
    __output1_bit = 0
    __output2_bit = 0
    __bit0_res = 0xFE
    __bit1_res = 0xFD
    __bit2_res = 0xFB
    __bit3_res = 0xF7
    __bit4_res = 0xEF
    __bit5_res = 0xDF
    __bit6_res = 0xBF
    __bit7_res = 0x7F
    __bit0_set = 0x01
    __bit1_set = 0x02
    __bit2_set = 0x04
    __bit3_set = 0x08
    __bit4_set = 0x10
    __bit5_set = 0x20
    __bit6_set = 0x40
    __bit7_set = 0x80

    __reg_1 = 1
    __reg_2 = 2
    __reg_3 = 3
    __reg_4 = 4
    __reg_5 = 5
    __reg_6 = 6
    __reg_7 = 7
    __reg_8 = 8
    __reg_9 = 9
    __reg_10 = 10
    __reg_11 = 11
    __reg_12 = 12
    __reg_13 = 13
    __reg_14 = 14
    __reg_15 = 15
    __reg_16 = 16
    __reg_17 = 17
    __reg_30 = 30
    __reg_31 = 31
    __reg_32 = 32
    __reg_33 = 33
    __reg_34 = 34
    __reg_35 = 35
    __reg_36 = 36
    __reg_37 = 37
    __reg_38 = 38
    __reg_39 = 39
    __reg_40 = 40
    __reg_41 = 41
    __reg_42 = 42
    __reg_43 = 43
    __reg_44 = 44
    __reg_45 = 45
    __reg_46 = 46
    __reg_47 = 47
    __reg_48 = 48
    __reg_49 = 49
    __reg_50 = 50
    __reg_51 = 51
    __reg_52 = 55
    __reg_53 = 57
    __reg_54 = 59
    __reg_59 = 59
    __reg_60 = 60
    __on = 0xFFFF
    __off = 0

    def __timer1_Tick(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
        pass

    def __hID_Send_Comand(self, comand: int, data: int) -> None:
        conv_array = Utils.newArrayOfBytes(4, 0)
        conv_array = (data).to_bytes(4, byteorder="little")
        Form1.__buffer_usb_rx[Form1.__reg_40] = (0)
        Form1.__buffer_usb_rx[50] = (0)
        swichVal = comand
        if (swichVal == Form1.__reg_1):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[1] = conv_array[0]
            Form1.__buffer_usb_rx[2] = conv_array[1]
        elif (swichVal == Form1.__reg_2):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[3] = conv_array[0]
            Form1.__buffer_usb_rx[4] = conv_array[1]
        elif (swichVal == Form1.__reg_3):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[5] = conv_array[0]
            Form1.__buffer_usb_rx[6] = conv_array[1]
        elif (swichVal == Form1.__reg_4):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[7] = conv_array[0]
            Form1.__buffer_usb_rx[8] = conv_array[1]
        elif (swichVal == Form1.__reg_5):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[9] = conv_array[0]
            Form1.__buffer_usb_rx[10] = conv_array[1]
        elif (swichVal == Form1.__reg_6):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[11] = conv_array[0]
            Form1.__buffer_usb_rx[12] = conv_array[1]
        elif (swichVal == Form1.__reg_7):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[13] = conv_array[0]
            Form1.__buffer_usb_rx[14] = conv_array[1]
        elif (swichVal == Form1.__reg_8):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[15] = conv_array[0]
            Form1.__buffer_usb_rx[16] = conv_array[1]
        elif (swichVal == Form1.__reg_9):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[17] = conv_array[0]
            Form1.__buffer_usb_rx[18] = conv_array[1]
        elif (swichVal == Form1.__reg_10):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[19] = conv_array[0]
            Form1.__buffer_usb_rx[20] = conv_array[1]
        elif (swichVal == Form1.__reg_11):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[21] = conv_array[0]
            Form1.__buffer_usb_rx[22] = conv_array[1]
        elif   def __hID_Send_Comand(self, comand: int, data: int) -> None:
        conv_array = Utils.newArrayOfBytes(4, 0)
        conv_array = (data).to_bytes(4, byteorder="little")
        Form1.__buffer_usb_rx[Form1.__reg_40] = (0)
        Form1.__buffer_usb_rx[50] = (0)
        swichVal = comand
        if (swichVal == Form1.__reg_1):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[1] = conv_array[0]
            Form1.__buffer_usb_rx[2] = conv_array[1]
        elif (swichVal == Form1.__reg_2):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[3] = conv_array[0]
            Form1.__buffer_usb_rx[4] = conv_array[1]
        elif (swichVal == Form1.__reg_3):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[5] = conv_array[0]
            Form1.__buffer_usb_rx[6] = conv_array[1]
        elif (swichVal == Form1.__reg_4):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[7] = conv_array[0]
            Form1.__buffer_usb_rx[8] = conv_array[1]
        elif (swichVal == Form1.__reg_5):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[9] = conv_array[0]
            Form1.__buffer_usb_rx[10] = conv_array[1]
        elif (swichVal == Form1.__reg_6):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[11] = conv_array[0]
            Form1.__buffer_usb_rx[12] = conv_array[1]
        elif (swichVal == Form1.__reg_7):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[13] = conv_array[0]
            Form1.__buffer_usb_rx[14] = conv_array[1]
        elif (swichVal == Form1.__reg_8):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[15] = conv_array[0]
            Form1.__buffer_usb_rx[16] = conv_array[1]
        elif (swichVal == Form1.__reg_9):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[17] = conv_array[0]
            Form1.__buffer_usb_rx[18] = conv_array[1]
        elif (swichVal == Form1.__reg_10):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[19] = conv_array[0]
            Form1.__buffer_usb_rx[20] = conv_array[1]
        elif (swichVal == Form1.__reg_11):
            conv_array = (data).to_bytes(4, byteorder="little")
            F(swichVal == Form1.__reg_12):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[23] = conv_array[0]
            Form1.__buffer_usb_rx[24] = conv_array[1]
        elif (swichVal == Form1.__reg_13):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[25] = conv_array[0]
            Form1.__buffer_usb_rx[26] = conv_array[1]
        elif (swichVal == Form1.__reg_14):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[27] = conv_array[0]
            Form1.__buffer_usb_rx[28] = conv_array[1]
        elif (swichVal == Form1.__reg_15):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[29] = conv_array[0]
            Form1.__buffer_usb_rx[30] = conv_array[1]
        elif (swichVal == Form1.__reg_16):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[Form1.__reg_45] = conv_array[0]
            Form1.__buffer_usb_rx[Form1.__reg_46] = conv_array[1]
        elif (swichVal == Form1.__reg_17):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[Form1.__reg_47] = conv_array[0]
            Form1.__buffer_usb_rx[Form1.__reg_48] = conv_array[1]
        elif (swichVal == Form1.__reg_30):
            Form1.__buffer_usb_rx[Form1.__reg_30] = (.ToByte(Form1.__output0_bit)  # error )
            elif (swichVal == Form1.__reg_31):
            Form1.__buffer_usb_rx[Form1.__reg_31] = (.ToByte(Form1.__output1_bit)  # error )
            elif (swichVal == Form1.__reg_32):
            Form1.__buffer_usb_rx[Form1.__reg_32] = (.ToByte(Form1.__output2_bit)  # error )
            elif (swichVal == Form1.__reg_33):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[Form1.__reg_33] = conv_array[0]
            elif (swichVal == Form1.__reg_34):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[Form1.__reg_34] = conv_array[0]
            elif (swichVal == Form1.__reg_35):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[Form1.__reg_35] = conv_array[0]
            elif (swichVal == Form1.__reg_36):
            conv_array = (data).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[Form1.__reg_36] = conv_array[0]
            elif (swichVal == Form1.__reg_37):
            Form1.__buffer_usb_rx[Form1.__reg_37] = conv_array[0]
            elif (swichVal == Form1.__reg_38):
            Form1.__buffer_usb_rx[Form1.__reg_38] = conv_array[0]
            elif (swichVal == Form1.__reg_39):
            Form1.__buffer_usb_rx[Form1.__reg_39] = conv_array[0]
            elif (swichVal == Form1.__reg_40):
            Form1.__buffer_usb_rx[Form1.__reg_40] = conv_array[0]
            elif (swichVal == Form1.__reg_41):
            Form1.__buffer_usb_rx[Form1.__reg_41] = conv_array[0]
            elif (swichVal == Form1.__reg_42):
            Form1.__buffer_usb_rx[Form1.__reg_42] = conv_array[0]
            elif (swichVal == Form1.__reg_43):
            Form1.__buffer_usb_rx[Form1.__reg_43] = conv_array[0]
            elif (swichVal == Form1.__reg_44):
            Form1.__buffer_usb_rx[Form1.__reg_44] = conv_array[0]
            elif (swichVal == Form1.__reg_47):
            Form1.__buffer_usb_rx[Form1.__reg_47] = conv_array[0]
            elif (swichVal == Form1.__reg_48):
            Form1.__buffer_usb_rx[Form1.__reg_48] = conv_array[0]
            elif (swichVal == Form1.__reg_49):
            Form1.__buffer_usb_rx[Form1.__reg_49] = conv_array[0]
            elif (swichVal == Form1.__reg_50):
            Form1.__buffer_usb_rx[50] = conv_array[0]
            conv_array = (.ERROR: ToInt32(?)
            int
            not supported in Python).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[51] = conv_array[0]
            Form1.__buffer_usb_rx[52] = conv_array[1]
            Form1.__buffer_usb_rx[53] = conv_array[2]
            Form1.__buffer_usb_rx[54] = conv_array[3]
            if (numericUpDown12.Value > numericUpDown13.Value):
                numericUpDown12.Value = (numericUpDown13.Value)
            conv_array = (.ERROR: ToInt32(?)
            int
            not supported in Python).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[55] = conv_array[0]
            Form1.__buffer_usb_rx[56] = conv_array[1]
            if (numericUpDown13.Value < numericUpDown12.Value):
                numericUpDown13.Value = (numericUpDown12.Value)
            conv_array = (.ERROR: ToInt32(?)
            int
            not supported in Python).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[57] = conv_array[0]
            Form1.__buffer_usb_rx[58] = conv_array[1]
            conv_array = (.ERROR: ToInt32(?)
            int
            not supported in Python).to_bytes(4, byteorder="little")
            Form1.__buffer_usb_rx[59] = conv_array[0]
            Form1.__buffer_usb_rx[60] = conv_array[1]
            Form1.__buffer_usb_rx[61] = (.ToByte(comboBox1.Text)  # error )
            self.(Form1.__buffer_usb_rx)

    def __groupBox3_Enter(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
        pass

    def __timer2_Tick(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
        # **** INPUT *****////
        if (len(Form1.__buffer_usb_tx) > 60):
            x = ((Form1.__buffer_usb_tx[30]) & (Form1.__bit0_set))
            if (x == (0)):
                pictureBox7.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox7.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit1_set)))
            if (x == (0)):
                pictureBox8.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox8.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit2_set)))
            if (x == (0)):
                pictureBox9.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox9.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit3_set)))
            if (x == (0)):
                pictureBox10.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox10.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit4_set)))
            if (x == (0)):
                pictureBox11.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox11.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit5_set)))
            if (x == (0)):
                pictureBox12.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox12.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit6_set)))
            if (x == (0)):
                pictureBox13.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox13.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[30]) & (Form1.__bit7_set)))
            if (x == (0)):
                pictureBox14.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox14.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[31]) & (Form1.__bit0_set)))
            if (x == (0)):
                pictureBox15.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox15.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            x = (((Form1.__buffer_usb_tx[31]) & (Form1.__bit1_set)))
            if (x == (0)):
                pictureBox16.Image = (WindowsFormsApp1.Properties.Resources.green_led_off_md)
            else:
                pictureBox16.Image = (WindowsFormsApp1.Properties.Resources.green_led_on_md)
            numericUpDown17.Value = (.ERROR: ToInt16(?)
            short
            not supported in Python)
            numericUpDown18.Value = (.ERROR: ToInt16(?)
            short
            not supported in Python)
            numericUpDown15.Value = (int.from_bytes(Form1.__buffer_usb_tx[51:51 + 2], byteorder="little"))
            numericUpDown20.Value = (int.from_bytes(Form1.__buffer_usb_tx[44:44 + 2], byteorder="little"))
        if (Form1.__attached == False):
            label1.Text = (" not connected ")
        else:
            label1.Text = (" MicrOptik " + comboBox2.Text)

    def __trackBar12_Scroll(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
        """ C1-V1

        Args:
            sender(object):
            e0_( ERROR(type=EventArgs)):
        """
        numericUpDown19.Value = (.ERROR: ToUInt16(?)
        ushort
        not supported in Python)
        self.__hID_Send_Comand(Form1.__reg_1,.ERROR: ToUInt16(?) ushort
        not supported in Python)

        def __numericUpDown19_ValueChanged(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
            trackBar12.Value = (.ERROR: ToUInt16(?)
            ushort
            not supported in Python)
            self.__hID_Send_Comand(Form1.__reg_1,.ERROR: ToUInt16(?) ushort
            not supported in Python)

            def __trackBar1_Scroll(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
                numericUpDown1.Value = (.ERROR: ToUInt16(?)
                ushort
                not supported in Python)
                self.__hID_Send_Comand(Form1.__reg_2,.ERROR: ToUInt16(?) ushort
                not supported in Python)

                def __numericUpDown1_ValueChanged(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
                    trackBar1.Value = (.ERROR: ToUInt16(?)
                    ushort
                    not supported in Python)
                    self.__hID_Send_Comand(Form1.__reg_2,.ERROR: ToUInt16(?) ushort
                    not supported in Python)

                    def __trackBar2_Scroll(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
                        numericUpDown2.Value = (.ERROR: ToUInt16(?)
                        ushort
                        not supported in Python)
                        self.__hID_Send_Comand(Form1.__reg_3,.ERROR: ToUInt16(?) ushort
                        not supported in Python)

                        def __numericUpDown2_ValueChanged(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
                            trackBar2.Value = (.ERROR: ToUInt16(?)
                            ushort
                            not supported in Python)
                            self.__hID_Send_Comand(Form1.__reg_3,.ERROR: ToUInt16(?) ushort
                            not supported in Python)

                            def __trackBar3_Scroll(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
                                numericUpDown3.Value = (.ERROR: ToUInt16(?)
                                ushort
                                not supported in Python)
                                self.__hID_Send_Comand(Form1.__reg_4,.ERROR: ToUInt16(?) ushort
                                not supported in Python)

                                def __numericUpDown3_ValueChanged(self, sender: object,
                                                                  e0_: ERROR(type=EventArgs)) -> None:
                                    trackBar3.Value = (.ERROR: ToUInt16(?)
                                    ushort
                                    not supported in Python)
                                    self.__hID_Send_Comand(Form1.__reg_4,.ERROR: ToUInt16(?) ushort
                                    not supported in Python)

                                    def __trackBar4_Scroll(self, sender: object, e0_: ERROR(type=EventArgs)) -> None:
                                        numericUpDown4.Value = (.ERROR: ToUInt16(?)
                                        ushort
                                        not supported in Python)
                                        self.__hID_Send_Comand(Form1.__reg_5,.ERROR: ToUInt16(?) ushort
                                        not supported in Python)

                                        def __numericUpDown4_ValueChanged(self, sender: object,
                                                                          e0_: ERROR(type=EventArgs)) -> None:
                                            trackBar4.Value = (.ERROR: ToUInt16(?)
                                            ushort
                                            not supported in Python)
                                            self.__hID_Send_Comand(Form1.__reg_5,.ERROR: ToUInt16(?) ushort
                                            not supported in Python)

                                            def __trackBar5_Scroll(self, sender: object,
                                                                   e0_: ERROR(type=EventArgs)) -> None:
                                                numericUpDown5.Value = (.ERROR: ToUInt16(?)
                                                ushort
                                                not supported in Python)
                                                self.__hID_Send_Comand(Form1.__reg_6,.ERROR: ToUInt16(?) ushort
                                                not supported in Python)

                                                def __numericUpDown5_ValueChanged(self, sender: object,
                                                                                  e0_: ERROR(type=EventArgs)) -> None:
                                                    trackBar5.Value = (.ERROR: ToUInt16(?)
                                                    ushort
                                                    not supported in Python)
                                                    self.__hID_Send_Comand(Form1.__reg_6,.ERROR: ToUInt16(?) ushort
                                                    not supported in Python)

                                                    def __trackBar6_Scroll(self, sender: object,
                                                                           e0_: ERROR(type=EventArgs)) -> None:
                                                        numericUpDown6.Value = (.ERROR: ToUInt16(?)
                                                        ushort
                                                        not supported in Python)
                                                        self.__hID_Send_Comand(Form1.__reg_7,.ERROR: ToUInt16(?) ushort
                                                        not supported in Python)

                                                        def __numericUpDown6_ValueChanged(self, sender: object,
                                                                                          e0_: ERROR(
                                                                                              type=EventArgs)) -> None:
                                                            trackBar6.Value = (.ERROR: ToUInt16(?)
                                                            ushort
                                                            not supported in Python)
                                                            self.__hID_Send_Comand(
                                                                Form1.__reg_7,.ERROR: ToUInt16(?) ushort
                                                            not supported in Python)

                                                            def __trackBar7_Scroll(self, sender: object,
                                                                                   e0_: ERROR(type=EventArgs)) -> None:
                                                                numericUpDown7.Value = (.ERROR: ToUInt16(?)
                                                                ushort
                                                                not supported in Python)
                                                                self.__hID_Send_Comand(
                                                                    Form1.__reg_8,.ERROR: ToUInt16(?) ushort
                                                                not supported in Python)

                                                                def __numericUpDown7_ValueChanged(self, sender: object,
                                                                                                  e0_: ERROR(
                                                                                                      type=EventArgs)) -> None:
                                                                    trackBar7.Value = (.ERROR: ToUInt16(?)
                                                                    ushort
                                                                    not supported in Python)
                                                                    self.__hID_Send_Comand(
                                                                        Form1.__reg_8,.ERROR: ToUInt16(?) ushort
                                                                    not supported in Python)

                                                                    def __trackBar8_Scroll(self, sender: object,
                                                                                           e0_: ERROR(
                                                                                               type=EventArgs)) -> None:
                                                                        self.__hID_Send_Comand(
                                                                            Form1.__reg_16,.ERROR: ToUInt16(?) ushort
                                                                        not supported in Python)
                                                                        numericUpDown8.Value = (.ERROR: ToUInt16(?)
                                                                        ushort
                                                                        not supported in Python)

                                                                        def __numericUpDown8_ValueChanged(self,
                                                                                                          sender: object,
                                                                                                          e0_: ERROR(
                                                                                                              type=EventArgs)) -> None:
                                                                            trackBar8.Value = (.ERROR: ToUInt16(?)
                                                                            ushort
                                                                            not supported in Python)
                                                                            self.__hID_Send_Comand(
                                                                                Form1.__reg_16,.ERROR: ToUInt16(?) ushort
                                                                            not supported in Python)

                                                                            def __trackBar9_Scroll(self, sender: object,
                                                                                                   e0_: ERROR(
                                                                                                       type=EventArgs)) -> None:
                                                                                self.__hID_Send_Comand(
                                                                                    Form1.__reg_17,.ERROR: ToUInt16(?) ushort
                                                                                not supported in Python)
                                                                                numericUpDown9.Value = (
                                                                                    .ERROR: ToUInt16(?)
                                                                                ushort
                                                                                not supported in Python)

                                                                                def __numericUpDown9_ValueChanged(self,
                                                                                                                  sender: object,
                                                                                                                  e0_: ERROR(
                                                                                                                      type=EventArgs)) -> None:
                                                                                    trackBar9.Value = (
                                                                                        .ERROR: ToUInt16(?)
                                                                                    ushort
                                                                                    not supported in Python)
                                                                                    self.__hID_Send_Comand(
                                                                                        Form1.__reg_17,.ERROR: ToUInt16(?) ushort
                                                                                    not supported in Python)

                                                                                    def __button5_Click_1(self,
                                                                                                          sender: object,
                                                                                                          e0_: ERROR(
                                                                                                              type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button5.BackColor == Color.Khaki):
                                                                                            button5.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit0_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                (Form1.__output0_bit))
                                                                                        else:
                                                                                            button5.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit0_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button9_Click(self,
                                                                                                        sender: object,
                                                                                                        e0_: ERROR(
                                                                                                            type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button9.BackColor == Color.Khaki):
                                                                                            button9.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit1_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button9.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit1_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button10_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button10.BackColor == Color.Khaki):
                                                                                            button10.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit2_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button10.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit2_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button11_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button11.BackColor == Color.Khaki):
                                                                                            button11.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit3_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button11.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit3_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button12_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button12.BackColor == Color.Khaki):
                                                                                            button12.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit4_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button12.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit4_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button13_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button13.BackColor == Color.Khaki):
                                                                                            button13.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit5_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button13.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit5_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button14_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        self.__hID_Send_Comand(
                                                                                            Form1.__reg_50, 0x01)

                                                                                    def __button16_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        self.__hID_Send_Comand(
                                                                                            Form1.__reg_50, 0x02)

                                                                                    def __button15_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        self.__hID_Send_Comand(
                                                                                            Form1.__reg_50, 0x03)

                                                                                    def __button17_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        """ PLC

                                                                                        Args:
                                                                                            sender(object):
                                                                                            e0_( ERROR(type=EventArgs)):
                                                                                        """
                                                                                        if (
                                                                                                button17.BackColor == Color.Khaki):
                                                                                            button17.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit0_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                (Form1.__output0_bit))
                                                                                        else:
                                                                                            button17.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit0_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button19_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button19.BackColor == Color.Khaki):
                                                                                            button19.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit1_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button19.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit1_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button21_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button21.BackColor == Color.Khaki):
                                                                                            button21.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit2_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button21.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit2_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button22_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button22.BackColor == Color.Khaki):
                                                                                            button22.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit3_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button22.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit3_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button20_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button20.BackColor == Color.Khaki):
                                                                                            button20.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit4_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button20.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit4_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button18_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button18.BackColor == Color.Khaki):
                                                                                            button18.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit5_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button18.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit5_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button23_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button23.BackColor == Color.Khaki):
                                                                                            button23.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit6_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button23.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit6_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button24_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button24.BackColor == Color.Khaki):
                                                                                            button24.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output0_bit |= Form1.__bit7_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)
                                                                                        else:
                                                                                            button24.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output0_bit &= Form1.__bit7_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_30,
                                                                                                Form1.__output0_bit)

                                                                                    def __button29_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button29.BackColor == Color.Khaki):
                                                                                            button29.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit0_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button29.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit0_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button31_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button31.BackColor == Color.Khaki):
                                                                                            button31.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit1_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button31.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit1_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button33_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button33.BackColor == Color.Khaki):
                                                                                            button33.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit2_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button33.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit2_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button34_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button34.BackColor == Color.Khaki):
                                                                                            button34.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit3_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button34.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit3_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button32_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button32.BackColor == Color.Khaki):
                                                                                            button32.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit4_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button32.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit4_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button30_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button30.BackColor == Color.Khaki):
                                                                                            button30.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit5_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button30.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit5_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button28_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button28.BackColor == Color.Khaki):
                                                                                            button28.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit6_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button28.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit6_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button27_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button27.BackColor == Color.Khaki):
                                                                                            button27.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output1_bit |= Form1.__bit7_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)
                                                                                        else:
                                                                                            button27.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output1_bit &= Form1.__bit7_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_31,
                                                                                                Form1.__output1_bit)

                                                                                    def __button37_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button37.BackColor == Color.Khaki):
                                                                                            button37.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit0_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button37.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit0_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button39_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button39.BackColor == Color.Khaki):
                                                                                            button39.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit1_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button39.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit1_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button41_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button41.BackColor == Color.Khaki):
                                                                                            button41.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit2_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button41.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit2_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button42_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button42.BackColor == Color.Khaki):
                                                                                            button42.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit3_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button42.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit3_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button40_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button40.BackColor == Color.Khaki):
                                                                                            button40.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit4_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button40.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit4_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button38_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button38.BackColor == Color.Khaki):
                                                                                            button38.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit5_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button38.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit5_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button36_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button36.BackColor == Color.Khaki):
                                                                                            button36.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit6_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button36.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit6_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __button35_Click(self,
                                                                                                         sender: object,
                                                                                                         e0_: ERROR(
                                                                                                             type=EventArgs)) -> None:
                                                                                        if (
                                                                                                button35.BackColor == Color.Khaki):
                                                                                            button35.BackColor = (
                                                                                                Color.PaleGreen)
                                                                                            Form1.__output2_bit |= Form1.__bit7_set
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)
                                                                                        else:
                                                                                            button35.BackColor = (
                                                                                                Color.Khaki)
                                                                                            Form1.__output2_bit &= Form1.__bit7_res
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_32,
                                                                                                Form1.__output2_bit)

                                                                                    def __trackBar10_Scroll(self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                        numericUpDown10.Value = (
                                                                                            .ERROR: ToUInt16(?)
                                                                                        ushort
                                                                                        not supported in Python)
                                                                                        self.__hID_Send_Comand(
                                                                                            Form1.__reg_14,.ERROR: ToUInt16(?) ushort
                                                                                        not supported in Python)

                                                                                        def __numericUpDown10_ValueChanged(
                                                                                                self, sender: object,
                                                                                                e0_: ERROR(
                                                                                                    type=EventArgs)) -> None:
                                                                                            trackBar10.Value = (
                                                                                                .ERROR: ToUInt16(?)
                                                                                            ushort
                                                                                            not supported in Python)
                                                                                            self.__hID_Send_Comand(
                                                                                                Form1.__reg_14,.ERROR: ToUInt16(?) ushort
                                                                                            not supported in Python)

                                                                                            def __trackBar11_Scroll(
                                                                                                    self,
                                                                                                    sender: object,
                                                                                                    e0_: ERROR(
                                                                                                        type=EventArgs)) -> None:
                                                                                                numericUpDown16.Value = (
                                                                                                    .ERROR: ToUInt16(?)
                                                                                                ushort
                                                                                                not supported in Python)
                                                                                                self.__hID_Send_Comand(
                                                                                                    Form1.__reg_12,.ERROR: ToUInt16(?) ushort
                                                                                                not supported in Python)

                                                                                                def __numericUpDown16_ValueChanged(
                                                                                                        self,
                                                                                                        sender: object,
                                                                                                        e0_: ERROR(
                                                                                                            type=EventArgs)) -> None:
                                                                                                    trackBar11.Value = (
                                                                                                        .ERROR: ToUInt16(?)
                                                                                                    ushort
                                                                                                    not supported in Python)
                                                                                                    self.__hID_Send_Comand(
                                                                                                        Form1.__reg_12,.ERROR: ToUInt16(?) ushort
                                                                                                    not supported in Python)

                                                                                                    def __button1_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x01)

                                                                                                    def __button3_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x02)

                                                                                                    def __button2_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x03)

                                                                                                    def __button8_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x04)

                                                                                                    def __button6_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x05)

                                                                                                    def __button26_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x06)

                                                                                                    def __button4_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        if (
                                                                                                                button4.Text == "POWER ON"):
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x07)
                                                                                                            button4.Text = (
                                                                                                                "POWER OFF")
                                                                                                        else:
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x08)
                                                                                                            button4.Text = (
                                                                                                                "POWER ON")

                                                                                                    def __button50_Click(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x09)

                                                                                                    def __comboBox1_SelectedIndexChanged(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_50,
                                                                                                            0x00)

                                                                                                    def __numericUpDown12_ValueChanged(
                                                                                                            self,
                                                                                                            sender: object,
                                                                                                            e0_: ERROR(
                                                                                                                type=EventArgs)) -> None:
                                                                                                        self.__hID_Send_Comand(
                                                                                                            Form1.__reg_51,.ERROR: ToUInt32(?) uint
                                                                                                        not supported in Python)

                                                                                                        def __button7_Click(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_40,
                                                                                                                0x01)

                                                                                                        def __numericUpDown13_ValueChanged(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __numericUpDown15_ValueChanged(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __numericUpDown11_ValueChanged(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __groupBox7_Enter(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __form1_Load(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __tabPage2_Click(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __button47_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "1")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x03)

                                                                                                        def __button47_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "1")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button46_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "1")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x01)

                                                                                                        def __button46_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "1")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button49_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "3")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x03)

                                                                                                        def __button49_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "3")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button48_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "3")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x01)

                                                                                                        def __button48_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "3")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button43_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "2")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x01)

                                                                                                        def __button43_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "2")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button25_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "2")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x03)

                                                                                                        def __button25_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "2")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button45_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "4")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x03)

                                                                                                        def __button45_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "4")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button44_MouseDown(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "4")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x01)

                                                                                                        def __button44_MouseUp(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            comboBox1.Text = (
                                                                                                                "4")
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x02)

                                                                                                        def __button45_Click(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __button51_Click(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            pass

                                                                                                        def __button52_Click(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            data = Utils.newArrayOfBytes(
                                                                                                                Form1.__report_length,
                                                                                                                0)
                                                                                                            data[0] = (
                                                                                                                2)
                                                                                                            Form1.__random.ERROR: NextBytes(
                                                                                                                byte[])
                                                                                                            void
                                                                                                            not supported in Python
                                                                                                            Form1.__device.WriteReport(
                                                                                                                HidReport(
                                                                                                                    Form1.__report_length,
                                                                                                                    HidDeviceData(
                                                                                                                        data,
                                                                                                                        HidDeviceData.ReadStatus.Success)))  # error

                                                                                                        def __hID_Write(
                                                                                                                self,
                                                                                                                bufer: bytearray) -> None:
                                                                                                            bufer[0] = (
                                                                                                                2)
                                                                                                            Form1.__device.WriteReport(
                                                                                                                HidReport(
                                                                                                                    Form1.__report_length,
                                                                                                                    HidDeviceData(
                                                                                                                        bufer,
                                                                                                                        HidDeviceData.ReadStatus.Success)))  # error

                                                                                                        @staticmethod
                                                                                                        def __onReport(
                                                                                                                report: HidReport) -> None:
                                                                                                            """ Читати USB буфер

                                                                                                            Args:
                                                                                                                report(HidReport):
                                                                                                            """
                                                                                                            if (
                                                                                                                    Form1.__attached == False):
                                                                                                                pass
                                                                                                            else:
                                                                                                                Form1.__buffer_usb_tx = (
                                                                                                                    report.Data)

                                                                                                        @staticmethod
                                                                                                        def __deviceAttachedHandler() -> None:
                                                                                                            """ Включити Подію читання USB """
                                                                                                            Form1.__attached = True
                                                                                                            Form1.__device.ReadReport(
                                                                                                                OnReport)  # error

                                                                                                        @staticmethod
                                                                                                        def __deviceRemovedHandler() -> None:
                                                                                                            """ USB відключено(помилка) """
                                                                                                            Form1.__attached = False

                                                                                                        def __form1_FormClosed(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: FormClosedEventArgs) -> None:
                                                                                                            pass

                                                                                                        def __form1_FormClosing(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: FormClosingEventArgs) -> None:
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x04)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                0x08)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_1,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_2,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_3,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_4,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_5,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_6,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_7,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_8,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_9,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_10,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_11,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_12,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_13,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_14,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_15,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_16,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_17,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_30,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_31,
                                                                                                                0)
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_32,
                                                                                                                0)

                                                                                                        def __comboBox2_SelectedIndexChanged(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            if ((
                                                                                                            comboBox2.SelectedItem) == "V1"):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    0])
                                                                                                            if ((
                                                                                                            comboBox2.SelectedItem) == "C1"):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    1])
                                                                                                            if ((
                                                                                                            comboBox2.SelectedItem) == "CMS"):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    2])
                                                                                                            if ((
                                                                                                            comboBox2.SelectedItem) == "GLA"):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    3])
                                                                                                            if (
                                                                                                                    Form1.__device is None):
                                                                                                                return
                                                                                                            else:
                                                                                                                Form1.__device.OpenDevice()  # error
                                                                                                                Form1.__device.Inserted += (
                                                                                                                    DeviceAttachedHandler)
                                                                                                                Form1.__device.Removed += (
                                                                                                                    DeviceRemovedHandler)
                                                                                                                Form1.__device.MonitorDeviceEvents = (
                                                                                                                    True)
                                                                                                                Form1.__device.ReadReport(
                                                                                                                    OnReport)  # error

                                                                                                        def __readDevice(self) -> None:
                                                                                                            comboBox2.Items.Clear()  # error
                                                                                                            self.__devices = (Utils.newArray(4,None))
                                                                                                            self.__devices[0] = ( HidDevices.Enumerate(self.__device_vid, self.__v1_pid)
                                                                                                                # error .FirstOrDefault() # error )
                                                                                                                Form1.__devices[1] = (HidDevices.Enumerate(self.__device_vid, self.__c1_pid)  # error .FirstOrDefault() # error )
                                                                                                            Form1.__devices[
                                                                                                                2] = (
                                                                                                                HidDevices.Enumerate(
                                                                                                                    self.__device_vid,
                                                                                                                    self.__cms_pid)
                                                                                                                # error .FirstOrDefault() # error )
                                                                                                                Form1.__devices[3] = (HidDevices.Enumerate(self.__device_vid, self.__ga_pid)  # error .FirstOrDefault() # error )
                                                                                                            if (
                                                                                                                    Form1.__devices[
                                                                                                                        3] is not None):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    3])
                                                                                                            comboBox2.Items.Add(
                                                                                                                "GLA")  # error
                                                                                                            comboBox2.Text = (
                                                                                                                "GLA")
                                                                                                            if (
                                                                                                                    Form1.__devices[
                                                                                                                        2] is not None):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    2])
                                                                                                            comboBox2.Items.Add(
                                                                                                                "CMS")  # error
                                                                                                            comboBox2.Text = (
                                                                                                                "CMS")
                                                                                                            if (
                                                                                                                    Form1.__devices[
                                                                                                                        1] is not None):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    1])
                                                                                                            comboBox2.Items.Add(
                                                                                                                "C1")  # error
                                                                                                            comboBox2.Text = (
                                                                                                                "C1")
                                                                                                            if (
                                                                                                                    Form1.__devices[
                                                                                                                        0] is not None):
                                                                                                                Form1.__device = (
                                                                                                                Form1.__devices[
                                                                                                                    0])
                                                                                                            comboBox2.Items.Add(
                                                                                                                "V1")  # error
                                                                                                            comboBox2.Text = (
                                                                                                                "V1")

                                                                                                        def __comboBox2_MouseClick(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: MouseEventArgs) -> None:
                                                                                                            self.__readDevice()

                                                                                                        def __button51_Click_1(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            self.__hID_Send_Comand(
                                                                                                                Form1.__reg_50,
                                                                                                                10)

                                                                                                        def __button52_Click_1(
                                                                                                                self,
                                                                                                                sender: object,
                                                                                                                e0_: ERROR(
                                                                                                                    type=EventArgs)) -> None:
                                                                                                            Form1.__device.ReadReport(
                                                                                                                OnReport)  # error

                                                                                                        # static constructor for class Form1
                                                                                                        @staticmethod
                                                                                                        def _static_ctor():
                                                                                                            Form1.__random = ERROR: Constructor.ctor()
                                                                                                            not supported in Python
                                                                                                            Form1.__buffer_usb_rx = Utils.newArrayOfBytes(
                                                                                                                Form1.__page,
                                                                                                                0)
                                                                                                            Form1.__buffer_usb_tx = Utils.newArrayOfBytes(
                                                                                                                Form1.__page,
                                                                                                                0)]]]]]]]]

                                                                                                    Form1._static_ctor()


try:
    objDev = hidDev()
    objDev.Start()

    objDev.ReadDevice())

finally:
    objDev.Close()