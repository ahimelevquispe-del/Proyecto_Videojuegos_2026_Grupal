# ============================================================
# RESACA Y HORIZONTE - ARCO MEJORADO DE VALENZUELA
# Novela Visual · Lima · San Miguel · Costa Verde
# ============================================================

# ============================================================
# CONFIGURACIÓN DE AUDIO E IMÁGENES
# ============================================================

define music_melancolia = "audio/melancolia_nocturna.ogg"
define music_tension = "audio/tension_creciente.ogg"
define music_esperanza = "audio/amanecer_esperanza.ogg"
define music_ambiental = "audio/olas_costa_verde.ogg"
define music_institucional = "audio/ambiente_campus.ogg"
define music_colapso = "audio/colapso_silencio.ogg"
define music_reflexion = "audio/reflexion_piano.ogg"
define music_reconstruccion = "audio/reconstruccion_lenta.ogg"
define music_valenzuela = "audio/valenzuela_tema.ogg"


# ============================================================
# INICIALIZACIÓN - VARIABLES DEL SISTEMA
# ============================================================

default mental_load = 2
default avoidance = 0
default drinking = 0
default impulse = 0
default prof_trust = 50
default bernard_vinculo = 50
default valenzuela_relacion = 50  # NUEVA: Relación específica con Valenzuela (0-100)
default valenzuela_interacciones = 0  # NUEVA: Contador de interacciones
default valenzuela_ultima_impresion = "neutral"  # NUEVA: Última impresión que tiene de Leo
default busco_ayuda = False
default hubo_accidente = False
default hubo_tutoria = False
default mensaje_mama_respondido = False
default enfrento_problemas = False
default termino_carrera = False
default valenzuela_ofrecido_extension = False  # NUEVA: Si ofreció prórroga
default valenzuela_sabe_verdad = False  # NUEVA: Si Leo fue honesto con ella

# ============================================================
# PERSONAJES
# ============================================================

define l = Character("Leo", color="#9b59b6")
define b = Character("Bernard", color="#e67e22")
define v = Character("Prof. Valenzuela", color="#7f8c8d")
define pensamiento = Character(None, kind=nvl, what_italic=True, what_color="#CCCCCC")
define mama = Character("Mamá", color="#e74c3c")

# ============================================================
# IMÁGENES
# ============================================================

image bg_black = Solid("#000000")
image bg_playa_noche = Transform("images/fondos/bg_playa_noche.png", size=(1920, 1080))
image bg_calle_noche = Transform("images/fondos/bg_calle_noche.png", size=(1920, 1080))
image bg_habitacion = Transform("images/fondos/bg_habitacion.png", size=(1920, 1080))
image bg_campus_tarde = Transform("images/fondos/bg_campus_tarde.png", size=(1920, 1080))
image bg_oficina = Transform("images/fondos/bg_oficina.png", size=(1920, 1080))
image bg_pasillo_universidad = Transform("images/fondos/bg_pasillo_universidad.jpeg", size=(1920, 1080))
image bg_playa_accidente = Transform("images/fondos/bg_playa_accidente.png", size=(1920, 1080))
image bg_playa_amanecer = Transform("images/fondos/bg_playa_amanecer.png", size=(1920, 1080))
image bg_malecon = Transform("images/fondos/bg_malecon.png", size=(1920, 1080))
image bg_biblioteca = Transform("images/fondos/bg_biblioteca_vacia.png", size=(1920, 1080))
image bg_cancha = Transform("images/fondos/bg_cancha_amateur.png", size=(1920, 1080))
image bg_centro_salud = Transform("images/fondos/bg_centro_salud.png", size=(1920, 1080))
image bg_cafeteria = Transform("images/fondos/bg_cafeteria_universidad.png", size=(1920, 1080))

image bernard_neutral = "images/personajes/bernard_neutral.png"
image bernard_preocupado = "images/personajes/bernard_preocupado.png"
image bernard_triste = "images/personajes/bernard_triste.png"
image bernard_feliz = "images/personajes/bernard_feliz.png"
image valenzuela_neutral = "images/personajes/valenzuela_neutral.png"
image valenzuela_firme = "images/personajes/valenzuela_firme.png"
image valenzuela_comprensiva = "images/personajes/valenzuela_comprensiva.png"
image valenzuela_preocupada = "images/personajes/valenzuela_preocupada.png"
image valenzuela_decepcionada = "images/personajes/valenzuela_decepcionada.png"
image valenzuela_orgullosa = "images/personajes/valenzuela_orgullosa.png"
transform bajar_sprite:
    yoffset 600
# ============================================================
# SCREENS
# ============================================================

screen hud_estados():
    frame:
        xalign 0.98
        yalign 0.02
        background "#00000099"
        padding (10, 10, 10, 10)
        vbox:
            text "Carga Mental: [mental_load]/10" size 13 color "#ffffff"
            text "Evasión: [avoidance]" size 13 color "#ffffff"
            text "Bebida: [drinking]%" size 13 color "#ffffff"
            text "Impulso: [impulse]" size 13 color "#ffffff"
            text "Prof. Trust: [prof_trust]" size 13 color "#ffffff"
            text "Bernard: [bernard_vinculo]" size 13 color "#ffffff"
            text "Valenzuela: [valenzuela_relacion]" size 13 color "#ffffff"

