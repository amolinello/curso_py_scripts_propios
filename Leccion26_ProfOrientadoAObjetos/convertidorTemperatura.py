class ConvertidorTemperatura:
    MAX_CELSIUS = 100
    MAX_FAHRENHEIT = 213

    @classmethod
    def c_f(cls, celsius):
        if celsius > cls.MAX_CELSIUS:
            raise ValueError(f'Tempeatura en Celcius demasiado alta {celsius}')
        
        return (celsius * 9/5) + 32

    @classmethod
    def f_c(cls, fahrenheith):
        if fahrenheith > cls.MAX_FAHRENHEIT:
            raise ValueError(f'Tempeatura en Fahrenheit demasiado alta {fahrenheith}')

        return fahrenheith * 32 * 5 / 9

if __name__ == '__main__':
    resultado = ConvertidorTemperatura.c_f(15)
    print(f'La temperatura en F es: {resultado:.2f}')
    resultado2 = ConvertidorTemperatura.f_c(11)
    print(f'La temperatura en C es: {resultado2:.2f}')