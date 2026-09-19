#=======================================================================================================================
# Programmer: Nathalie Kate B. Subido
# Date: 09/19/26
# Activity: Long test 1: part 2
# Description: This program will help determine measurements about the garden based on a radius entered by the user.
#=======================================================================================================================
#This allows the use of the math library
import math

#Input stage
radius_of_garden = float(input("Enter the radius of the garden: ")) # Asks for the input to process

#Processing stage
##Calculates area and circumference using math.pi and pow()
Area = math.pi * pow(radius_of_garden, 2)
Circumference = 2 * math.pi * radius_of_garden

Square_root = math.sqrt(Area)
#Uses math.floor and math.ceil to calculate the area rounded up and down
area_rounded_down = math.floor(Area)
area_rounded_up = math.ceil(Area)

#Output Stage
print("="* 50)
print("  Processed Measurements:")
print("="* 50)
print(f"""Given radius of garden: {radius_of_garden}""")
print(f"""Area of the garden: {Area:.2f} square meters""")
print(f"""Circumference of the garden: {Circumference:.2f} meters""")
print(f"""Square_root of the area: {Square_root:.2f}""")
print(f"""Area rounded down: {area_rounded_down} square meters""")
print(f"""Area rounded up: {area_rounded_up} square meters """)
