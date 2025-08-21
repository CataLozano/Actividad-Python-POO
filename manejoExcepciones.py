#######
#ZeertoDivisionError
#######
try:
    resultado=10/0
except ZeroDivisionError:
    print("No se puede dividir por 0")
#######        
#IndexError
#######
try:
    lista=[1,2,3,4]
    print(lista[70])
except IndexError:
    print("Error:lista fuera del campo ") 
    
######   
#NameError
######
try:
    print(x)
except NameError:
    print("La variable x no esta dfinida")
    
########
#TypeErrror
########
try:
    suma= 10 + 'juan'
    print(suma)
except TypeError:
    print("Error: no soporta tipo entero con contenido de texto")
    
########
# ModuloNotFoundErrror
########

try:
    import randomx #no existe randomx
except ModuleNotFoundError:
    print("Error: no encontrado")     
    
########
#OverFlowerERROR
########
try:
    resultado= 5.24**2384737
except OverflowError:
    print("Error: resultado demasiado grande")
    
########
#KeyERRROR
########

try:
    productos={"manzana":45, "peras":32, "lechuga":23}
    print(productos["sandia"])
except KeyError:
    print("Error: llave erronea, no existe")
    
    
##############################################################

#EXCEPCIONES MULTIPLES#

##############################################################

try:
    archivo= open ('archivo_inexistente.txt', 'r')
    contenido=archivo.read()
    resultado= 10/0 
except FileNotFoundError:
    print("error: no se encontro")
except ZeroDivisionError:   
    print("Error: no se puede dividir por 0")
finally:
    print("esto se ejecuta siempre")     
