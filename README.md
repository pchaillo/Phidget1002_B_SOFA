# Phidget1002_B_SOFA
Python code that link the Phidget1002_B volatge output board to SOFA. That way the component could be used for actuation. Conversion function to directly apply the simulated pressure on hardware

## Getting started

Contain all the python files to connect and to use Phidget1002_0B

## Recquirement

Recquire the Phidget22 python library

```console
pip3 install Phidget22
```

Recquire also to install the Phidget library :
(https://www.phidgets.com/docs/OS_-_Linux#Non-Root-1)

Root :
```console
curl -fsSL https://www.phidgets.com/downloads/setup_linux | bash - &&\
apt-get install -y libphidget22
```
Non-Root :
```console
curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash - &&\
sudo apt-get install -y libphidget22
```

## Serial Number

Serial number of the board at Defrost :
589531 - #A
589473 - #B