screen telefono(contacto, mensaje, hora):
    frame:
        xalign 0.5
        yalign 0.3
        xsize 400
        ysize 200
        background "#1a1a1a"
        padding (20, 20, 20, 20)
        vbox:
            text "[contacto]" size 18 color "#00ff00" bold True
            null height 10
            text "[mensaje]" size 16 color "#ffffff"
            null height 10
            text "[hora]" size 12 color "#888888" xalign 1.0

# ============================================================
# PUNTO DE INICIO
# ============================================================

label start:
    scene black
    with fade
    
    play music music_melancolia fadein 2.0
    
    "Resaca y Horizonte"
    "Una novela visual sobre quedarse, beber y aprender a elegir."
    "8 finales posibles. Tus decisiones importan."

    $ renpy.pause(3)
    
    stop music fadeout 2.0

    jump acto1_inicio

# ============================================================
# ACTO I: ESCAPE (Noche artificial)
# ============================================================

label acto1_inicio:
    scene black
    with fade
    
    play music music_ambiental fadein 2.0

    "Lima, 11:47 PM. Costa Verde, San Miguel."

    "El sonido del mar es lo único constante. Todo lo demás es ruido."

    "Tengo veintiún años, estoy en penúltimo año, y postergo la pregunta que más me pesa:"

    pensamiento "\"¿Qué haré después?\""

    "Pero esta noche, eso no importa. Esta noche solo importa el siguiente trago."

    show screen hud_estados

    scene bg_playa_noche
    with dissolve

    show bernard_neutral at center, bajar_sprite
    with dissolve

    b "Oye, ¿escuchaste lo de Marco? Ya está trabajando en esa startup."

    menu:
        "Qué bien por él.":
            $ prof_trust += 5
            $ mental_load -= 1
            b "Sí... supongo que sí."

        "Seguro se va a quemar en un mes.":
            $ avoidance += 1
            $ drinking += 10
            $ impulse += 1
            $ mental_load += 1
            b "Qué amargo estás hoy."

        "No quiero hablar de eso.":
            $ avoidance += 1
            $ drinking += 5
            $ mental_load += 1
            b "Claro. Como siempre."

    b "¿Y tú? ¿Ya pensaste en qué vas a hacer después de este ciclo?"

    menu:
        "No sé. Quizás trabajar un rato, viajar...":
            $ avoidance += 1
            $ mental_load += 1
            b "Eso dijiste el semestre pasado."

        "Tengo miedo de elegir mal.":
            $ prof_trust += 5
            $ bernard_vinculo += 5
            $ enfrento_problemas = True
            show bernard_preocupado at center, bajar_sprite
            b "Leo... es la primera vez que lo dices en voz alta."
            b "Yo también tengo miedo."

        "No hablemos de eso. Pásame la botella.":
            $ avoidance += 2
            $ drinking += 15
            $ impulse += 1
            $ mental_load += 2
            show bernard_triste at center, bajar_sprite
            b "Toma."

    if drinking >= 25:
        "El alcohol me golpea más fuerte de lo esperado."
        $ drinking += 10
        $ mental_load += 1

    scene bg_playa_noche
    with dissolve

    "Pasamos una hora en silencio."

    show bernard_neutral at center, bajar_sprite

    b "Deberíamos irnos. Mañana hay clase."

    menu:
        "Quédate un rato más.":
            $ avoidance += 1
            $ drinking += 10
            $ mental_load += 1
            show bernard_triste at center, bajar_sprite
            b "Está bien. Pero solo un rato."

        "Tienes razón. Vámonos.":
            $ prof_trust += 5
            $ mental_load -= 1
            "Asiento. Me levanto."

    hide bernard_neutral
    with dissolve

    scene bg_calle_noche
    with dissolve
    
    play music music_tension fadein 2.0

    "Caminamos de regreso."

    "El teléfono vibra. Un mensaje de mi mamá."

    show screen telefono("Mamá", "¿Ya vas llegando? Te quiero.", "23:15")

    $ renpy.pause(3)

    hide screen telefono

    menu:
        "Responder: 'Sí, ya casi llego. Te quiero.'":
            $ prof_trust += 10
            $ mental_load -= 1
            $ mensaje_mama_respondido = True
            "Escribo el mensaje. Siento un pequeño alivio."

        "Dejar en visto.":
            $ avoidance += 1
            $ mental_load += 2
            "Guardo el teléfono."

    scene bg_habitacion
    with dissolve

    "Esa noche, antes de dormir, abro la app de notas."

    "Reviso el correo de la universidad. Hay uno nuevo."

    show screen telefono("Prof. Valenzuela", "Leo, necesito verte esta semana. ¿Puedes pasar por mi oficina? Es importante.", "23:58")

    $ renpy.pause(3)

    hide screen telefono

    pensamiento "\"¿Qué querrá? No he faltado tanto... ¿o sí?\""

    menu:
        "Responder: 'Sí, profe. Mañana después de clase.'":
            $ valenzuela_relacion += 5
            $ prof_trust += 5
            $ mental_load += 1
            "Al menos respondo. Eso cuenta."

        "Dejarlo para mañana.":
            $ avoidance += 1
            $ mental_load += 2
            "Mañana lo veo. Si es urgente, me volverá a escribir."

    if mental_load >= 7:
        pensamiento "\"No puedo pensar. Todo pesa.\""
    elif mental_load >= 4:
        pensamiento "\"Tengo miedo, pero todavía puedo elegir.\""
    else:
        pensamiento "\"Mañana será otro día.\""

    $ renpy.pause(2)
    
    stop music fadeout 2.0

    jump acto2_inicio

