def celcius_to_fahrenheit(cel: float):
    # 0 deg C = 32 deg F
    fahrenheit = (cel * 9/5) + 32
    print( fahrenheit)

def fahrenheit_to_kelvin(farenheit: float):
    # 32 deg F = 273.15 K
    kelvin_temp = (farenheit - 32) * (5/9) + 273.15
    print( kelvin_temp)


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    print( celsius)

if __name__ == "__main__":
    celcius_to_fahrenheit(0)
    fahrenheit_to_kelvin(32)
    kelvin_to_celsius(300)