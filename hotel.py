import hotel
from datetime import date

hotel = [
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
    [[], [], [], [], [], [], ],
]

def resv_habitacion(piso, num_habi, nombre, apellido, rut):
    if not hotel[piso][num_habi]:  
        hotel[piso][num_habi] = nombre
        hotel[piso][num_habi] [nombre] = apellido
        hotel[piso][num_habi] [nombre] [apellido]= rut
        print(f"Reserva realizada para {nombre, apellido,rut} en el piso {piso}, habitacion {num_habi}.")
    else:
        print(f"Estimad@ {nombre, apellido, rut}, la habitacion {num_habi} del piso {piso} se encuentra ocupada, salir al menu principal.")

def anular_reserva(piso, num_habi, nombre , apellido, rut):
    if not hotel[piso][num_habi]:  
        hotel[piso][num_habi] = nombre
        hotel[piso][num_habi] [nombre] = apellido
        hotel[piso][num_habi] [nombre] [apellido]= rut
        print(f"Reserva anulada  para {nombre, apellido,rut} en el piso {piso}, habitacion {num_habi}.")
    else:
        print(f"Estimad@/a {nombre, apellido ,rut }, la habitacion {num_habi} del piso {piso} a anulado se reserva sera dirigido al menu principal.")        

def guardar_reserva(piso, num_habi, nombre, apellido, rut): 
    with open("hotel.csv", "w") as archivo:
        archivo.write(f"Su habitacion esta en el piso {piso}, numero {num_habi}. Gracias por reserva, {nombre, apellido, rut }.")

def buscar_habitacion(hotel): #op2 saber que piso estas 
    for i, piso in enumerate(hotel): 
        for m, habitacion in enumerate(piso):
            if not habitacion:
                print(f"Habitacion {i} del piso {m} esta disponible.")
            else:
                print(f"Habitacion {i} del piso {m} no esta disponible.")
            
def ver_estado(hotel): # op3 se supone que ve el estado de que se ebcuebtra la reserva
    for i, piso in enumerate(hotel):
        for m, habitacion in enumerate(piso):
            if not habitacion:
                print(f"Habitacion {i} del piso {m} disponible.")
            else:
                print(f"Habitacion {i} del piso {m} no esta disponible.") 

habitaciones_premium_piso_5 = 100000
habitaciones_piso_4 = 60000
habitacion_normal = 30000

def guardar(hotel):
     with open("hotel.csv", "w") as archivo:
        archivo.write


        
while True:

    print("Bienvenido al hotel shimy duoc ")
    print("""
******** Este es el menu principal ********
1. Desea Reservar una habitacion.
2. Desea Buscar habitaciones.
3. ver estado de la habitacion.
4. Ver ventas diarias 
5. Guardar  
    """)
    op = int(input("Seleccione una opcion: "))
    match op:
        case(1):# 1. Desea Reservar una habitacion.
            piso = int(input("Ingrese el piso: "))
            num_habi = int(input("Ingrese el numero de su habitacion: "))
            nombre = input("Ingrese su nombre para la reserva: ")
            apellido = input("ingrese su apellido")
            rut =("ingrese su rut")
            resv_habitacion(piso, num_habi, nombre,apellido, rut)
            guardar_reserva(piso, num_habi, nombre, apellido, rut )
            anular_reserva(piso,num_habi,nombre,apellido, rut)
        case (2): # 2. Desea Buscar habitaciones. 
            for piso in hotel:
                print(piso)
                buscar_habitacion(hotel)
        case (3): # 3. ver estado de la habitacion. 
            ver_estado(hotel)
        case (4): # 4. Ver ventas diarias
            ventas_diarias
            print("las ventas diarias son ", ventas_diarias)
            
            print("")
        case (5): # 5. Guardar 
            guardar_reserva
        case (6):
            print("usted ha salido")
            break    
        case (_):
            print("opcion invalida, ingresa una opcion valida, por favor ")