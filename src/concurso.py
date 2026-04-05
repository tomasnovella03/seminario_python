def calcular_puntaje_ronda(scores_participante):
    return sum(scores_participante.values())


def obtener_ganador_ronda(scores_ronda):
    puntajes = {
        participante: calcular_puntaje_ronda(scores)
        for participante, scores in scores_ronda.items()
    }
    ganador = max(puntajes, key=puntajes.get)
    return ganador, puntajes[ganador]


def actualizar_acumulado(acumulado, scores_ronda, ganador_ronda):
    for participante, scores in scores_ronda.items():
        pts = calcular_puntaje_ronda(scores)

        if participante not in acumulado:
            acumulado[participante] = {
                'total': 0,
                'rondas_ganadas': 0,
                'mejor_ronda': 0,
                'puntajes_por_ronda': []
            }

        acumulado[participante]['total'] += pts
        acumulado[participante]['puntajes_por_ronda'].append(pts)

        if pts > acumulado[participante]['mejor_ronda']:
            acumulado[participante]['mejor_ronda'] = pts

        if participante == ganador_ronda:
            acumulado[participante]['rondas_ganadas'] += 1

    return acumulado


def imprimir_tabla(acumulado, numero_ronda):
    ranking = sorted(
        acumulado.items(),
        key=lambda x: x[1]['total'],
        reverse=True
    )

    encabezado = f"{'Pos':<5}{'Cocinero':<15}{'Puntaje':<12}{'Rondas gan.':<14}{'Mejor ronda':<14}{'Promedio'}"
    separador = '-' * len(encabezado)

    print(encabezado)
    print(separador)

    for pos, (nombre, datos) in enumerate(ranking, start=1):
        promedio = datos['total'] / numero_ronda
        print(
            f"{pos:<5}"
            f"{nombre:<15}"
            f"{datos['total']:<12}"
            f"{datos['rondas_ganadas']:<14}"
            f"{datos['mejor_ronda']:<14}"
            f"{promedio:.1f}"
        )

    print(separador)


def simular_competencia(rounds):
    acumulado = {}

    for numero_ronda, ronda in enumerate(rounds, start=1):
        tema = ronda['theme']
        scores_ronda = ronda['scores']

        ganador, pts_ganador = obtener_ganador_ronda(scores_ronda)
        acumulado = actualizar_acumulado(acumulado, scores_ronda, ganador)

        print(f"\nRonda {numero_ronda} - {tema}:")
        print(f"  Ganador: {ganador} ({pts_ganador} pts)")
        print()
        imprimir_tabla(acumulado, numero_ronda)

    print("\n" + "=" * 60)
    print("TABLA DE POSICIONES FINAL")
    print("=" * 60)
    imprimir_tabla(acumulado, len(rounds))