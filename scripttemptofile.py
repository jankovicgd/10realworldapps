def celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        return "Temperatures cannot go below -273.15"
    else:
        return celsius * 9 / 5 + 32

temperatures = [10, -20, -289, 100]

file = open('temps.txt','a+')

for temp in temperatures:
    if type(celsius_to_fahrenheit(temp)) == float:
        file.write(str(celsius_to_fahrenheit(temp))+"\n")

file.close()
