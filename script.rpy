# ============================================================
# RESACA Y HORIZONTE
# Novela Visual · Lima · San Miguel · Costa Verde
# ============================================================

# ============================================================
# INICIALIZACIÓN - VARIABLES DEL SISTEMA
# ============================================================

# Variables del Pitch Deck (núcleo del prototipo)
default mental_load = 2      # Carga Mental (1-10). Bloquea opciones racionales si >= 7
default avoidance = 0        # Evasión
default drinking = 0         # Bebida / resaca
default impulse = 0          # Impulso (reaccionar sin pensar)
default prof_trust = 50      # Confianza con la profesora / responsabilidad académica

# Variables de apoyo narrativo
default bernard_vinculo = 50 # Lealtad social con Bernard
default hubo_accidente = False
default hubo_tutoria = False
default mensaje_mama_respondido = False

# ============================================================
# PERSONAJES
# ============================================================

define l = Character("Leo", color="#9b59b6")         # Morado: introspección
define b = Character("Bernard", color="#e67e22")     # Naranja: escape / calidez falsa
define v = Character("Prof. Valenzuela", color="#7f8c8d") # Gris: rutina institucional
define pensamiento = Character(None, kind=nvl, what_italic=True, what_color="#CCCCCC")
define mama = Character("Mamá", color="#e74c3c")

# ============================================================
# IMÁGENES PLACEHOLDER (paleta del Pitch Deck)
# ============================================================

# Fondos - progresión de luz por acto
image bg_black = Solid("#000000")
image bg_playa_noche = Solid("#1a1a2e")        # Acto I: noche artificial
image bg_calle_noche = Solid("#2d2d44")
image bg_habitacion = Solid("#2c1a3a")         # Morado introspección
image bg_campus_tarde = Solid("#5a5a6a")       # Acto II: tarde nublada (gris)
image bg_oficina = Solid("#4a4a4a")            # Gris institucional
image bg_playa_accidente = Solid("#1a0a1a")    # Noche del accidente
image bg_playa_amanecer = Solid("#d4a574")     # Acto III: amanecer limpio
image bg_malecon = Solid("#3a3a4a")

# Personajes (sólidos)
image bernard_neutral = Solid("#e67e22")
image bernard_preocupado = Solid("#d35400")
image bernard_triste = Solid("#a04000")
image valenzuela_neutral = Solid("#7f8c8d")
image valenzuela_firme = Solid("#5d6d7e")

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
            text "Bebida: [drinking]" size 13 color "#ffffff"
            text "Impulso: [impulse]" size 13 color "#ffffff"
            text "Prof. Trust: [prof_trust]" size 13 color "#ffffff"

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

    "Resaca y Horizonte"
    "Una novela visual sobre quedarse, beber y aprender a elegir."

    $ renpy.pause(3)

    jump acto1_inicio

# ============================================================
# ACTO I: ESCAPE (Noche artificial)
# ============================================================

