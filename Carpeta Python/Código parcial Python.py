def comparar_velocidad_escoba(velocidad_escoba_ms, limite_velocidad_kmh):

  velocidad_escoba_kmh = velocidad_escoba_ms * 3.6

  if velocidad_escoba_kmh > limite_velocidad_kmh:
    diferencia = velocidad_escoba_kmh - limite_velocidad_kmh
    return f"¡La escoba excede el límite de velocidad en {diferencia:.2f} km/h!"
  else:
    diferencia = limite_velocidad_kmh - velocidad_escoba_kmh
    return f"La escoba está dentro del límite de velocidad.  Quedan {diferencia:.2f} km/h de margen."

velocidad_escoba = int(input("Ingrese la velocidad de la escoba en m/s: "))
limite_velocidad = int(input("Ingrese el límite de velocidad en km/h: "))

velocidad_escobaenkm = velocidad_escoba * 3.6
print("la velocidad de la escoba en km/h es",velocidad_escobaenkm)

resultado = comparar_velocidad_escoba(velocidad_escoba, limite_velocidad)
resultado
