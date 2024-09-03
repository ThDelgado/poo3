class Animal: 

    def __init__(self, nombre:str, raza:str, edad:str, peso:str, especie:str) -> None: 

        self.nombre = nombre 
        self.edad = edad 
        self.raza = raza 
        self.peso = peso 
        self.especie = especie 



caballo = Animal("zeus", "5 años", "Pura Sangre", "450 kg", "Caballo") 

leon = Animal("Boulder", "10 años", "Atlas","130 kg", "Leon") 

  

print ("El nombre del caballo es: ", caballo.nombre) 
print("El nombre del leon es: ", leon.nombre)

 

 