label acto1_inicio:
    scene black
    with fade

    "Lima, 11:47 PM. Costa Verde, San Miguel."

    "El sonido del mar es lo único constante. Todo lo demás es ruido."

    "Tengo veintiún años, estoy en penúltimo año, y postergo la pregunta que más me pesa:"

    pensamiento "\"¿Qué haré después?\""

    "Pero esta noche, eso no importa. Esta noche solo importa el siguiente trago."

    show screen hud_estados

    scene bg_playa_noche
    with fade

    show bernard_neutral at center

    b "Oye, ¿escuchaste lo de Marco? Ya está trabajando en esa startup."

    "Marco. El que siempre sacaba diecisiete. El que tenía todo resuelto."

    menu:
        "Qué bien por él.":
            $ prof_trust += 5
            b "Sí... supongo que sí."

        "Seguro se va a quemar en un mes.":
            $ avoidance += 1
            $ drinking += 10
            $ impulse += 1
            $ mental_load += 1
            b "..."
            b "Qué amargo estás hoy."

        "No quiero hablar de eso.":
            $ avoidance += 1
            $ drinking += 5
            $ mental_load += 1
            b "Claro. Como siempre."

    b "¿Y tú? ¿Ya pensaste en qué vas a hacer después de este ciclo?"

    "La pregunta me golpea como el viento frío de la costa."

    menu:
        "No sé. Quizás trabajar un rato, viajar...":
            $ avoidance += 1
            $ mental_load += 1
            b "Eso dijiste el semestre pasado."

        "Tengo miedo de elegir mal.":
            $ prof_trust += 5
            $ bernard_vinculo += 5
            show bernard_preocupado
            b "Leo... es la primera vez que lo dices en voz alta."
            b "Yo también tengo miedo."

        "No hablemos de eso. Pásame la botella.":
            $ avoidance += 2
            $ drinking += 15
            $ impulse += 1
            $ mental_load += 2
            show bernard_triste
            b "..."
            b "Toma."

    if drinking >= 30:
        "El alcohol me golpea más fuerte de lo esperado. El mundo gira un poco."
        $ drinking += 10
        $ mental_load += 1

    scene bg_playa_noche
    with dissolve

    "Pasamos una hora en silencio. El ruido del mar llena los vacíos."

    show bernard_neutral at center

    b "Deberíamos irnos. Mañana hay clase."

    menu:
        "Quédate un rato más.":
            $ avoidance += 1
            $ drinking += 10
            $ mental_load += 1
            show bernard_triste
            b "Está bien. Pero solo un rato."

        "Tienes razón. Vámonos.":
            $ prof_trust += 5
            "Asiento. Me levanto. Las piernas me tiemblan un poco."

    hide bernard_neutral
    with dissolve

    scene bg_calle_noche
    with fade

    "Caminamos de regreso. Las calles de San Miguel están vacías."

    "El teléfono vibra. Un mensaje de mi mamá."

    show screen telefono("Mamá", "¿Ya vas llegando? Te quiero.", "23:15")

    $ renpy.pause(3)

    hide screen telefono

    menu:
        "Responder: 'Sí, ya casi llego. Te quiero.'":
            $ prof_trust += 10
            $ mental_load -= 1
            $ mensaje_mama_respondido = True
            "Escribo el mensaje. Lo envío. Siento un pequeño alivio."

        "Dejar en visto.":
            $ avoidance += 1
            $ mental_load += 2
            "Guardo el teléfono. No tengo energía para esto ahora."

    scene bg_habitacion
    with fade

    "Esa noche, antes de dormir, abro la app de notas."

    if mental_load >= 7:
        pensamiento "\"No puedo pensar. Todo pesa.\""
    elif mental_load >= 4:
        pensamiento "\"Tengo miedo, pero todavía puedo elegir.\""
    else:
        pensamiento "\"Mañana será otro día.\""

    $ renpy.pause(2)

    jump acto2_inicio

# ============================================================
# ACTO II: OBSERVACIÓN (Tarde nublada)
# ============================================================

label acto2_inicio:
    scene black
    with fade

    "Tres semanas después."

    scene bg_campus_tarde
    with fade

    show screen hud_estados

    "La universidad se siente más pequeña cada día. Como si las paredes se cerraran."

    "El correo de la universidad tiene un asunto que llevo días evitando:"

    pensamiento "\"Reunión de seguimiento - Prof. Valenzuela. Mañana, 10:00 AM.\""

    $ mental_load += 2

    # --- ESCENA DE LA TUTORÍA ---
    # Se activa siempre en el Acto II, pero el comportamiento depende de prof_trust

    scene bg_oficina
    with fade

    show valenzuela_neutral at center

    v "Leo. Gracias por venir."

    if prof_trust < 30:
        v "Voy a ser directa: estás en riesgo de deserción. No necesito que tengas todo resuelto. Necesito que aparezcas."
        $ hubo_tutoria = True
        $ mental_load += 2

        menu:
            "Tiene razón. He estado evadiendo.":
                $ prof_trust += 15
                $ mental_load -= 1
                v "Me alegra escucharlo. Fijemos un compromiso concreto."

            "Es que no sé qué quiero hacer con la carrera.":
                $ prof_trust += 5
                v "Eso es honesto. Pero la honestidad sin acción es solo otra forma de esconderse."

            "No vine a que me regañen.":
                $ impulse += 2
                $ prof_trust -= 10
                $ avoidance += 1
                $ mental_load += 2
                show valenzuela_firme
                v "No es un regaño, Leo. Es un espejo. Lo que hagas con él es tuyo."

    elif prof_trust < 50:
        v "He notado que faltaste a varias clases. ¿Todo bien?"
        $ hubo_tutoria = True

        menu:
            "La verdad: no sé qué hacer después.":
                $ prof_trust += 10
                $ mental_load -= 1
                v "Es una pregunta válida. No tienes que responderla hoy. Pero no desaparezcas."

            "He estado complicado, pero ya estoy mejor.":
                $ avoidance += 1
                $ mental_load += 1
                v "Está bien. Pero si necesitas algo, aquí estoy."

            "Todo bien, profe. No se preocupe.":
                $ avoidance += 1
                $ prof_trust -= 5
                $ mental_load += 1
                v "Mmm. De acuerdo."

    else:
        v "Solo quería saludarte. Vas bien. Sigue así."
        $ prof_trust += 5

    hide valenzuela_neutral
    with dissolve

    scene bg_campus_tarde
    with fade

    "Salgo de la oficina. El peso en el pecho no se fue, pero al menos ya no está solo."

    # --- NOCHE DEL ACCIDENTE ---
    # Se dispara si drinking + impulse son altos

    if drinking >= 30 and impulse >= 3:
        jump noche_accidente
    else:
        jump noche_normal

