def toOctal(decimal: int) -> int:
    residuos = [str(decimal % 8)]
    cociente = int(decimal / 8)

    while cociente > 0:
        residuo = cociente % 8
        residuos.append(str(residuo))
        cociente = int(cociente / 8)
    
    return int("".join(residuos)[::-1])

def toHexadecimal(decimal: int) -> str:
    converter = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F",
    }
    residuos = [str(decimal % 16)]
    cociente = int(decimal / 16)

    while cociente > 0:
        residuo = cociente % 16

        if 10 <= residuo <= 15:
            residuo = converter[residuo]

        residuos.append(str(residuo))
        cociente = int(cociente / 16)
    
    return "".join(residuos)[::-1]

print(toHexadecimal(756))