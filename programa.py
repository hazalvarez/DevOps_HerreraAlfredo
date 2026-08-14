import cv2

# Cargar la imagen
imagen = cv2.imread("cartas.jpeg")

# Verificar que la imagen exista
if imagen is None:
    print("Error: no se pudo cargar la imagen cartas.jpeg")
    exit()

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detectar bordes con Canny
bordes = cv2.Canny(gris, 100, 200)

# Guardar el resultado
cv2.imwrite("result_HA.jpg", bordes)

print("Proceso terminado correctamente.")
print("El resultado se guardó como result_HA.jpg")