# --- NOCHE NORMAL ---
label noche_normal:
    scene bg_playa_noche
    with fade

    show bernard_neutral at center

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

    jump acto3_inicio

# --- NOCHE DEL ACCIDENTE ---
label noche_accidente:
    scene bg_playa_accidente
    with fade

    $ hubo_accidente = True

    show bernard_triste at center

    "La noche se fue de las manos. Demasiados tragos, demasiadas palabras sueltas."

    b "Leo, para. Ya fue suficiente."

    menu:
        "Tienes razón. Paramos.":
            $ impulse -= 1
            $ mental_load += 1
            "Me detengo. Apenas. Pero me detengo."

        "No me digas qué hacer.":
            $ impulse += 2
            $ drinking += 15
            $ avoidance += 1
            $ mental_load += 2
            "Algo se rompe. Un vaso. O algo peor. No recuerdo bien."
            b "..."
            b "Ya no sé si estás aquí o solo tu cuerpo."

    "Algo se rompió esta noche. No se deshace con una disculpa."

    $ mental_load += 2

    jump acto3_inicio

# ============================================================
# ACTO III: CLARIDAD (Amanecer limpio)
# ============================================================

label acto3_inicio:
    scene black
    with fade

    "Una semana después."

    # Calcular final según la matriz del Pitch Deck
    # Ejes: Salud Mental (mental_load bajo = alta), Éxito Académico (prof_trust), Lealtad Social (bernard_vinculo)

    # Determinar salud mental: mental_load bajo = alta
    if mental_load <= 3:
        $ salud_alta = True
        $ salud_media = False
        $ salud_baja = False
    elif mental_load <= 6:
        $ salud_alta = False
        $ salud_media = True
        $ salud_baja = False
    else:
        $ salud_alta = False
        $ salud_media = False
        $ salud_baja = True

    # Éxito académico
    if prof_trust >= 60:
        $ academico_alto = True
        $ academico_medio = False
        $ academico_bajo = False
    elif prof_trust >= 35:
        $ academico_alto = False
        $ academico_medio = True
        $ academico_bajo = False
    else:
        $ academico_alto = False
        $ academico_medio = False
        $ academico_bajo = True

    # Lealtad social
    if bernard_vinculo >= 60:
        $ lealtad_alta = True
        $ lealtad_media = False
        $ lealtad_baja = False
    elif bernard_vinculo >= 35:
        $ lealtad_alta = False
        $ lealtad_media = True
        $ lealtad_baja = False
    else:
        $ lealtad_alta = False
        $ lealtad_media = False
        $ lealtad_baja = True

    # Resolver final según matriz
    if salud_alta and academico_alto and lealtad_alta:
        jump final_amanecer_lucido
    elif salud_media and academico_alto and lealtad_alta:
        jump final_puente
    elif salud_baja and academico_bajo and lealtad_media:
        jump final_desercion_silenciosa
    elif salud_baja and academico_bajo and lealtad_baja:
        jump final_colapso
    elif salud_media and academico_medio and lealtad_media:
        jump final_pausa_necesaria
    elif salud_baja and academico_alto and lealtad_baja:
        jump final_carrera_vacia
    elif salud_baja and academico_medio and lealtad_alta:
        jump final_circulo_vicioso
    elif salud_media and academico_bajo and lealtad_alta:
        jump final_reconstruccion_tardia
    else:
        # Fallback: el más cercano por salud mental
        if salud_alta:
            jump final_amanecer_lucido
        elif salud_media:
            jump final_pausa_necesaria
        else:
            jump final_colapso

