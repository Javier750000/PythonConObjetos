from yacc import parser

def main():
    print("Escriba el nombre del archivo de prueba.")
    nombreArchivo = input()
    print("")
    archivo = open(nombreArchivo)
    datos = archivo.read()
    archivo.close()
    parser.parse(datos)

if __name__ == '__main__':
    main()
