"""
Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2023
Propriétaire : Université de Lille - CNRS 
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).
"""

import Sofa.Core
import Sofa.constants.Key as Key

import numpy

from . import Phidget1002_0B as Phidget1002_0B

try : # Trouver une solution propre pour la connexion à la scène ?
    import Connexion_Function_ucl as connect # ATTENTION => cette ligne dépend de la fonction de connexion utilisé (ucl_collaboration) # TODO = décoreller cette fonction de mon connecteur SOFA en python (plus propre et réutilisable) ou sinon faire une dépendance propre
    # import Connexion_Function_kais as connect # ATTENTION => cette ligne dépend de la fonction de connexion utilisé (kaiserlautern)
except :
    print("Scene connexion")


class Phidget_pressure_actuation(Sofa.Core.Controller):
        """
Fonction to apply simulation pressure in hardware trough Phidget1002_0B

Connect pneumatic chamber 3 by 3 with CavityConnect function

        """
        def __init__(self,node, module,serial_nb,print_flag = False,i=0,*args, **kwargs):

            Sofa.Core.Controller.__init__(self,args,kwargs)

            self.pressure, txt_chmbre = connect.CavityConnect_1parent(node=node,module=module,i=i)

            self.channel_1 = Phidget1002_0B.PhidgetOutput(serial_nb = serial_nb,channel = 1)
            self.channel_2 = Phidget1002_0B.PhidgetOutput(serial_nb = serial_nb,channel = 2)
            self.channel_3 = Phidget1002_0B.PhidgetOutput(serial_nb = serial_nb,channel = 3)

            self.sn = serial_nb

            if module.dyn_flag == 1:
                self.time_step = module.dt
            else :
                self.time_step = 1

            self.print_flag = print_flag


        def onAnimateBeginEvent(self,dt):
            # pres_tab = [copy(self.pressure[0].pressure.value)/self.time_step,copy(self.pressure[1].pressure.value)/self.time_step,copy(self.pressure[2].pressure.value)/self.time_step]
            pres_tab = [self.pressure[0].pressure.value/self.time_step,self.pressure[1].pressure.value/self.time_step,self.pressure[2].pressure.value/self.time_step]
            if self.print_flag == True :
                print("Pressure Applied (kPa)")
                print([self.sn,pres_tab])
            bar_tab = connect.kPa_to_bar(pres_tab)
            self.channel_1.apply_pressure(bar_tab[0])
            self.channel_2.apply_pressure(bar_tab[1])
            self.channel_3.apply_pressure(bar_tab[2])