# ============================================================
# ACTO II: OBSERVACIÓN (Tarde nublada)
# ============================================================

label acto2_inicio:
    scene black
    with fade
    
    play music music_institucional fadein 2.0

    "Tres semanas después."

    scene bg_campus_tarde
    with dissolve

    show screen hud_estados

    "La universidad se siente más pequeña cada día."

    "He evadido el correo de Valenzuela tres veces. Hoy no puedo más."

    scene bg_pasillo_universidad
    with dissolve

    "Camino hacia su oficina. El pasillo se siente más largo que nunca."

    "Veo a Valenzuela al final. Está hablando con otro estudiante. Se ve cansada."

    pensamiento "\"¿Cuántos como yo habrá visto?\""

    scene bg_oficina
    with dissolve

    show valenzuela_neutral at center, bajar_sprite
    with dissolve

    v "Leo. Gracias por venir. Siéntate."

    "Su oficina está llena de libros. Hay fotos de exalumnos en la pared. Algunos sonríen, otros no."

    v "Voy a ser directa contigo. He notado que estás... distante."

    if prof_trust < 30:
        v "Estás en riesgo de deserción. No necesito que tengas todo resuelto. Necesito que aparezcas."
        $ hubo_tutoria = True
        $ mental_load += 2
        $ valenzuela_relacion -= 5

        menu:
            "Tiene razón. He estado evadiendo.":
                $ prof_trust += 15
                $ mental_load -= 1
                $ enfrento_problemas = True
                $ valenzuela_relacion += 10
                $ valenzuela_ultima_impresion = "honesto"
                show valenzuela_comprensiva at center, bajar_sprite
                v "Me alegra escucharlo, Leo. De verdad."
                v "No te voy a mentir: la situación es seria. Pero no es irreversible."
                v "¿Qué necesitas? ¿Una prórroga? ¿Reducir carga? ¿Algo más?"
                
                menu:
                    "Una prórroga para el proyecto final.":
                        $ valenzuela_ofrecido_extension = True
                        v "Te doy dos semanas extra. Pero necesito un avance semanal."
                        v "¿Trato?"
                        "Asiento."
                        v "Bien. Y Leo... si necesitas hablar, mi puerta está abierta."
                        $ valenzuela_relacion += 5

                    "No sé qué necesito. Solo... tiempo.":
                        v "El tiempo no resuelve nada, Leo. Pero la acción sí."
                        v "Vamos a fijar metas pequeñas. ¿Te parece?"
                        $ valenzuela_relacion += 5

            "Es que no sé qué quiero hacer con la carrera.":
                $ prof_trust += 5
                $ valenzuela_relacion += 5
                $ valenzuela_sabe_verdad = True
                v "Eso es honesto. Pero la honestidad sin acción es solo otra forma de esconderse."
                v "¿Sabes cuántos estudiantes me han dicho lo mismo? Muchos."
                v "Y ¿sabes cuántos se graduaron sin saber qué querían? Más de los que imaginas."
                v "La carrera no es el destino. Es el puente."

            "No vine a que me regañen.":
                $ impulse += 2
                $ prof_trust -= 10
                $ avoidance += 1
                $ mental_load += 2
                $ valenzuela_relacion -= 15
                $ valenzuela_ultima_impresion = "defensivo"
                show valenzuela_firme at center, bajar_sprite
                v "No es un regaño, Leo. Es un espejo."
                v "Llevo quince años enseñando. He visto a cientos como tú."
                v "Algunos desaparecen. Otros vuelven. Y algunos... aprenden."
                v "¿Cuál vas a ser tú?"
                "No respondo."
                v "Piénsalo. Y vuelve cuando estés listo para hablar de verdad."
                $ valenzuela_relacion -= 5

    elif prof_trust < 50:
        v "He notado que faltaste a varias clases. ¿Todo bien?"
        $ hubo_tutoria = True
        $ valenzuela_interacciones += 1

        menu:
            "La verdad: no sé qué hacer después.":
                $ prof_trust += 10
                $ mental_load -= 1
                $ enfrento_problemas = True
                $ valenzuela_relacion += 10
                $ valenzuela_sabe_verdad = True
                show valenzuela_comprensiva at center, bajar_sprite
                v "Es una pregunta válida. No tienes que responderla hoy."
                v "Pero no desaparezcas, Leo. La ausencia no te da respuestas."
                v "¿Qué te parece si nos vemos cada dos semanas? Solo para chequear."
                
                menu:
                    "Me parece bien.":
                        $ valenzuela_relacion += 5
                        v "Bien. Entonces estamos de acuerdo."
                        v "Y Leo... si las cosas se ponen muy pesadas, hay ayuda disponible."
                        v "El centro de salud mental de la universidad es gratuito."
                        "Asiento."
                        v "Bien."

                    "No sé. Quizás.":
                        v "Piénsalo. No es una obligación. Es una opción."
                        $ valenzuela_relacion += 3

            "He estado complicado, pero ya estoy mejor.":
                $ avoidance += 1
                $ mental_load += 1
                $ valenzuela_relacion -= 5
                $ valenzuela_ultima_impresion = "evasivo"
                v "Está bien. Pero si necesitas algo, aquí estoy."
                v "No soy tu enemiga, Leo. Soy tu profesora. Hay una diferencia."
                v "Tu enemiga es la evasión. Yo solo te recuerdo que existe."

            "Todo bien, profe.":
                $ avoidance += 1
                $ prof_trust -= 5
                $ mental_load += 1
                $ valenzuela_relacion -= 10
                $ valenzuela_ultima_impresion = "mentiroso"
                show valenzuela_decepcionada at center, bajar_sprite
                v "Mmm. De acuerdo."
                v "Pero Leo... las mentiras piadosas no me convencen."
                v "He visto esa mirada antes. En otros estudiantes."
                v "Algunos volvieron. Otros no."
                "Me levanto."
                v "Leo."
                "Me detengo."
                v "Mi puerta está abierta. Cuando estés listo para la verdad."

    else:
        v "Solo quería saludarte. Vas bien. Sigue así."
        $ prof_trust += 5
        $ valenzuela_relacion += 5
        show valenzuela_comprensiva at center, bajar_sprite
        v "Me alegra verte bien, Leo."
        v "¿Y el proyecto final? ¿Cómo vas?"
        
        menu:
            "Voy avanzando. No es perfecto, pero avanza.":
                $ prof_trust += 5
                $ valenzuela_relacion += 5
                v "Eso es lo importante. No tiene que ser perfecto."
                v "Solo tiene que ser tuyo."

            "Estoy complicado, pero lo voy a terminar.":
                $ prof_trust += 10
                $ valenzuela_relacion += 10
                $ valenzuela_sabe_verdad = True
                v "Eso suena a que estás luchando. Y está bien."
                v "La lucha es parte del proceso."
                v "Si necesitas algo, avísame."

    hide valenzuela_neutral
    with dissolve

    scene bg_oficina
    with dissolve

    "Me levanto para irme."

    # ESCENA ADICIONAL CON VALENZUELA
    if valenzuela_relacion >= 50:
        v "Leo. Una cosa más."
        show valenzuela_neutral at center, bajar_sprite
        with dissolve
        v "¿Conocés a Marco? El que mencionaste en clase la semana pasada."
        "Asiento."
        v "Él también estuvo donde estás ahora. Tercer año. Quería dejarlo todo."
        v "Vino a verme. Hablamos. No fue mágico. Pero algo cambió."
        v "Hoy trabaja en esa startup. Y está bien."
        v "No te digo esto para presionarte. Te lo digo porque es posible."
        $ valenzuela_relacion += 5
        hide valenzuela_neutral
        with dissolve

    scene bg_pasillo_universidad
    with dissolve

    "Salgo de la oficina."

    if valenzuela_relacion >= 60:
        pensamiento "\"Quizás no todo está perdido.\""
    elif valenzuela_relacion >= 40:
        pensamiento "\"Al menos alguien me ve.\""
    else:
        pensamiento "\"Otra persona que espera algo de mí.\""

    $ valenzuela_interacciones += 1
    
    stop music fadeout 2.0

    # DECISIÓN CRÍTICA: Buscar ayuda o no
    menu:
        "Ir al centro de salud mental de la universidad.":
            jump decision_buscar_ayuda
        
        "Ir a la playa con Bernard.":
            jump decision_playa
        
        "Volver a casa y descansar.":
            jump decision_casa

