def evaluar_persona(nombre, apellido, edad, sexo):
    # Evaluar edad
    if edad >= 18:
        print(f"{nombre} {apellido} es mayor de edad.")
    else:
        print(f"{nombre} {apellido} es menor de edad.")

    # Evaluar sexo
    if sexo.lower() == "masculino":
        print("Es un Hombre.")
    else:
        print("Es una Mujer.")


# Ejemplo de uso
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (Masculino/Femenino): ")

evaluar_persona(nombre, apellido, edad, sexo)

