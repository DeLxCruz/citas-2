import core
import os
import datetime

dictAppointments = {"data": []}


def LoadInfoappointments():
    global dictAppointments
    if core.checkFile("appointments.json"):
        dictAppointments = core.LoadInfo("appointments.json")
    else:
        core.crearInfo("appointments.json", dictAppointments)


def mainMenu():
    os.system("cls")
    isRun = True
    os.system("pause")
    os.system("cls")
    print("╔═══════════════════════════════════════════╗")
    print("║           ¡GESTIÓN DE CITAS!              ║")
    print("╠═══════════════════════════════════════════╣")
    print("║      Seleccione una opción:               ║")
    print("║                                           ║")
    print("║    1. Agregar Citas                       ║")
    print("║    2. Buscar Citas                        ║")
    print("║    3. Modificar Cita                      ║")
    print("║    4. Cancelar cita                       ║")
    print("║    5. Salir del Programa                  ║")
    print("║                                           ║")
    print("╚═══════════════════════════════════════════╝")

    try:
        opcion = int(input("-->  "))
    except ValueError:
        print("Opción no válida. Por favor seleccione una opción válida.")
        input("Presione cualquier tecla para continuar...")
        mainMenu()

    if opcion == 1:
        namePatient = validateName()
        date = validateDate()
        hour = validateTime()
        reason = validateReason()

        data = {
            'name': namePatient,
            'date': date,
            'hour': hour,
            'reason': reason,
        }

        core.crearInfo("appointments.json",data)
        dictAppointments["data"].append(data)

        print("La cita se ha agregado correctamente.")
        input("Presione cualquier tecla para continuar...")

    elif opcion == 2:
        while True:
            os.system("cls")
            print("╔════════════════════════════════════════════════╗")
            print("║              ¡BÚSQUEDA DE CITAS!               ║")
            print("╠════════════════════════════════════════════════╣")
            print("║      Seleccione una opción:                    ║")
            print("║                                                ║")
            print("║    [N] Buscar Citas Por Nombre del Paciente    ║")
            print("║    [F] Buscar Citas Por Fecha                  ║")
            print("║    [V] Volver al Menú Principal                ║")
            print("║                                                ║")
            print("╚════════════════════════════════════════════════╝")

            try:
                opcion = input("-->  ").upper()

                if opcion == "N":
                    while True:
                        nameWanted = input("Ingrese el Nombre del paciente: ").upper()
                        try:
                            nameFound = False
                            for i, j in enumerate(dictAppointments["data"]):
                                if j['name'] == nameWanted:
                                    print(f"- Nombre: {j['name']} - Fecha: {j['date']} - Motivo: {j['reason']}")
                                    nameFound = True
                            if not nameFound:
                                print("No se encontró ningún paciente con el nombre especificado.")
                            input("Presione cualquier tecla para continuar...")
                            break
                        except ValueError:
                            print("Opción no válida. Por favor seleccione una opción válida.")
                            input("Presione cualquier tecla para continuar...")

                elif opcion == "F":
                    while True:
                        date_str = input("Ingrese una fecha (formato: DD/MM/AAAA): ")
                        try:
                            fecha = datetime.datetime.strptime(date_str, "%d/%m/%Y")
                            dateWanted = fecha.strftime("%d/%m/%Y")
                            dateFound = False
                            for i, j in enumerate(dictAppointments["data"]):
                                if j['date'] == dateWanted:
                                    print(f"- Nombre: {j['name']} - Fecha: {j['date']} - Motivo: {j['reason']}")
                                    dateFound = True
                            if not dateFound:
                                print("No se encontró ningún paciente con la fecha especificada.")
                            input("Presione cualquier tecla para continuar...")
                            break
                        except ValueError:
                            print("Fecha inválida. Intente nuevamente.")
                            input("Presione cualquier tecla para continuar...")
                elif opcion == "V":
                    break

            except ValueError:
                print("Opción no válida. Por favor seleccione una opción válida.")

    elif opcion == 3:
        print('Lista de Citas:')
        try:
            for i, j in enumerate(dictAppointments["data"]):
                print(f"{i + 1} Nombre: {j['name']} - Fecha: {j['date']} - Hora: {j['hour']} - Motivo: {j['reason']}")

            appointmentSelected = int(input("Seleccione una cita: "))
            appointmentSelected -= 1

            if 0 <= appointmentSelected < len(dictAppointments["data"]):
                showSelected = dictAppointments["data"][appointmentSelected]
                os.system("cls")
                print("Cita seleccionada:")
                print(f"Nombre: {showSelected['name']}, Fecha: {showSelected['date']}, Hora: {showSelected['hour']}, Motivo: {showSelected['reason']}")

                newDate_str = input("Ingrese la nueva fecha de la cita (formato: dd/mm/aaaa): ")
                newHour_str = input("Ingrese la nueva hora de la cita (formato: hh:mm): ")

                try:
                    newDate = datetime.datetime.strptime(newDate_str, "%d/%m/%Y").strftime("%d/%m/%Y")
                    newHour = datetime.datetime.strptime(newHour_str, "%H:%M").strftime("%H:%M")

                    dictAppointments["data"][appointmentSelected]["date"] = newDate
                    dictAppointments["data"][appointmentSelected]["hour"] = newHour

                    editAppointment = dictAppointments["data"][appointmentSelected]
                    print("La cita se ha modificado correctamente.")

                    print(f"Nombre: {editAppointment['name']}, Fecha: {editAppointment['date']}, Hora: {editAppointment['hour']}, Motivo: {editAppointment['reason']}")

                    core.EditarData("appointments.json", dictAppointments)

                except ValueError:
                    print("Fecha u hora inválida. Intente nuevamente.")
            else:
                print("El número de cita seleccionado es inválido.")

        except ValueError:
            print("Opción no válida. Por favor seleccione una opción válida.")
            input("Presione cualquier tecla para continuar...")

    elif opcion == 4:
        print('Lista de Citas:')
        try:
            for i, j in enumerate(dictAppointments["data"]):
                print(f"{i + 1} Nombre: {j['name']} - Fecha: {j['date']} - Hora: {j['hour']} - Motivo: {j['reason']}")

            appointmentSelected = int(input("Seleccione una cita: "))
            appointmentSelected -= 1

            if 0 <= appointmentSelected < len(dictAppointments["data"]):
                try:
                    dictAppointments["data"].pop(appointmentSelected)
                    print("La cita se ha eliminado correctamente.")
                    core.EditarData("appointments.json", dictAppointments)
                except ValueError:
                    print("Opción no válida. Por favor seleccione una opción válida.")

        except ValueError:
            print("Opción no válida. Por favor seleccione una opción válida.")

    elif opcion == 5:
        isRun = False
        print("Gracias por usar el sistema de citas médicas.")

    else:
        print("Opción no válida. Por favor seleccione una opción válida.")
        input("Presione cualquier tecla para continuar...")
        mainMenu()

    if isRun:
        mainMenu()


def validateName():
    while True:
        name = input("Ingrese el Nombre del Citas: ").upper()
        if name == "":
            print("El nombre no puede estar vacío")
        else:
            return name


def validateDate():
    while True:
        fecha_str = input("Ingrese una fecha (formato: DD/MM/AAAA): ")

        try:
            fecha = datetime.datetime.strptime(fecha_str, "%d/%m/%Y")
            if fecha < datetime.datetime.now():
                print("La fecha de la cita no puede ser anterior a la fecha actual")
            else:
                return fecha.strftime("%d/%m/%Y")
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")


def validateTime():
    while True:
        hora_str = input("Ingrese una hora (formato: HH:MM): ")

        try:
            datetime.datetime.strptime(hora_str, "%H:%M")
            return hora_str
        except ValueError:
            print("Hora inválida. Intente nuevamente.")


def validateReason():
    while True:
        reason = input("Ingrese el Motivo de su Consulta: ")
        if reason == "":
            print("El motivo no puede estar vacío")
        elif len(reason) > 50:
            print("El motivo no puede tener más de 50 caracteres")
        else:
            return reason