# ============================================================
# DECISIONES CRÍTICAS DEL ACTO II
# ============================================================

label decision_buscar_ayuda:
    scene bg_centro_salud
    with dissolve
    
    play music music_reflexion fadein 2.0

    "Entro al centro de salud mental. No es fácil admitir que necesito ayuda."

    "La psicóloga me escucha. No juzga. Solo escucha."

    "Hablamos de la presión, del miedo, de la postergación."

    "Me da herramientas. No son mágicas, pero son un inicio."

    $ busco_ayuda = True
    $ mental_load -= 3
    $ avoidance -= 1
    $ enfrento_problemas = True

    "Salgo de ahí con una cita para la próxima semana."

    "Por primera vez en meses, siento que no estoy solo en esto."

    "Pienso en lo que dijo Valenzuela. 'Mi puerta está abierta.'"

    "Quizás debería tomarla en serio."

    stop music fadeout 2.0

    jump acto2_noche

label decision_playa:
    scene bg_playa_noche
    with dissolve
    
    play music music_ambiental fadein 2.0

    show bernard_neutral at center, bajar_sprite
    with dissolve

    b "¿Cómo te fue con Valenzuela?"

    menu:
        "Fue... necesaria.":
            $ prof_trust += 5
            $ mental_load -= 1
            b "Me alegra. De verdad."

        "Fue horrible. No quiero volver.":
            $ avoidance += 1
            $ mental_load += 1
            b "Ya. Pásame la botella entonces."
            $ drinking += 10

        "No quiero hablar de eso.":
            $ avoidance += 1
            $ mental_load += 1
            b "Claro. Como siempre."

    "Pasamos la noche ahí. El ciclo se repite."

    if drinking >= 30:
        "El alcohol me golpea fuerte."
        $ drinking += 10
        $ mental_load += 1

    stop music fadeout 2.0

    jump acto2_noche

