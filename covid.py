print('Bienvenido al diagnostico de riesgo del COVID-19')



#inicializacion de las variables a utilizar

sospechoso = 0

paciente_de_riesgo = 0

caso_autoctono = 0



neumonia = 0

fiebre = 0

sintomas = 0

temperatura = 0

tos = 0

dificultad_respiratoria = 0

odinofagia = 0



personal_salud = 0

contacto_caso = 0

viaje_exterior = 0

zona_casos_confirmados = 0

datos_extras = 0



#Se piden los datos personales al usuario

nombre = input('Por favor, Ingrese su Nombre: ')

print('Excelente',nombre)

edad = int(input('Ahora, por favor ingrese su edad: '))



######################################################################

### verificacion si pertenece al grupo de riesgo debido a su edad ####

######################################################################



#paciente que NO es de riesgo

if edad <= 60:

    paciente_de_riesgo = 0

    print('Antes de Proceder con el diagnostico, queremos aclararle que debido a su edad, no entra en el grupo de paciente de riesgo')

    temperatura = float(input('Pero continuaremos con el diagnostico, para ello, por favor ingrese su temperatura corporal :'))

    print('\nA continuacion Responda las siguientes Preguntas con 1(uno) para SI o 0(cero) para NO\n\n')

    neumonia = int(input('Padece de Neumonia? ( 1(uno) para SI, 0(cero) para NO ): '))



    if neumonia == 1:

        sospechoso = 1

        print('Paciente',nombre,' es un caso SOSPECHOSO de COVID-19')

    elif temperatura > 37:

        fiebre = 1

        tos = int(input('Tiene Tos? ( 1(uno) para SI, 0(cero) para NO ): '))

        odinofagia = int(input('Tiene odinofagia? ( 1(uno) para SI, 0(cero) para NO ): '))

        dificultad_respiratoria = int(input('Tiene dificultad respiratoria? ( 1(uno) para SI, 0(cero) para NO ): '))

        sintomas = odinofagia + tos + dificultad_respiratoria

    else:

        print('Paciente', nombre, 'NO es un caso sospechoso y NO forma parte del Grupo de riesgo')









#paciente de riesgo

else:

    paciente_de_riesgo = 1

    print('Antes de Proceder con el diagnostico, queremos advertile que debido a su edad, usted es un paciente de riesgo')

    temperatura = float(input('Continuando con el diagnostico, por favor ingrese su temperatura corporal : '))

    print('\nA continuacion Responda las siguientes Preguntas con 1(uno) para SI o 0(cero) para NO\n\n')

    neumonia = int(input('Padece de Neumonia? ( 1(uno) para SI, 0(cero) para NO ): '))



    if neumonia == 1:

        sospechoso = 1

        print('Paciente',nombre,' es un caso SOSPECHOSO de COVID-19')

    elif temperatura > 37:

        fiebre = 1

        tos = int(input('Tiene Tos? ( 1(uno) para SI, 0(cero) para NO)'))

        odinofagia = int(input('Tiene odinofagia? ( 1(uno) para SI, 0(cero) para NO ): '))

        dificultad_respiratoria = int(input('Tiene dificultad respiratoria? ( 1(uno) para SI, 0(cero) para NO ): '))

        sintomas = odinofagia + tos + dificultad_respiratoria







if sintomas >= 1:

    print('Ya casi hemos terminado, recuerda para las siguientes Preguntas con 1(uno) para SI o 0(cero) para NO')



    personal_salud = int(input('Usted forma parte del personal de salud? ( 1(uno) para SI, 0(cero) para NO ): '))

    contacto_caso = int(input('Usted estuvo en contacto con un caso confirmado de COVID-19? ( 1(uno) para SI, 0(cero) para NO ): '))

    viaje_exterior = int(input('Usted ha viajado al exterior en las ultimas semanas? ( 1(uno) para SI, 0(cero) para NO ): '))

    zona_casos_confirmados = int(input('Usted estuvo en zonas nacionales con casos de transmision confirmados? ( 1(uno) para SI, 0(cero) para NO ): '))



    datos_extras = contacto_caso + viaje_exterior + zona_casos_confirmados





if fiebre == 1 and sintomas >= 1 and (datos_extras > 0 or personal_salud == 1):

    sospechoso = 1

    if sintomas >= 2 and contacto_caso == 0 and viaje_exterior == 0 and zona_casos_confirmados == 1:

        caso_autoctono = 1

        print('Paciente',nombre, ' es un CASO AUTOCTONO SOSPECHOSO de COVID-19')

    else:

        print('Paciente',nombre,' es un caso SOSPECHOSO de COVID-19')

elif sospechoso == 0 and edad >= 60:

    print('Paciente',nombre,'NO es un caso sospechoso, pero forma parte del Grupo de riesgo')