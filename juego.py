import time


def comparacion(usuario, maquina):
  ganador = ""
  if usuario == "PIEDRA" and maquina == 1:
    time.sleep(1)
    print("\nTU: PIEDRA\nMAQUINA: PIEDRA\n\nHEMOS EMPATADO")
    ganador = ""
  elif usuario == "PIEDRA" and maquina == 2:
    time.sleep(1)
    print("\nTU: PIEDRA\nMAQUINA: PAPEL\n\nHAS PERDIDO JAJA")
    ganador = "maquina"
  elif usuario == "PIEDRA" and maquina == 3:
    time.sleep(1)
    print("\nTU: PIEDRA\nMAQUINA: TIJERA\n\nHAS GANADO")
    ganador = "usuario"
  elif usuario == "PAPEL" and maquina == 1:
    time.sleep(1)
    print("\nTU: PAPEL\nMAQUINA: PIEDRA\n\nHAS GANADO")
    ganador = "usuario"
  elif usuario == "PAPEL" and maquina == 2:
    time.sleep(1)
    print("\nTU: PAPEL\nMAQUINA: PAPEL\n\nHEMOS EMPATADO")
    ganador = ""
  elif usuario == "PAPEL" and maquina == 3:
    time.sleep(1)
    print("\nTU: PAPEL\nMAQUINA: TIJERA\n\nHAS PERDIDO JAJA")
    ganador = "maquina"
  elif usuario == "TIJERA" and maquina == 1:
    time.sleep(1)
    print("\nTU: TIJERA\nMAQUINA: PIEDRA\n\nHAS PERDIDO JAJA")
    ganador = "maquina"
  elif usuario == "TIJERA" and maquina == 2:
    time.sleep(1)
    
    print("\nTU: TIJERA\nMAQUINA: PAPEL\n\nHAS GANADO")
    ganador = "usuario"
  elif usuario == "TIJERA" and maquina == 3:
    time.sleep(1)
    print("\nTU: TIJERA\nMAQUINA: TIJEA\n\nHEMOS EMPATADO")
    ganador = " "
  else:
     print ("\n***NO PUDE ENTENDERTE***") 
  return ganador