label decision_casa:
    scene bg_habitacion
    with dissolve
    
    play music music_melancolia fadein 2.0

    "Llego a casa. Me tiro en la cama."

    "El techo me mira. Yo miro el techo."

    menu:
        "Abrir la laptop y trabajar en el proyecto.":
            $ prof_trust += 10
            $ mental_load -= 1
            $ enfrento_problemas = True
            "No es mucho, pero al menos avanzo algo."

        "Ver series hasta quedarme dormido.":
            $ avoidance += 1
            $ mental_load += 1
            "El tiempo pasa. El problema sigue ahí."

        "Salir a caminar sin rumbo.":
            $ mental_load -= 1
            "El aire frío me despeja un poco."

    stop music fadeout 2.0

    jump acto2_noche

# ============================================================
# ACTO II - NOCHE: PUNTO DE QUIEBRE
# ============================================================

label acto2_noche:
    scene bg_habitacion
    with dissolve
    
    play music music_tension fadein 2.0

    "Es de noche. No puedo dormir."

    "El teléfono vibra. Bernard me escribe."

    show screen telefono("Bernard", "¿Vamos mañana a la playa?", "23:45")

    $ renpy.pause(2)

    hide screen telefono

    menu:
        "Responder: 'Sí, pero esta vez sin alcohol.'":
            $ drinking -= 10
            $ bernard_vinculo += 5
            $ mental_load -= 1
            "Bernard acepta. Algo cambia."

        "Responder: 'No sé. Estoy cansado.'":
            $ avoidance += 1
            $ mental_load += 1
            "Bernard no responde."

        "Apagar el teléfono.":
            $ avoidance += 2
            $ bernard_vinculo -= 10
            $ mental_load += 2
            "El silencio gana."

    "Me acuesto. Mañana será otro día."

    $ renpy.pause(2)
    
    stop music fadeout 2.0

    jump acto3_inicio

# ============================================================
# ACTO III: CLARIDAD (Punto de decisión)
# ============================================================

