#Inicio de conexion al bot de telegram 
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler,filters, ContextTypes
# Preguntas y respuestas (por categoria)

categories = {
    "Reumatología": [
        {
            "question": "¿Cuál es la articulación que se afecta con mayor frecuencia en la condrocalcinosis?",
            "options": ["Interfalángica distal", "Sacroilíaca", "Escapulohumeral", "Rodilla", "Interfalángica proximal"],
            "answer": 3
        },
        {
            "question": "Mujer de 14 años con artrologías y exantema malar. ¿Cuál es el diagnóstico más probable?",
            "options": ["Esclerodermia", "Artritis reactiva", "Dermatitis fotosensible", "Dermatomiositis juvenil", "Lupus eritematoso sistémico"],
            "answer": 4
        },
        {
            "question": "Escolar de 12 años, presenta hace 6 días dolor en rodilla derecha con sensación de alza térmica e incapacidad funcional para caminar. Examen PA: 110/60 mmHg, FC: 100X', T°: 38.5°C; rodilla aumentada de volumen con flogosis y dolor para caminar. ¿Cuál es la conducta inmediata a seguir?",
            "options": ["Resonancia", "Aspiración articular", "Rx de rodilla", "Artrotomía", "Tomografía"],
            "answer": 1
        },
        {
            "question": "Varón de 5 años, presenta durante 3 días erupción máculo papular rosada y algunas equimosis en ambas piernas, desde hace 2 días dolor en rodillas, dolor abdominal postprandial y vómitos alimentarios. Examen: FC 88x', FR 18x', T° 37°C; pápulas rosadas confluentes, petequias en ambas piernas que se extienden a tobillos y nalgas; dolor al movilizar ambas rodillas, no signos de flogosis; abdomen: dolor difuso a la palpación profunda. ¿Cuál es el diagnóstico más probable?",
            "options": ["Trombocitopenia inmune primaria", "Vasculitis por hipersensibilidad", "Artritis reumatoide juvenil", "Poliartritis nudosa", "Púrpura de Henoch-Schönlein"],
            "answer": 4
        },
        {
            "question": "¿Cuál es la principal complicación de la hiperuricemia?",
            "options": ["Artritis", "Nefrolitiasis", "Insuficiencia renal", "Hepatitis B", "Atresia de vías biliares"],
            "answer": 0
        },
        {
            "question": "Forman parte del perfil de riesgo de la mujer a desarrollar osteoporosis, excepto…",
            "options": ["Historia familiar de osteoporosis", "Multiparidad", "Vida sedentaria", "Menopausia prematura", "Dieta rica en carnes rojas y alcohol"],
            "answer": 1
        },
        {
            "question": "¿Cuál es el primer cuadro ocular que se presenta en la artritis reactiva (síndrome de Reiter)?",
            "options": ["Escleritis", "Queratitis", "Conjuntivitis papilar", "Glaucoma ángulo cerrado", "Glaucoma ángulo abierto"],
            "answer": 2
        },
        {
            "question": "Varón de 66 años, llega a su consulta por presentar dolor intenso y tumefacción en su rodilla derecha desde el día anterior, confirmándose la presencia de un derrame sinovial a la exploración. Una radiografía de la articulación podrá aportar datos útiles para el diagnóstico, solo si el paciente sufre...",
            "options": ["Ataque de gota", "Artritis por pirofosfato cálcico", "Espondiloartopatías", "Artritis séptica", "Hemofilia"],
            "answer": 1
        },
        {
            "question": "¿Cuál de los siguientes fármacos se considera hoy en día de elección en el tratamiento de la artritis reumatoide?",
            "options": ["Prednisolona", "Ciclosporina", "Metotrexato", "Sales de oro", "D-penicilamina"],
            "answer": 2
        },
        {
            "question": "Varón de 13 años, desde hace tres días presenta dolor en rodilla derecha que le impide caminar y fiebre de 38,5°C. Al examen: rodilla derecha dolorosa, aumentada de volumen y con signos inflamatorios. Hemograma con leucocitos de 25,000 x mm³ y 10% de abastonados. ¿Cuál es el probable germen responsable de la infección?",
            "options": ["Staphylococcus aureus", "Escherichia coli", "Corynebacterium pyogenes", "Haemophilus influenzae"],
            "answer": 0
        },
    ],
    "Patología Apendicular": [
        {
            "question": "Varón de 18 años presenta desde hace 24 horas, dolor abdominal, al inicio en epigastrio, luego en fosa ilíaca derecha. Al examen: T 39°C, FC 100 x', dolor a la palpación y rebote (+) en FID. Leucocitos: 15.400/mm3 con desviación a la izquierda. ¿Cuál es la conducta a seguir?",
            "options": ["Antibioticoterapia", "Laparotomía", "Observación", "Analgésicos IV"],
            "answer": 1
        },
        {
            "question": "Gestante de 24 semanas, hace 12 horas con dolor en CID, náuseas y vómitos. Al examen: T 38.5o C, FC 120 x', FR 24 x'. Abdomen: útero ocupado, dolor a la palpación de FID, rebote (+). Laboratorio: leucocitos 14000/cm3 10% abastonados, examen de orina, normal. ¿Cuál es la prueba que facilite el diagnóstico?",
            "options": ["TEM sin contraste", "TAC con contraste", "RMN abdomen con contraste", "Ecografía abdominal"],
            "answer": 3
        },
        {
            "question": "Varón de 80 años, desde hace 2 días dolor periumbilical, alza térmica y vómitos. Al examen: abdomen distendido, RHA ausentes, dolor en FID, Rovsing (+). Laboratorio: leucocitosis con desviación izquierda, examen de orina 2-4 leucocitos/campo. ¿Cuál es el diagnóstico?",
            "options": ["Obstrucción intestinal", "Apendicitis aguda", "Diverticulitis aguda", "Pielonefritis aguda"],
            "answer": 1
        },
        {
            "question": "Mujer de 30 años, hace 18 horas presenta dolor en CID, náuseas y vómitos. Al examen T 38o C, FC 100 x', FR 20 x', PA 110/70 mmHg, abdomen dolor a la palpación en FID. Laboratorio: leucocitos 12000/ cm3, 8% abastonados. ¿Cuál es el estudio a realizar?",
            "options": ["Paracentisis diagnóstica", "Rx abdomen simple", "Ecografía abdominal", "Tránsito intestinal"],
            "answer": 2
        },
        {
            "question": "Escolar de 6 años, presenta malestar general, anorexia, dolor abdominal periumbilical de 12 horas de evolución, acompañado de vómitos sin contenido alimentario, no diarreas. Al examen: dolor a la palpación en fosa ilíaca derecha, ¿cuál es el diagnóstico probable?",
            "options": ["Apendicitis aguda", "Invaginación intestinal", "Gastroenterocolitis", "Diverticulitis"],
            "answer": 0
        },
        {
            "question": "Niño de 9 años presenta dolor abdominal de 36 horas que migra a FID, con antecedente de resfrío, al momento orofaringe congestiva. ¿Cuál es el diagnóstico más probable?",
            "options": ["Diverticulitis de Meckel", "Apendicitis aguda", "Adenitis mesentérica", "Parasitosis intestinal", "Neumonía basal derecha"],
            "answer": 2
        },
        {
            "question": "Escolar desde hace 24 horas dolor periumbilical de moderada intensidad, posteriormente vómitos y sensación febril. Examen: dolor y defensa muscular, en hemiabdomen inferior derecho, RHA aumentados, signos del rebote (+). ¿Cuál es el diagnóstico probable?",
            "options": ["Gastroenterocolitis", "Apendicitis aguda", "Adenitis mesentérica", "Invaginación intestinal", "Malrotación intestinal"],
            "answer": 1
        },
        {
            "question": "Varón de 13 años, desde hace 2 días presenta dolor abdominal con náuseas y vómitos, pérdida de apetito y constipación. Examen: T: 39°C, deshidratado, piel sudorosa. Abdomen distendido, dolor y contractura muscular en FID. Niega antecedente infeccioso. ¿Cuál es el diagnóstico más probable?",
            "options": ["Pancreatitis aguda", "Apendicitis aguda", "Adenitis mesentérica", "Obstrucción intestinal"],
            "answer": 1
        },
        {
            "question": "Mujer gestante de 28 semanas con diagnóstico de apendicitis aguda ¿Cuál es el manejo mejor recomendado?",
            "options": ["Observación", "Antibioticoterapia", "Apendicectomía laparoscópica", "Apendicectomía convencional", "Apendicectomía electiva"],
            "answer": 2
        },
        {
            "question": "Paciente varón que ingresa por dolor en fosa ilíaca derecha que se irradia a todo el abdomen. Es operado por apendicitis aguda complicada con peritonitis. Se deja dren peritoneal. ¿Cuánto tiempo debe recibir antibióticos?",
            "options": ["3 días", "1 día", "7 días", "14 días", "21 días"],
            "answer": 2
        },
    ],
    "Cardiología": [
        {
            "question": "Varón de 65 años, hospitalizado desde hace 3 días por infarto agudo de miocardio de cara inferior, en forma sostenida empieza a presentar hipotensión y disnea. Examen 80/60 mmHg FC: 102X', escasos crépitos en bases de AHT. EKG sin cambios en la relación a la inicial. ¿Cuál es el examen más adecuado para confirmar el diagnóstico?",
            "options": ["Gammagrafía cardiaca", "Coronariografía", "Ecodoppler cardíaco", "Ecocardiografía"],
            "answer": 3
        },
        {
            "question": "Varón de 45 años, acude por dolor retroesternal que se irradia hacia la mandíbula luego de esfuerzo físico. Acude a la emergencia donde se le aplica un medicamento que logra menor demanda de oxígeno al miocardio. ¿Qué medicamento logra ello?",
            "options": ["Amlodipino", "Nitroglicerina sublingual", "Sildenafilo", "Diltiazem"],
            "answer": 1
        },
        {
            "question": "Varón de 37 años, acude por presentar disnea, hemoptisis. Antecedentes: hace 5 meses arritmia cardiaca: Rx de tórax: congestión pulmonar; test de esfuerzo: genera arritmias y signos de isquemia miocárdica. ¿Cuál es el mecanismo fisiológico alterado?",
            "options": ["Disminución del llenado ventricular izquierdo", "Disminución de la gradiente de presión atrioventricular", "Aumento de resistencia pulmonar", "Disminución del llenado ventricular derecho"],
            "answer": 0
        },
        {
            "question": "¿Cuál es el ruido cardíaco que es causado por el flujo turbulento asociado al cierre de las válvulas auriculoventriculares en el comienzo de la sístole?",
            "options": ["S2", "S4", "S3", "S1"],
            "answer": 3
        },
        {
            "question": "¿Qué tejido es indispensable para dividir el corazón en cuatro cámaras y el tracto de salida en los canales pulmonar y aórtico?",
            "options": ["Membrana cloacal", "Membrana bucofaríngea", "Mesocaradio dorsal", "Almohadillas endocárdicas"],
            "answer": 3
        },
        {
            "question": "El sistema de conducción especializado del corazón tiene doble función: generar impulsos rítmicos que provoquen la contracción miocárdica y por otra parte la de conducir este impulso a lo largo del corazón. Todas las células miocárdicas tienen cuatro propiedades. ¿Cómo se llama la capacidad de ser contráctil?",
            "options": ["Cronotopismo", "Inotropismo", "Automatismo", "Dromotropismo"],
            "answer": 1
        },
        {
            "question": "En relación a las fases del potencial de acción de la célula miocárdica, señale qué mecanismo fisiológico sucede en la despolarización rápida (fase 0):",
            "options": ["Brusca entrada de sodio a la célula", "Salida brusca de sodio de la célula", "Entrada lenta de calcio", "Salida de potasio desde la célula"],
            "answer": 0
        },
        {
            "question": "Un paciente de 45 años se presenta en la sala de urgencias con episodios recurrentes de taquicardia, que se caracterizan por una frecuencia cardíaca de 180 latidos por minuto, palpitaciones, opresión en el pecho y mareos. Después de realizar un electrocardiograma (ECG) que confirma el diagnóstico de taquicardia supraventricular paroxística, se decide iniciar el tratamiento farmacológico. ¿Cuál es el tratamiento de elección más adecuado para controlar los episodios de taquicardia supraventricular paroxística en este paciente?",
            "options": ["Administración de adenosina intravenosa", "Uso de betabloqueantes orales", "Terapia con antagonistas del calcio orales", "Utilización de medicamentos antiarrítmicos intravenosos", "No se requiere tratamiento farmacológico para la taquicardia supraventricular paroxística"],
            "answer": 0
        },
        {
            "question": "Varón de 72 años llevado a emergencia por mareos y dolor precordial hace una hora. EKG: QT largo, taquicardia ventricular, no signos de isquemia; resto sin alteraciones. Refiere automedicación con pastillas por un supuesto COVID - 19. ¿Cuál es el medicamento responsable?",
            "options": ["Dexametasoa", "Paracetamol", "Azitromicina", "Ivermectina"],
            "answer": 2
        },
        {
            "question": "Mujer de 70 años, presenta dolor precordial, disnea y palpitaciones. Antecedente: Falla cardiaca e hipertensión arterial. Examen: PA: 100/60 mmHg, FC: 102X', FR: 20X', T:37°C. EKG: fibrilación auricular con frecuencia ventricular controlada. Paciente tiene indicación de anticoagulación, para valorar el riesgo de sangrado. ¿Qué score debe valorarse?",
            "options": ["CHA2DS2 VASc", "TIMI", "HAS-BLED", "EHRA"],
            "answer": 2
        },
    ]
}
# --- Función para iniciar el examen ---
async def start_exam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Verifica si el usuario accedió mediante el enlace con el parámetro correcto.
    if context.args and context.args[0] == "acceso":
        # Crea un teclado con botones para cada categoría.
        keyboard = [[InlineKeyboardButton(category, callback_data=f"category-{category}")] for category in categories]
        reply_markup = InlineKeyboardMarkup(keyboard)  # Configura el teclado con las categorías.
        
        # Envía el mensaje inicial con el teclado de categorías.
        await update.message.reply_text(
            "👋 ¡Bienvenido al examen interactivo!\nSelecciona una categoría para comenzar:",
            reply_markup=reply_markup,
        )
    else:
        # Si no se accede con el parámetro correcto, niega el acceso.
        await update.message.reply_text(
            "⚠️ Acceso denegado. Solo los usuarios con el enlace de acceso pueden utilizar este bot."
        )

