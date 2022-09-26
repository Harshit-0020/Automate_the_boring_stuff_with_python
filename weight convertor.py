weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    print(str(weight * 0.453592) + " kilos")
else:
    print(str(weight * 2.20462) + " pounds")