label acto3_inicio:
    scene black
    with fade
    
    play music music_reflexion fadein 2.0

    "Una semana después."

    "Las decisiones que tomé me han traído hasta aquí."

    "Es tiempo de enfrentar las consecuencias."

    $ renpy.pause(2)

    # ESCENA FINAL CON VALENZUELA
    scene bg_pasillo_universidad
    with dissolve

    "Veo a Valenzuela en el pasillo. Me ve."

    show valenzuela_neutral at center, bajar_sprite
    with dissolve

    v "Leo."

    if valenzuela_relacion >= 70:
        v "¿Cómo estás? ¿De verdad?"
        $ valenzuela_interacciones += 1
        
        menu:
            "Mejor. Estoy buscando ayuda.":
                $ valenzuela_relacion += 10
                $ valenzuela_ultima_impresion = "mejorando"
                show valenzuela_orgullosa at center, bajar_sprite
                v "Eso es valiente, Leo. De verdad."
                v "No es fácil admitir que necesitamos ayuda."
                v "¿Y el proyecto?"
                
                menu:
                    "Voy avanzando. No es perfecto, pero avanza.":
                        $ prof_trust += 10
                        v "Eso es todo lo que necesito escuchar."
                        v "Sigue así."
                    
                    "Estoy complicado, pero no voy a dejarlo.":
                        $ prof_trust += 15
                        $ enfrento_problemas = True
                        v "Eso es lo importante. No rendirse."
                        v "Y recuerda: mi puerta siempre está abierta."

            "Sigo complicado. Pero estoy intentando.":
                $ valenzuela_relacion += 5
                v "Eso es suficiente, Leo. Intentar es suficiente."
                v "No tienes que tener todo resuelto."
                v "Solo tienes que seguir moviéndote."

            "Estoy bien.":
                $ avoidance += 1
                $ valenzuela_relacion -= 5
                v "Mmm. De acuerdo."
                v "Pero Leo... las mentiras piadosas no me convencen."
                v "Ya sabes dónde encontrarme."

    elif valenzuela_relacion >= 40:
        v "¿Cómo vas con el proyecto?"
        $ valenzuela_interacciones += 1
        
        menu:
            "Voy avanzando.":
                $ prof_trust += 5
                v "Bien. Sigue así."
                v "Y recuerda: si necesitas ayuda, aquí estoy."

            "Estoy complicado.":
                $ valenzuela_relacion += 5
                $ valenzuela_sabe_verdad = True
                v "Está bien admitirlo, Leo."
                v "¿Has pensado en buscar ayuda?"
                
                menu:
                    "Sí. Voy a ir al centro de salud.":
                        $ busco_ayuda = True
                        $ mental_load -= 2
                        $ valenzuela_relacion += 10
                        v "Eso es valiente. De verdad."
                        v "Y si necesitas una prórroga para el proyecto, dímelo."
                        $ valenzuela_ofrecido_extension = True

                    "No sé. Quizás.":
                        v "Piénsalo. No es una obligación. Es una opción."
                        v "Pero no te quedes solo con el peso."

            "Todo bien.":
                $ avoidance += 1
                $ valenzuela_relacion -= 5
                v "Mmm. De acuerdo."
                v "Pero Leo... ya sabes dónde encontrarme."

    else:
        v "Leo."
        $ valenzuela_interacciones += 1
        show valenzuela_decepcionada at center, bajar_sprite
        
        "No dice nada más. Solo me mira."

        menu:
            "Profe, yo...":
                $ valenzuela_relacion += 10
                v "No necesito disculpas, Leo."
                v "Necesito que decidas."
                v "¿Vas a desaparecer? ¿O vas a intentar?"
                
                menu:
                    "Voy a intentar.":
                        $ enfrento_problemas = True
                        $ valenzuela_relacion += 10
                        v "Bien. Entonces empieza hoy."
                        v "No mañana. Hoy."

                    "No sé.":
                        $ avoidance += 1
                        $ valenzuela_relacion -= 5
                        v "Entonces piénsalo. Pero rápido."
                        v "El tiempo no espera."

            "Profe, disculpe. He estado...":
                $ avoidance += 1
                $ valenzuela_relacion -= 5
                v "No necesito disculpas vacías, Leo."
                v "Necesito acción."
                v "¿Qué vas a hacer?"

    hide valenzuela_neutral
    with dissolve

    scene bg_pasillo_universidad
    with dissolve

    "Me alejo."

    if valenzuela_relacion >= 60:
        pensamiento "\"Quizás no todo está perdido.\""
    elif valenzuela_relacion >= 40:
        pensamiento "\"Al menos alguien me ve.\""
    else:
        pensamiento "\"Otra persona que espera algo de mí.\""

    $ renpy.pause(2)
    
    stop music fadeout 2.0

    # CÁLCULO DE FINALES - SISTEMA BALANCEADO
    
    # FINAL 1: AMANECER LÚCIDO (Mejor final)
    if busco_ayuda and mental_load <= 4 and prof_trust >= 55 and bernard_vinculo >= 50 and valenzuela_relacion >= 60:
        jump final_amanecer_lucido
    
    # FINAL 2: PUENTE (Final positivo parcial)
    elif mental_load <= 5 and prof_trust >= 45 and bernard_vinculo >= 55 and enfrento_problemas and valenzuela_relacion >= 50:
        jump final_puente
    
    # FINAL 3: DESERCIÓN SILENCIOSA (Final negativo por evasión)
    elif avoidance >= 4 and prof_trust < 35 and bernard_vinculo < 40 and valenzuela_relacion < 35:
        jump final_desercion_silenciosa
    
    # FINAL 4: COLAPSO (Final trágico)
    elif mental_load >= 8 and drinking >= 50 and impulse >= 3:
        jump final_colapso
    
    # FINAL 5: PAUSA NECESARIA (Final neutral positivo)
    elif busco_ayuda and 4 <= mental_load <= 6 and prof_trust >= 40 and valenzuela_relacion >= 45:
        jump final_pausa_necesaria
    
    # FINAL 6: CARRERA VACÍA (Final agridulce)
    elif prof_trust >= 65 and bernard_vinculo < 35 and mental_load >= 5:
        jump final_carrera_vacia
    
    # FINAL 7: CÍRCULO VICIOSO (Final negativo por estancamiento)
    elif drinking >= 40 and bernard_vinculo >= 50 and prof_trust < 45 and not busco_ayuda:
        jump final_circulo_vicioso
    
    # FINAL 8: RECONSTRUCCIÓN TARDÍA (Final positivo desde fracaso)
    elif prof_trust < 40 and bernard_vinculo >= 55 and mental_load <= 6 and enfrento_problemas and valenzuela_relacion >= 40:
        jump final_reconstruccion_tardia
    
    # FALLBACK: Basado en el estado más crítico
    else:
        if mental_load <= 4 and prof_trust >= 50 and valenzuela_relacion >= 55:
            jump final_amanecer_lucido
        elif mental_load <= 5 and bernard_vinculo >= 50 and valenzuela_relacion >= 45:
            jump final_puente
        elif avoidance >= 3 and prof_trust < 40 and valenzuela_relacion < 40:
            jump final_desercion_silenciosa
        elif mental_load >= 7 and drinking >= 40:
            jump final_colapso
        elif busco_ayuda and valenzuela_relacion >= 40:
            jump final_pausa_necesaria
        elif prof_trust >= 60:
            jump final_carrera_vacia
        elif drinking >= 35 and bernard_vinculo >= 45:
            jump final_circulo_vicioso
        elif bernard_vinculo >= 55 and valenzuela_relacion >= 35:
            jump final_reconstruccion_tardia
        else:
            jump final_pausa_necesaria

# ============================================================
# FINALES - 8 VARIANTES CON ARCO DE VALENZUELA
# ============================================================

label final_amanecer_lucido:
    scene bg_playa_amanecer
    with dissolve
    
    play music music_esperanza fadein 2.0

    show screen hud_estados

    "4:30 AM. Camino al malecón sin botella. Sin Bernard."

    "Solo yo. El mar. Y el frío."

    "Por primera vez en meses, mi cabeza está en silencio."

    "La terapia me ayudó. No fue mágico, pero fue real."

    "Y Valenzuela... ella también ayudó. No con soluciones, sino con preguntas."

    "Saco el teléfono. Abro las notas."

    "Escribo tres líneas:"

    pensamiento "\"Lo que me da miedo: no ser suficiente.\""
    $ renpy.pause(2)
    pensamiento "\"Lo que ya sé: no estoy solo.\""
    $ renpy.pause(2)
    pensamiento "\"Lo que puedo controlar: el siguiente paso.\""
    $ renpy.pause(3)

    "El sol empieza a salir. La garúa se disipa."

    "No tengo todas las respuestas. Pero tengo algo mejor:"

    "Tengo la capacidad de elegir."

    "Terminaré la carrera. No por el título. Sino porque quiero tener las manos limpias para construir lo que venga después."

    scene bg_oficina
    with dissolve

    show valenzuela_orgullosa at center, bajar_sprite
    with dissolve

    "Días después, en su oficina:"

    v "Leo. Vi tu proyecto final."
    v "No es perfecto. Pero es tuyo."
    v "Eso es lo que importa."
    "Sonrío."
    v "¿Y ahora? ¿Qué vas a hacer?"
    "No sé. Pero por primera vez, eso no me asusta."
    v "Bien. Sigue así."

    hide valenzuela_orgullosa
    with dissolve

    hide screen hud_estados
    
    stop music fadeout 3.0

    "Fin — Amanecer Lúcido"
    "Final 1 de 8 desbloqueado"
    
    jump menu_finales