# ============================================================
# FINALES
# ============================================================

label final_amanecer_lucido:
    scene bg_playa_amanecer
    with fade

    show screen hud_estados

    "4:30 AM. Camino al malecón sin botella. Sin Bernard."

    "Solo yo. El mar. Y el frío."

    "Por primera vez en meses, mi cabeza está en silencio."

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

    hide screen hud_estados

    "Fin — Amanecer Lúcido"

    return

label final_puente:
    scene bg_playa_amanecer
    with fade

    "El amanecer llega. No cambió todo. Pero algo se movió."

    "Bernard y yo seguimos yendo a la playa. Pero ya no es el único lugar al que podemos ir."

    "Valenzuela me dio una prórroga. No fue un regalo: fue un acuerdo."

    "Todavía tengo miedo. Pero ahora sé que el miedo no es una razón para esconderse."

    "Es una razón para elegir con más cuidado."

    "Fin — Puente"

    return

label final_desercion_silenciosa:
    scene bg_habitacion
    with fade

    "Dejé de abrir el correo de la universidad hace dos semanas."

    "No avisé. No me despedí. Simplemente dejé de ir."

    "Bernard me escribe. A veces contesto. A veces no."

    "El techo de mi cuarto se ha vuelto el único horizonte que miro."

    "No es un final dramático. Es el más silencioso de todos."

    "Fin — Deserción Silenciosa"

    return

label final_colapso:
    scene bg_black
    with fade

    "No dormí."

    "El teléfono está lleno de mensajes sin responder."

    "Pero no tengo energía para abrirlos."

    "El ruido de Lima se vuelve ensordecedor."

    "Todo es demasiado."

    #scene bg_playa_accidente if hubo_accidente else bg_malecon
    with fade

    "Cierro los ojos."

    "Siento el viento frío en la cara."

    scene black
    with Dissolve(2.0)

    "..."

    $ renpy.pause(6)

    "Fin — Colapso"

    return

label final_pausa_necesaria:
    scene bg_campus_tarde
    with fade

    "Fui a ver a Valenzuela. Le dije la verdad: necesito parar."

    "Ella no me juzgó. Me dio los papeles para congelar el ciclo."

    "No es rendirse. Es reconocer que no puedo seguir corriendo sin saber hacia dónde."

    "Bernard me escribió: 'Tómate tu tiempo. Yo también voy a intentar algo distinto.'"

    "Por primera vez, el silencio no pesa."

    "Fin — Pausa Necesaria"

    return

label final_carrera_vacia:
    scene bg_oficina
    with fade

    "Terminé la carrera. Con buenas notas. Con el título en la mano."

    "Pero no sé quién soy detrás de él."

    "Bernard dejó de escribirme hace meses. No lo culpo."

    "Cada mañana me pongo la camisa. Cada mañana siento que actúo un papel."

    "Elegí lo correcto. Pero no me elegí a mí."

    "Fin — Carrera Vacía"

    return

label final_circulo_vicioso:
    scene bg_playa_noche
    with fade

    show bernard_triste at center

    "Seguimos yendo a la playa. Seguimos bebiendo. Seguimos sin hablar de lo que importa."

    "Valenzuela me aprobó por lástima, o por inercia. No sé cuál de las dos duele más."

    b "Oye, ¿mañana vamos?"

    "Digo que sí. Como siempre."

    "El ciclo se repite. Y esta vez, ya no noto que se repite."

    hide bernard_triste
    with dissolve

    "Fin — Círculo Vicioso"

    return

label final_reconstruccion_tardia:
    scene bg_malecon
    with fade

    "Perdí el ciclo. Tengo que repetir varios cursos."

    "Pero Bernard está ahí. Y por primera vez, no es para escapar juntos."

    b "¿Empezamos de nuevo? Pero esta vez en serio."

    "Asiento."

    "No es el final que imaginaba. Es más lento. Más difícil. Más honesto."

    "La reconstrucción empieza hoy."

    "Fin — Reconstrucción Tardía"

    return