"""
Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2023
Propriétaire : Université de Lille - CNRS 
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).

589531 - #A
589473 - #B
"""

from Phidget1002_0B import *

for i in range(3):
    channel = PhidgetOutput(serial_nb = 589473,channel = 0)
    # channel.apply_voltage(1)
    channel.apply_pressure(0)
    channel.close_channel()

for i in range(3):
    channel = PhidgetOutput(serial_nb = 589531,channel = 0)
    # channel.apply_voltage(1)
    channel.apply_pressure(0)
    channel.close_channel()

try:
    input("Press Enter to Stop\n")
except (Exception, KeyboardInterrupt):
    pass

channel.close_channel()