label final_puente:
    scene bg_playa_amanecer
    with dissolve
    
    play music music_esperanza fadein 2.0

    "El amanecer llega. No cambió todo. Pero algo se movió."

    "Bernard y yo seguimos yendo a la playa. Pero ya no es el único lugar al que podemos ir."

    "Valenzuela me dio una prórroga. No fue un regalo: fue un acuerdo."

    scene bg_oficina
    with dissolve

    show valenzuela_comprensiva at center, bajar_sprite
    with dissolve

    "En su oficina:"

    v "Leo, ¿cómo vas?"
    "Le muestro el avance. No es mucho, pero es algo."
    v "Bien. Sigue así."
    v "Y recuerda: no tienes que hacerlo solo."
    "Asiento."
    v "Bien."

    hide valenzuela_comprensiva
    with dissolve

    "Todavía tengo miedo. Pero ahora sé que el miedo no es una razón para esconderse."

    "Es una razón para elegir con más cuidado."

    stop music fadeout 3.0

    "Fin — Puente"
    "Final 2 de 8 desbloqueado"
    
    jump menu_finales

label final_desercion_silenciosa:
    scene bg_habitacion
    with dissolve
    
    play music music_colapso fadein 2.0

    "Dejé de abrir el correo de la universidad hace dos semanas."

    "No avisé. No me despedí. Simplemente dejé de ir."

    "Bernard me escribe. A veces contesto. A veces no."

    scene bg_pasillo_universidad
    with dissolve

    show valenzuela_decepcionada at center, bajar_sprite
    with dissolve

    "La última vez que vi a Valenzuela:"

    v "Leo."
    "No respondí."
    v "Entiendo."
    v "Pero quiero que sepas algo."
    v "Mi puerta siempre estuvo abierta."
    v "Y siempre lo estará."
    "Seguí caminando."

    hide valenzuela_decepcionada
    with dissolve

    "El techo de mi cuarto se ha vuelto el único horizonte que miro."

    "No es un final dramático. Es el más silencioso de todos."

    stop music fadeout 3.0

    "Fin — Deserción Silenciosa"
    "Final 3 de 8 desbloqueado"
    
    jump menu_finales

label final_colapso:
    scene bg_black
    with fade
    
    play music music_colapso fadein 2.0

    "No dormí."

    "El teléfono está lleno de mensajes sin responder."

    "Pero no tengo energía para abrirlos."

    "El ruido de Lima se vuelve ensordecedor."

    "Todo es demasiado."

    with fade

    "Cierro los ojos."

    "Siento el viento frío en la cara."

    scene bg_oficina
    with dissolve

    show valenzuela_preocupada at center, bajar_sprite
    with dissolve

    "Recuerdo la última vez que vi a Valenzuela:"

    v "Leo, necesito que me escuches."
    v "Estás desapareciendo."
    v "Y no puedo dejarte caer sin intentar algo."
    v "¿Hay alguien con quien pueda hablar? ¿Familia? ¿Amigos?"
    "No respondí."
    v "Por favor, Leo. No te rindas."
    "Me fui."

    hide valenzuela_preocupada
    with dissolve

    scene black
    with Dissolve(2.0)

    "..."

    $ renpy.pause(6)
    
    stop music fadeout 3.0

    "Fin — Colapso"
    "Final 4 de 8 desbloqueado"
    
    jump menu_finales

label final_pausa_necesaria:
    scene bg_campus_tarde
    with dissolve
    
    play music music_reflexion fadein 2.0

    "Fui a ver a Valenzuela. Le dije la verdad: necesito parar."

    scene bg_oficina
    with dissolve

    show valenzuela_comprensiva at center, bajar_sprite
    with dissolve

    v "Leo, gracias por ser honesto."
    v "No es rendirse. Es reconocer tus límites."
    v "Vamos a congelar el ciclo. Y cuando estés listo, vuelves."
    v "¿Trato?"
    "Asiento."
    v "Bien. Y Leo..."
    v "Cuídate. De verdad."
    "Gracias, profe."
    v "De nada. Ahora ve a descansar."

    hide valenzuela_comprensiva
    with dissolve

    "Bernard me escribió: 'Tómate tu tiempo. Yo también voy a intentar algo distinto.'"

    "Por primera vez, el silencio no pesa."

    stop music fadeout 3.0

    "Fin — Pausa Necesaria"
    "Final 5 de 8 desbloqueado"
    
    jump menu_finales

