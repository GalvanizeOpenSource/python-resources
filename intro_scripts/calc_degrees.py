temp_degrees = float(raw_input("Please enter the temperature outside:"))

celcius_to_farenheit = (temp_degrees * 1.8) + 32
farenheit_to_celcius = (temp_degrees - 32) / 1.8

output_str = 'If you input degrees in {}, the translation to {} gives us: {}'
print output_str.format('Farenheit', 'Celcius', farenheit_to_celcius)
print output_str.format('Celcius', 'Farenheit', celcius_to_farenheit)