# --- Función que maneja la selección de categoría ---
async def handle_category_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query  # Obtiene la consulta del usuario.
    await query.answer()  # Confirma al usuario que su interacción ha sido recibida.

    # Extrae el nombre de la categoría seleccionada del callback_data.
    category_name = query.data.split("-")[1]
    context.user_data["category"] = category_name  # Guarda la categoría seleccionada en los datos del usuario.
    context.user_data["answered_questions"] = []  # Inicializa la lista de preguntas respondidas.

    # Notifica al usuario que la categoría ha sido seleccionada.
    await query.message.edit_text(f"📚 Has seleccionado la categoría: {category_name}. ¡Vamos a comenzar!")
    # Envía una pregunta aleatoria de la categoría seleccionada.
    await send_question(query.message, context)

# --- Función que envía una pregunta aleatoria ---
async def send_question(message, context: ContextTypes.DEFAULT_TYPE):
    category = context.user_data.get("category")  # Obtiene la categoría seleccionada.
    if not category:  # Verifica que haya una categoría seleccionada.
        await message.reply_text("⚠️ No se ha seleccionado ninguna categoría.")
        return

    questions = categories[category]  # Obtiene las preguntas de la categoría seleccionada.
    answered_questions = context.user_data.get("answered_questions", [])  # Obtiene las preguntas ya respondidas.
    # Filtra las preguntas que aún no han sido respondidas.
    remaining_questions = [i for i in range(len(questions)) if i not in answered_questions]

    if not remaining_questions:  # Si no quedan preguntas, felicita al usuario.
        await message.reply_text("🎉 ¡Has respondido todas las preguntas! 💪 ¡Gran trabajo!")
        return

    # Selecciona una pregunta aleatoria de las restantes.
    question_index = random.choice(remaining_questions)
    context.user_data["current_question"] = question_index  # Guarda el índice de la pregunta actual.
    context.user_data["answered_questions"].append(question_index)  # Marca la pregunta como respondida.
    question_data = questions[question_index]  # Obtiene los datos de la pregunta seleccionada.

    # Prepara el texto de la pregunta y las opciones de respuesta.
    question_text = f"❓ {question_data['question']}"
    options = [f"{chr(65 + i)}. {option}" for i, option in enumerate(question_data["options"])]
    # Crea un teclado con las opciones de respuesta.
    keyboard = [[InlineKeyboardButton(opt, callback_data=f"answer-{question_index}-{i}")] for i, opt in enumerate(options)]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Envía la pregunta y las opciones al usuario.
    await message.reply_text(f"{question_text}\n" + "\n".join(options), reply_markup=reply_markup)

