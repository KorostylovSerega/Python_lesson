# class ChemicalElement practic 

class ChemicalElement:
    name = 'chemical element'

    def __init__(self, melting_t: [int, bool], boling_t: [int, bool]):
        self.melting_t = melting_t
        self.boling_t = boling_t


    def check_state(self, temp: [int, bool], unit: str = None, name: str = name) -> str:
        if unit:
            temp = self.temp_converter(temp, unit)

        if temp < self.melting_t:
            return f'At a temperature of {temp}°C the {name} is in a SOLID state'
        elif temp < self.boling_t:
            return f'At a temperature of {temp}°C the {name} is in a LIQUID state'
        else:
            return f'At a temperature of {temp}°C the {name} is in a GAS state'


    def temp_converter(self, temp: [int, bool], unit: str = None) -> [int, bool]:
        if unit:
            if unit in 'Kk':
                return round(temp-273.15, 1)
            elif unit in 'Ff':
                return round((temp-32)*(5/9), 1)        
        return temp
        

if __name__ == '__main__':

    Al = ChemicalElement(660, 2518.8) # object aluminium
    print(Al.check_state(550))
    print(Al.check_state(850))
    print(Al.check_state(2550))

    print(Al.check_state(823, 'k'))
    print(Al.check_state(1560, 'f'))
    print(Al.check_state(2550, 'c'))


    print(Al.check_state(823, 'k', 'Aluminium'))
    print(Al.check_state(1560, 'f', 'Aluminium'))
    print(Al.check_state(2550, None, 'Aluminium'))

    print()

    Ni = ChemicalElement(1453, 2732) # object nickel
    print(Ni.check_state(550))
    print(Ni.check_state(1550))
    print(Ni.check_state(2800))

    print(Ni.check_state(825, 'k'))
    print(Ni.check_state(2820, 'f'))
    print(Ni.check_state(2800, 'c'))


    print(Ni.check_state(825, 'k', 'Nickel'))
    print(Ni.check_state(2820, 'f', 'Nickel'))
    print(Ni.check_state(2800, None, 'Nickel'))

    print()

    Xe = ChemicalElement(-111.85, -107.05) # object xenon
    print(Xe.check_state(-120))
    print(Xe.check_state(-110))
    print(Xe.check_state(0))

    print(Xe.check_state(153, 'k'))
    print(Xe.check_state(-165, 'f'))
    print(Xe.check_state(0, 'c'))


    print(Xe.check_state(153, 'k', 'Xenon'))
    print(Xe.check_state(-165, 'f', 'Xenon'))
    print(Xe.check_state(0, None, 'Xenon'))    
