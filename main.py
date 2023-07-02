from yacc import parser

def main():
    nombreArchivo = "fibonacci.txt"
    print("")
    archivo = open(nombreArchivo)
    datos = archivo.read()
    archivo.close()
    parser.parse(datos)

if __name__ == '__main__':
    main()