# --- Función que maneja la respuesta del usuario ---
async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query  # Obtiene la consulta del usuario.
    await query.answer()  # Confirma la recepción de la respuesta.

    # Extrae el índice de la pregunta y la opción seleccionada.
    data = query.data.split("-")
    question_index, selected_option = int(data[1]), int(data[2])
    category = context.user_data["category"]  # Obtiene la categoría seleccionada.
    question_data = categories[category][question_index]  # Obtiene los datos de la pregunta.
    correct_option = question_data["answer"]  # Obtiene la opción correcta.

    # Verifica si la respuesta es correcta o incorrecta.
    if selected_option == correct_option:
        await query.message.reply_text("✅ ¡Correcto!")
    else:
        correct_answer_text = question_data["options"][correct_option]
        await query.message.reply_text(f"❌ Incorrecto. La respuesta correcta era: {correct_answer_text}.")

    # Pide al usuario que escriba "sí" para continuar o "no" para finalizar.
    await query.message.reply_text(
        "¿Deseas continuar? Escribe 'Si' para regresar al menú de categorías o 'no' para finalizar."
    )

# --- Función que maneja la entrada de texto del usuario ---
async def handle_text_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text.strip().lower()  # Convierte la entrada a minúsculas.

    if user_input in ["sí", "si"]:  # Si el usuario escribe "sí".
        # Muestra el menú principal de categorías.
        keyboard = [[InlineKeyboardButton(category, callback_data=f"category-{category}")] for category in categories]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            "👋 Selecciona una nueva categoría para comenzar:",
            reply_markup=reply_markup,
        )
    elif user_input == "no":  # Si el usuario escribe "no".
        # Enviar un mensaje de despedida.
        await update.message.reply_text("🎉 ¡Gracias por participar! 💡 ¡Sigue aprendiendo!.Recuerda: Los logros no son magia o surte, son esfuerzo y dedicación")
    else:  # Si la entrada no es válida.
        await update.message.reply_text("⚠️ Respuesta no válida. Escribe 'Sí' para regresar al menú o 'No' para finalizar.")


# --- Configuración del bot ---
app = ApplicationBuilder().token("7648845471:AAFY6FhamIAUUNkEPgqduZj12o7f6ZyNrew").build()  # Reemplaza YOUR_BOT_TOKEN con tu token real.
# Asocia los comandos y eventos con las funciones correspondientes.
app.add_handler(CommandHandler("start", start_exam))  # Maneja el comando /start.
app.add_handler(CallbackQueryHandler(handle_category_selection, pattern="^category-"))  # Maneja la selección de categoría.
app.add_handler(CallbackQueryHandler(handle_answer, pattern="^answer-"))  # Maneja las respuestas a las preguntas.
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_input))  # Maneja entradas de texto del usuario.

# --- Ejecuta el bot ---
if __name__ == "__main__":
    app.run_polling()  # Inicia el bot y espera interacciones.