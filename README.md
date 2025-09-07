# Demonio-de-autoguardado
🧮 Calculadora con Autoguardado (Daemon)

Este proyecto implementa una calculadora gráfica en Python utilizando Tkinter.
Además de las operaciones básicas, integra un hilo demonio que guarda automáticamente el historial de operaciones en un archivo de texto.

🚀 Características

Interfaz gráfica hecha con Tkinter.

Operaciones básicas soportadas:

Suma (+)

Resta (-)

Botones numéricos y algunos símbolos preparados para futuras funciones.

Función de borrado de último dígito (←).

El resultado de cada operación se muestra en pantalla.

Historial automático:

Cada operación realizada se guarda en una lista en memoria.

Un hilo demonio (threading.Thread) revisa periódicamente si hay operaciones nuevas y las escribe en un archivo de texto.

⚙️ Cómo funciona el demonio de autoguardado

Se crea un hilo en segundo plano con la bandera daemon=True.

Este hilo ejecuta la función autoguardado(), que:

Revisa si existen operaciones nuevas en el historial.

Si las hay, las escribe en el archivo historial.txt.

Actualiza el índice de operaciones guardadas.

Espera 5 segundos (time.sleep(5)) antes de volver a revisar.

De esta forma, el hilo solo escribe cuando hay operaciones nuevas y no interfiere con la interfaz gráfica.

Ejemplo practico de la calculadora.

Se realizan cualquier tipo de operaciones y se guardan en el archivo .txt

<img width="717" height="295" alt="image" src="https://github.com/user-attachments/assets/489ce029-84e3-449c-a42a-16a03e76f6fe" />

El codigo que genera y controla al demonio es este, en resumen un demonio es una funcion que trabaja por debajo de la "principal",
se ejecuta en segundo plano hasta que la principal termina.

<img width="660" height="265" alt="image" src="https://github.com/user-attachments/assets/39d37628-7aae-4f0b-a858-7c5c83ea1c60" />
