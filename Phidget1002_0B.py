"""
Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2023
Propriétaire : Université de Lille - CNRS 
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).
"""

from Phidget22.Phidget import *
from Phidget22.Devices.VoltageOutput import *


class PhidgetOutput:
    """
    Class to connect one channel of the Phidget1002_0B output voltage
    """

    def __init__(self,serial_nb,channel,debug_print_flag = False):
        self.serial_nb = serial_nb
        self.channel = channel
        self.debug_print_flag = debug_print_flag
        #INIT
        self.output = VoltageOutput()
        self.output.setDeviceSerialNumber(serial_nb)
        self.output.setChannel(channel)
        self.output.openWaitForAttachment(5000)

    def apply_voltage(self,value):
    	"""
		To apply voltage on this channel
    	"""
    	if value < 0 :
    		print("No negative voltage => set better value")
    	if value > 10 :
    		print("No more than 10V => set better value")
    	self.output.setVoltage(value)

    def apply_pressure(self,pressure):
        """
        Input : pressure : float, in bar
        To apply pressure with ED02 Rexroth electrovalve
        """
        if pressure < 0 :
        	print("No negative pressure => set better value")
        if pressure > 3 :
        	print("No more than 3bar => set better value")

        if self.debug_print_flag :
            print(self.serial_nb)
            print(self.channel)
            print(pressure)

        value = pressure * (10/3)
        
        self.apply_voltage(value)

    def close_channel(self):
    	self.output.close()

