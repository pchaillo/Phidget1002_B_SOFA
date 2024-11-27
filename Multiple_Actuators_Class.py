"""
Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2023
Propriétaire : Université de Lille - CNRS 
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).
"""

from .  import Phidget1002_0B as Phi # Ok ? => Need to be tested


def kPa_to_bar(tab_in,print_flag):
    """
    # Conversion  d'un tableau 1d de kPa en bar (titre relativement explicite)
    """
    tab_out = [] # pour appliquer la même transformation à tout le tableau python
    for i in range(len(tab_in)):
        tab_out.append(tab_in[i]/100) # on divise par 100 pcq 1 bar = 100 kPa
    if print_flag == True :
        print(tab_out)
    return tab_out


class Multiple_Actuators():
    """
    Class to connect one channel of the Phidget1002_0B output voltage

    min and max in kPa => between 0 and 3 bar
    """

    def __init__(self,min_value = 0, max_value=300,print_flag = False):

        self.actuator_list = []
        self.actuator_list.append(Phi.PhidgetOutput(serial_nb = 589531,channel = 1)) # codé en dur => faire remonter en argument de la fonction ?
        self.actuator_list.append(Phi.PhidgetOutput(serial_nb = 589531,channel = 2)) # 589531
        self.actuator_list.append(Phi.PhidgetOutput(serial_nb = 589531,channel = 3))
        self.actuator_list.append(Phi.PhidgetOutput(serial_nb = 589473,channel = 1)) # 589473
        self.actuator_list.append(Phi.PhidgetOutput(serial_nb = 589473,channel = 2))
        self.actuator_list.append(Phi.PhidgetOutput(serial_nb = 589473,channel = 3))

        self.pressure_tab = [0, 0, 0, 0, 0, 0]

        self.min = min_value
        self.max = max_value

        self.print_flag = print_flag

    def apply_pressure_tab(self,pressure_tab):
        """
        La longueur du tableau est sensé être identique au nombre d'actionneurs connectés
        """

        self.pressure_tab = kPa_to_bar(pressure_tab,self.print_flag) # ligne à commenter si l'input n'est pas en kPa
        for i in range(len(self.pressure_tab)):
            pressure = self.pressure_tab[i]
            if pressure < self.min :
                pressure = self.min
            elif pressure > self.max:
                pressure = self.max
            if self.print_flag == True :
                print(pressure)
            self.actuator_list[i].apply_pressure(pressure)

    def close_channels(self):
        """
        Pour refermer la communication avec la carte (donc remettre les pressions à 0)
        """
        for i in self.actuator_list:
            i.close_channel()
