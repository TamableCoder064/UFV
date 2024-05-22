1. Clase Pokemon (2 puntos)

Atributos:

nombre: str
tipo: str
nivel: int
salud: int
ataques: list
defensas: list
Métodos:

Constructor: recibirá el nombre, tipo y nivel del pokemon, así como una lista de ataques con la siguiente estructura: 
[ 
        ["Rayo", { "Daño": 3,"Tipo": "Eléctrico"} ],
        ["Tormenta", { "Daño": 2, "Tipo": "Agua"} ],
        etc...
]

 

  Además recibirá otro lista de defensas con esta estructura (ejemplo): 

[ 
        ["Esquivar", ["Agua", "Normal", "Planta", "Fuego"] ], #la sublista son los tipos para los que es efectiva la defensa.
        ["Saltar", ["Agua", "Normal", "Planta", "Tierra"] ],
        etc...
]

AprenderAtaque: recibirá el nombre, el tipo y el daño del ataque, y lo incluirá en la lista de ataques del pokemon siempre que no exista ya. Devolverá True si lo ha aprendido o False si ya existe. 
Atacar: no recibirá nada y deberá seleccionar un ataque aleatoriamente y devolver los datos del mismo (nombre, daño y tipo).
Defender: recibirá el tipo de ataque y deberá seleccionar una defensa adecuada para ese tipo de ataque que está sufriendo (es decir que el tipo de ataque que recibe esté en la sublista de tipos de esa defensa). Si no encuentra defensa para ese tipo deberá devolver False, si encuentra una devolverá True. 
2. Clase Entrenador (1 punto)

Atributos:

nombre: str
pokemons: list de objetos Pokemon
nivel: int
Métodos:

Constructor: recibirá el nombre del entrenador, una lista de objeto pokemon y el nivel del entrenador (por defecto será 1).
ElegirPokemon: recibirá el tipo y devolverá un Pokemon de su lista de ese tipo, si no tiene ninguno de ese tipo devolverá uno al azar.
3. Clase Batalla (3 puntos)

Atributos:

entrenador1: objeto tipo Entrenador
entrenador2: objeto tipo Entrenador
Métodos:

Constructor: recibirá dos objetos de dos entrenador diferentes. 
Combate: no recibirá nada, realizará las acciones necesarias para realizar un combate 1vs1 entre dos pokemons de los entrenadores. Deberá seleccionar un pokemon de forma aleatoria para cada entrenador. Después por turnos deberá realizar un ataque del pokemon del entrenador 1 y una defensa del pokemon del entrenador 2, cambiando el turno después.
      Cada turno realizará lo siguiente: 
        - Usará un ataque del pokemon al que le toque atacar.
        - El pokemon que le toca defender deberá comprobar si tiene una defensa para ese tipo de ataque. 
               * Si tiene defensa, el daño será: el daño del ataque seleccionado divido entre 4 + el nivel del pokemon atacante dividido entre 5.
               * Si no tiene defensa, el daño será: el daño del ataque seleccionado divido entre 2 + el nivel del pokemon atacante entre 2. 
        - Se restará a la salud del pokemon defensor el resultado del daño del ataque. 
        - Cuándo uno de los pokemons en ese turno su salud quede a cero o menos ganará el otro pokemon y finalizará el combate.

       Debe mostrar los datos del combate y de cada turno en todo momento.  

 

EN CASO DE ERROR DE EJECUCIÓN SUPONE UN ERROR CRÍTICO. 

ENTREGA:

Subir 1 fichero comprimido (.zip o .rar) con tu nombre y apellidos. Este fichero debe contener 1 archivo con el nombre "examen_final_pactico.py" con el código del ejercicio. 

 

ADEVERTENCIAS: 

Si se detecta copia o se tiene alguna sospecha, se llamará a defender el examen a los alumnos involucrados mediante un examen tipo oral. De suspender este examen oral, se considerará COPIA y se reportará a la dirección del grado para que tome las medias pertinentes. 
Las entregas que no se ajusten a la norma del apartado ENTREGA, NO SERÁN EVALUADAS. 