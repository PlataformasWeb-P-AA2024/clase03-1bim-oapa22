
# acceder al archivo
archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# obtener las líneas del archivo
data = archivo.readlines()


num=0
encabezados = data[0].split("|")


for lineas in data[1:]:
    num += 1

    # En línea tomo el valor de data[num]
    linea = data[num]

    # A línea que es una cadena, la separo mediante la función de Python split
    # Recuerdo que el separador de la cadena es un "|"
    linea = linea.split("|")
    archivo.close()

    pagina= """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Ejercicio Data</title>
    </head>
        <body>
            <h1>
                Información de Institución
            </h1>
            <p>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
                <b>%s:</b>%s<br>
            </p>
        </body>
    </html>
    """ % (encabezados[0], linea[0], encabezados[1], linea[1], encabezados[2], linea[2], encabezados[3],
           linea[3], encabezados[4], linea[4], encabezados[5], linea[5], encabezados[6], linea[6],
           encabezados[7], linea[7], encabezados[8], linea[8], encabezados[9], linea[9], encabezados[10],
           linea[10], encabezados[11], linea[11], encabezados[12], linea[12])
    print(pagina)
    archivo_generado = open("paginas/%s.html" % linea[1], "w")
    archivo_generado.write("%s" % pagina)
    archivo_generado.close()