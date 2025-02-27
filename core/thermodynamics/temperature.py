"""
TODO: MAKE A DOC FOR THIS FILE
"""
__all__ = ['Temperature']
try:
    from .temperature_error import _TemperatureError, _UndefinedStateError, _KeyTypeError
    from typing import Union
    from decimal import Decimal
except ImportError:
    from temperature_error import _TemperatureError, _UndefinedStateError, _KeyTypeError
    from typing import Union
    from decimal import Decimal

global kelvinConstant, rankinDivConstant, rankinRedivConstant, rankinStatConstant
kelvinConstant: Decimal = Decimal('273.15')
rankinStatConstant: Decimal = Decimal('491.67')
rankinRedivConstant: Decimal = Decimal('0.55555555555')
rankinDivConstant: Decimal = Decimal('1.8')

def fahrenMethod(target, status: Union[str, None]) -> Decimal:
    target = Decimal(target)
    if status == 'to fehren':
        result = target * Decimal('1.8') + Decimal('32')
        return result

    elif status == 'to kelvin&celsius':
        result = (target - Decimal('32')) / Decimal('1.8')
        return result
        
    raise _UndefinedStateError(status)

class Temperature:
    """
        FUNCTIONS:
            All functions take two arguments (Temperature, Key)

                Available FUNCTIONS:
                            Func 1:  Kelvin(here but the number of temperature, here but the scale key).
                            Func 2:  Fahrenheit(here but the number of temperature, here but the scale key).
                            Func 3:  Celsius(here but the number of temperature, here but the scale key).

                Available CASES:
                            Case 1:  Use the scale key 'K or k' if the temperature number from Kelvin. 
                            Case 2:  Use the scale key 'F or f' if the temperature number from Fahrenheit.
                            Case 3:  Use the scale key 'C or c' if the temperature number from Celsius.

         USES:
            If you want to switch between temperature gauges,
            Use the name of the scale you want to convert to,
            then put the temperature and the symbol of the scale from which this temperature came.

        
        CREATED BY: Muhammed Alkohawaldeh
        CLASS VERSION: 0.0.1(beta)
    
    """



   #TODO:   عدل على الدالة __init__ لكي تسمح بصنع مقاييس حرارة مختلفة بالاسم الذي تريد بالطريقة التي تريد 
    def __init__(self, Temperature, Key):
        self.__Temperature = Temperature
        self.__Key = Key
        
        # Not sure about it yet
    def __str__(self):
        return self.__Temperature
        

    @staticmethod
    def Kelvin(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Kelvin
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)

        if type(Temperature) not in [int, float]:
            raise TypeError('The Data type must be an integer or float')

        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')

        if Key in ['K', 'k', 'Kelvin']:
            return float(Temperature)

        elif Key in ['C', 'c', 'Celsius']:
            return float(Temperature + kelvinConstant)

        elif Key in ['F', 'f', 'Fahrenheit']:
            Temperature = fahrenMethod(target = Temperature, status = 'to kelvin&celsius')
            Temperature += kelvinConstant 
            return float(Temperature)
        
        elif Key.lower() in ['r', 'rankin']:
            return float(Temperature)

        raise _TemperatureError(Key)


    @staticmethod
    def Celsius(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Celsius
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)

        if type(Temperature) not in [int, float]:
            raise TypeError('The Data type must be an integer or float')

        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')

        if Key in ['K', 'k', 'Kelvin']:
            return float(Temperature - kelvinConstant)

        elif Key in ['C', 'c', 'Celsius']:
            return float(Temperature)

        elif Key in ['F', 'f', 'Fahrenheit']:
            return float(fahrenMethod(target = Temperature, status = 'to kelvin&celsius'))

        elif Key.lower() in ['r', 'rankin']:
            Temperature -= rankinStatConstant
            Temperature *= rankinRedivConstant
            return float(Temperature)
       
        raise _TemperatureError(Key)


    @staticmethod
    def Fahrenheit(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Fahrenheit
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)

        if type(Temperature) not in [int, float]:
            raise TypeError('The Data type must be an integer or float')
            
        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')

        if Key.lower() in ['k', 'kelvin']:
            Temperature -= kelvinConstant # transformed from Kelvin to Celsius
            Temperature = fahrenMethod(target = Temperature, status = 'to fehren') # transformed from Celsius to Fahrenheit
            return float(Temperature)

        elif Key.lower() in ['c', 'celsius']:
            return float(fahrenMethod(target = Temperature, status = 'to fehren')) # transformed from Celsius to Fahrenheit

        elif Key.lower() in ['f', 'fahrenheit']:
            return float(Temperature)

        elif Key.lower() in ['r', 'rankin']:
            return float(Temperature)
       
        raise _TemperatureError(Key)


    @staticmethod
    def Rankin(Temperature: Union[int, float], Key: str) -> float:
        """
            This function converts the entered temperature into Fahrenheit
        
        """
        if type(Key) != str:
            raise _KeyTypeError(Key)

        if type(Temperature) not in [int, float]:
            raise TypeError('The Data type must be an integer or float')
            
        Temperature = float(Temperature)
        Temperature = Decimal(f'{Temperature}')

        if Key.lower() in ['k', 'kelvin']:
            Temperature *= rankinDivConstant
            return float(Temperature)

        elif Key.lower() in ['c', 'celsius']:
            Temperature += kelvinConstant
            Temperature *= rankinDivConstant
            return float(Temperature)

        elif Key.lower() in ['f', 'fahrenheit']:
            Temperature = fahrenMethod(target = Temperature, status = 'to kelvin&celsius')
            Temperature *= rankinDivConstant
            return float(Temperature)

        elif Key.lower() in ['r', 'rankin']:
            return float(Temperature)
       
        raise _TemperatureError(Key)

