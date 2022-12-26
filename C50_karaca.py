def karaca(original_text, is_karaca):
    result = ""

    text = original_text.lower().split(" ")

    for word in text:
        if is_karaca:
            result += word.replace("aca", "")[::-1].replace("0", "a").replace("1", "e").replace("2", "i").replace("3", "o").replace("4", "u")
            result += " "
        else:
            result += word[::-1].replace("a", "0").replace("e", "1").replace("i", "2").replace("o", "3").replace("u", "4")
            result += "aca "

    return result

print(karaca("placa", False)) # 0c0lpaca
print(karaca("0c0lpaca", True)) # placa

print(karaca("Este es el penúltimo reto de programación del año", False)) # 1ts1aca s1aca l1aca 3m2tlún1paca 3t1raca 1daca nó2c0m0rg3rpaca l1daca 3ñ0aca
print(karaca("1ts1aca s1aca l1aca 3m2tlún1paca 3t1raca 1daca nó2c0m0rg3rpaca l1daca 3ñ0aca", True)) # este es el penúltimo reto de programación del año