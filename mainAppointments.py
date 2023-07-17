import os 
import datetime
import addAppointment

if __name__ == "__main__":
    isActivate = True
    opTion = 0
    while (isActivate):
        os.system("clear")
        print("╔═════════════════════════════════════════════╗")
        print("║   ¡ADMINISTRACIÓN DEL CENTRO VETERINARIO!   ║")
        print("╠═════════════════════════════════════════════╣")
        print("║        Seleccione una opción:               ║")
        print("║                                             ║")
        print("║      1. Gestión de Pacientes                ║")
        print("║      2. Gestión de Veterinarios             ║")
        print("║      3. Gestión de Citas Médicas            ║")
        print("║      4. Salir                               ║")
        print("║                                             ║")
        print("╚═════════════════════════════════════════════╝")
        try:
            opcion =int(input("-->  "))
        except ValueError:
            print("Error. Debes seleccionar una opción válida.")
            input("Presione ENTER para continuar...")
            continue
        
        if (opcion == 1):
            addAppointment.LoadInfoappointments()
            addAppointment.mainMenu()
        elif (opcion == 2):
            pass
        elif (opcion == 3):
            pass
        elif (opcion == 4):
            print("Gracias por usar el sistema :D.")
            isActivate = False