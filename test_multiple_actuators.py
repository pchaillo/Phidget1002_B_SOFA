"""
Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2023
Propriétaire : Université de Lille - CNRS 
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).

589531 - #A
589473 - #B
"""

import Multiple_Actuators_Class as actuation


pres_tab = [ 100 ,0,0,100,0,0 ]

actuators = actuation.Multiple_Actuators()

actuators.apply_pressure_tab(pres_tab)

try:
    input("Press Enter to Stop\n")
except (Exception, KeyboardInterrupt):
    pass

actuators.close_channels()