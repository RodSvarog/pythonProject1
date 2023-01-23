diameter = float(input("Enter a diameter: "))
print(f"Diameter is: {diameter} m")

radius = diameter / 2
print(f"Radius is: {radius} m")


def area():
    return radius ** 2 * 3.14


print(f"Area is: {area()} m2")
