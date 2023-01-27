import random
import time
from juego import comparacion

saludo="BIENVENID@ AL JUEGO PIEDRA PAPEL O TIJERA"
print (saludo)
time.sleep(1)
print("NO PERDAMOS UN SEGUNDO MAS, A JUGAR!")
time.sleep(1)
scoreusuario= 0
scoremaquina= 0
usuario=" "
while usuario != "FINALIZAR":
  maquina=random.randint(1,3) 

  usuario= input("\nPIEDRA | PAPEL | TIJERA | FINALIZAR\nIngrese su opción: ").upper()
    
  ganador=comparacion(usuario,maquina)

  if ganador=="maquina":
    scoremaquina +=1
  elif ganador=="usuario":
    scoreusuario += 1
  else:
    continue

if usuario == "FINALIZAR":  
  if scoreusuario > scoremaquina:
    time.sleep(1)
    print(f"***RESULTADO FINAL***\n\nTU: {scoreusuario}\nMAQUINA: {scoremaquina}\n\nHAS GANADO, FELICITACIONES!!")
  elif scoreusuario < scoremaquina:
    time.sleep(1)
    print(f"\n***RESULTADO FINAL***\n\nTU: {scoreusuario}\nMAQUINA: {scoremaquina}\n\nHAS PERDIDO JAJAJA!!")
  elif scoreusuario == scoremaquina:
    time.sleep(1)
    print(f"***RESULTADO FINAL***\n\nTU: {scoreusuario}\nMAQUINA: {scoremaquina}\n\nHEMOS EMPATADO!!")
    