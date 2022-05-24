from model.device.analogdevice import AnalogDevice
from model.device.digitaldevice import DigitalDevice
from model.device.pulseddevice import PulsedDevice
from model.source.currentsource import CurrentSource
from model.source.voltagesource import VoltageSource
from model.device.operationalamplifier import OperationalAmplifier
from model.operator.binarydecimaldecoder import BinaryDecimalDecoder
from model.operator.binaryadder import BinaryAdder


def main():
    obj1 = AnalogDevice("Urk", 10, 200, 10)
    print(obj1)
    obj2 = DigitalDevice("Lol", 20, 400, 40)
    print(obj2)
    obj3 = PulsedDevice("Veres", 5, 30, 100)
    print(obj3)
    obj4 = CurrentSource("K-a4", 10)
    print(obj4)
    obj5 = VoltageSource("Ur-20_400", 150, 5)
    print(obj5)
    obj6 = OperationalAmplifier("Ka-52", 100, 300, 5)
    print(obj6)
    obj7 = BinaryDecimalDecoder("AI-45", 10, 100)
    print(obj7)
    obj8 = BinaryAdder("Ukr-49", 20, 300)
    print(obj8)


if __name__ == '__main__':
    main()
