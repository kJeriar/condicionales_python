import random
x = 20
if x > 10: #20 >10
    print("el valor de x es", x)
#else
#print else
else:
    print("el número es menor a 10")
    
edad_infante = 4
if edad_infante < 2:
    print("es un bebe")
elif edad_infante < 5:
    print("es un toolder")
else:
    print("es un niño/a")
    
# && and
temperatura = 20
esta_lloviendo = False
if temperatura >18 and not esta_lloviendo: # ! es not
    print("salgamos a pasear!")
else:
    print("quedarse a mimir")
    
# en python no hay || se usa or 
edad = 17
permiso_padres = True
if edad >=18 or permiso_padres:
    print("puedes conducir un autito")
    
x=1
y=2
z=3
if x > 2 or y > 2 or z > 2:
    print("hay uno o mas números mayor a dos")
    
# orden de prioridades de python 
# Paréntesis
# Potencia
# Multiplicación
# División
# Adición
# Sustracción

#retos 
'''
Pedir al usuario que ingrese una respuesta del 1 al 10 
y generar 3 condiciones 
1 acertaste 
2 cerca por poco y
3 lejos por mucho 
'''
# desarrollo
numero_secreto = random.randint(1, 10)

intentos = 0
max_intentos = 3
numero_valido = False
#da un limite
while intentos < max_intentos:
    entrada = input("Ingresa un número del 1 al 10: ")
# verificar si el numero es numero y si es entero 
    if entrada.isnumeric():
        numero = int(entrada)
        if 1 <= numero <= 10:
            numero_valido = True
            break
        else:
            print("El número debe estar entre 1 y 10. Intenta nuevamente.")
    else:
        print("Entrada inválida. Por favor, ingresa solo números enteros del 1 al 10.")

    intentos += 1

if numero_valido:
    if numero == numero_secreto:
        print("Adivinaste buen adivinador!")
    elif abs(numero - numero_secreto) <= 2:
        print("Cerca por poco...")
    else:
        print("Lejos por mucho...")
else:
    print("Has agotado tus intentos.")
    print("Parece que hoy no estabas preparado para este desafío. ¡quizá otro dia podemos jugamos !")


print(f"El número secreto era: {numero_secreto}")


'''numero_secreto = random.randint(1, 10)
respuesta = int(input("Ingresa un número del 1 al 10: "))
if respuesta == numero_secreto:
    print("esoooo! es justo el número")
elif abs(respuesta - numero_secreto) <= 2:
    print("cerca por poquito")
else:
    print("lejos muy muy lejos")
'''
'''
MOOD DEL DÍA
Pide al usuario que ingrese su estado de ánimo (feliz, triste, cansado, emocionado).
Según la respuesta, muestra un mensaje motivador o divertido.
'''
# desarrollo
estado = input("¿Cómo estás hoy? (feliz, triste, cansado, emocionado, nose, enojado): ").lower()
if estado == "feliz":
    print("esoooo! tienes un dia bonito, disfrútalo")
elif estado == "triste":
    print("hay dias tristes, es muy normal, animo que siempre puede mejorar")
elif estado == "cansado":
    print("lo haz dado todo, encuentra el momento para descansar")
elif estado == "emocionado":
    print("¡Qué emoción! Aprovecha esa energía para hacer locuras")
elif estado == "nose":
    print("Está bien no saber cómo te sientes. Escúchate y reconócete... es parte del proceso")
elif estado == "enojado":
    print("Doble tarea Enojarse y desenojarse, respira profundo antes de explotar")
else:
    print("No reconocí ese estado, pero te mando buena vibra igual")
'''
3 NUMERITOS
Pide tres números. Según sus valores y la suma total, el programa mostrará un mensaje. Solo una opción se mostrará, la primera que cumpla:

Si todos los números son 0: mostrar "Todos los números son cero."
Si algún número es negativo: mostrar "Tienes al menos un número negativo."
Si los tres números son iguales a 100: mostrar "¡Triple 100!"
Si todos los números son iguales: mostrar "Todos los números son iguales."
Si la suma es mayor a 300: mostrar "La suma es altísima."
Si la suma está entre 201 y 300: mostrar "La suma es alta."
Si la suma está entre 101 y 200: mostrar "La suma es media."
Si la suma es 100 o menos: mostrar "La suma es baja."
En cualquier otro caso (no debería ocurrir, pero por buenas prácticas): mostrar "Caso no contemplado. Misterio sin resolver"
'''
# Función para pedir un número válido
def pedir_numero(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.lstrip('-').isnumeric():  # permite negativos
            return int(entrada)
        else:
            print("Eso no es un número. Inténtalo otra vez, pero con ganas.")

# Pedir tres números al usuario con validación
n1 = pedir_numero("Ingresa el primer número: ")
n2 = pedir_numero("Ingresa el segundo número: ")
n3 = pedir_numero("Ingresa el tercer número: ")

suma = n1 + n2 + n3

# Evaluar condiciones en orden
if n1 == 0 and n2 == 0 and n3 == 0:
    print("Wow... ¿Tres ceros? ¿Todo bien en casa?")
elif n1 < 0 or n2 < 0 or n3 < 0:
    print("¡Hey! Veo algo de energía negativa por aquí.")
elif n1 == 100 and n2 == 100 and n3 == 100:
    print("¡Boom! Triple 100, como una aplanadora numérica.")
elif n1 == n2 == n3:
    print("Tres clones numéricos. ¡Interesante elección!")
elif suma > 300:
    print("Esa suma está por las nubes. ¡Altísima!")
elif 201 <= suma <= 300:
    print("Nada mal, tu suma está bastante alta.")
elif 101 <= suma <= 200:
    print("Una suma media, como un día tranquilo.")
elif suma <= 100:
    print("Tu suma es bajita, pero tiene personalidad.")
else:
    print("Esto no estaba en el guión... Misterio sin resolver.")