label final_carrera_vacia:
    scene bg_biblioteca
    with dissolve
    
    play music music_melancolia fadein 2.0

    "Terminé la carrera. Con buenas notas. Con el título en la mano."

    "Pero no sé quién soy detrás de él."

    "Bernard dejó de escribirme hace meses. No lo culpo."

    scene bg_oficina
    with dissolve

    show valenzuela_neutral at center, bajar_sprite
    with dissolve

    "El día de la graduación, Valenzuela me detuvo:"

    v "Leo. Felicidades."
    "Gracias, profe."
    v "¿Estás bien?"
    "Sí. Todo bien."
    v "Mmm."
    v "Leo, el título no es el final. Es el comienzo."
    v "Ahora viene lo difícil: descubrir quién eres sin la estructura."
    v "¿Tienes un plan?"
    "No."
    v "Entonces búscalo. No te conformes con actuar un papel."
    v "Mereces más que eso."
    "No respondí."

    hide valenzuela_neutral
    with dissolve

    "Cada mañana me pongo la camisa. Cada mañana siento que actúo un papel."

    "Elegí lo correcto. Pero no me elegí a mí."

    stop music fadeout 3.0

    "Fin — Carrera Vacía"
    "Final 6 de 8 desbloqueado"
    
    jump menu_finales

label final_circulo_vicioso:
    scene bg_playa_noche
    with dissolve
    
    play music music_ambiental fadein 2.0

    show bernard_triste at center, bajar_sprite
    with dissolve

    "Seguimos yendo a la playa. Seguimos bebiendo. Seguimos sin hablar de lo que importa."

    "Valenzuela me aprobó por lástima, o por inercia. No sé cuál de las dos duele más."

    scene bg_pasillo_universidad
    with dissolve

    show valenzuela_decepcionada at center, bajar_sprite
    with dissolve

    "La última vez que la vi:"

    v "Leo."
    "Profe."
    v "Vi tu proyecto."
    v "No es tu mejor trabajo."
    "Lo sé."
    v "Pero lo terminaste."
    v "Supongo que eso cuenta para algo."
    "Supongo."
    v "Leo, ¿vas a seguir así?"
    "No sé."
    v "Piénsalo. Antes de que sea tarde."

    hide valenzuela_decepcionada
    with dissolve

    scene bg_playa_noche
    with dissolve

    show bernard_triste at center, bajar_sprite
    with dissolve

    b "Oye, ¿mañana vamos?"

    "Digo que sí. Como siempre."

    "El ciclo se repite. Y esta vez, ya no noto que se repite."

    hide bernard_triste
    with dissolve
    
    stop music fadeout 3.0

    "Fin — Círculo Vicioso"
    "Final 7 de 8 desbloqueado"
    
    jump menu_finales

label final_reconstruccion_tardia:
    scene bg_cancha
    with dissolve
    
    play music music_reconstruccion fadein 2.0

    "Perdí el ciclo. Tengo que repetir varios cursos."

    "Pero Bernard está ahí. Y por primera vez, no es para escapar juntos."

    show bernard_feliz at center, bajar_sprite
    with dissolve
    
    b "¿Empezamos de nuevo? Pero esta vez en serio."

    "Asiento."

    scene bg_pasillo_universidad
    with dissolve

    show valenzuela_comprensiva at center, bajar_sprite
    with dissolve

    "Valenzuela me detuvo en el pasillo:"

    v "Leo. Sé que perdiste el ciclo."
    "Sí."
    v "Pero vi que volviste."
    v "Eso es lo importante."
    v "No es el final. Es el comienzo."
    v "¿Necesitas ayuda con los cursos?"
    
    menu:
        "Sí, profe. Me vendría bien.":
            $ valenzuela_relacion += 10
            v "Bien. Ven a mi oficina el martes."
            v "Vamos a armar un plan."
            v "Y Leo..."
            v "No te rindas. ¿De acuerdo?"
            "De acuerdo."
            v "Bien."

        "Creo que puedo solo.":
            v "Está bien. Pero si cambias de opinión, aquí estoy."
            v "No hay vergüenza en pedir ayuda."
            v "Recuérdalo."

    hide valenzuela_comprensiva
    with dissolve

    "No es el final que imaginaba. Es más lento. Más difícil. Más honesto."

    "La reconstrucción empieza hoy."

    stop music fadeout 3.0

    "Fin — Reconstrucción Tardía"
    "Final 8 de 8 desbloqueado"
    
    jump menu_finales

# ============================================================
# MENÚ DE FINALES (GALERÍA)
# ============================================================

label menu_finales:
    scene black
    with fade
    
    "Has visto uno de los 8 finales posibles."
    
    menu:
        "Reiniciar para ver otro final":
            $ mental_load = 2
            $ avoidance = 0
            $ drinking = 0
            $ impulse = 0
            $ prof_trust = 50
            $ bernard_vinculo = 50
            $ valenzuela_relacion = 50
            $ valenzuela_interacciones = 0
            $ valenzuela_ultima_impresion = "neutral"
            $ busco_ayuda = False
            $ hubo_accidente = False
            $ hubo_tutoria = False
            $ mensaje_mama_respondido = False
            $ enfrento_problemas = False
            $ termino_carrera = False
            $ valenzuela_ofrecido_extension = False
            $ valenzuela_sabe_verdad = False
            jump start
            
        "Salir al menú principal":
            return

return
