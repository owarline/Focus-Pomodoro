import time

def pomodoro():
    # Configurar los tiempos
    work_time = 25*60 # Tiempo de trabajo en segundos
    short_break_time = 5*60 # Tiempo de descanso corto en segundos
    long_break_time = 30*60 # Tiempo de descanso largo en segundos
    interval_count = 0 # Contador de intervalos de trabajo completados

    while True:
        print("Empezando un nuevo intervalo de trabajo")
        time.sleep(work_time)
        interval_count += 1
        if interval_count % 4 == 0:
            print("Haz completado 4 intervalos de trabajo, toma un descanso largo")
            time.sleep(long_break_time)
        else:
            print("Haz completado un intervalo de trabajo, toma un descanso corto")
            time.sleep(short_break_time)

pomodoro() # Ejecutar la función principal
