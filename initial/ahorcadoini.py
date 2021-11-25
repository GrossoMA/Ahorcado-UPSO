import menuahorcado as m #desde aca modemos administrar interface del menu
import leerletra as l #desde aca podemos utilizar para solicitar lectura de una letra para una palabra
import imprimirahorcado as i #graficar el estado del juego, grafica el muñeco

#voy a hacer un ciclado hasta que la opcion elegida sea salir
#primero mostrar menu    
#leer opcion ingresada
#cambiardemenu
while m.opcionmenu != False:
    m.mostrarmenu()
    m.opcion = m.leeropcion()
    m.cambiardemenu(m.opcion)
if m.opcionmenu == False:
    m.cerrar()

