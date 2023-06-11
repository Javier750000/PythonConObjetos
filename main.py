from yacc import parser

def main():
    archivo = open('whileTest.txt')
    datos = archivo.read()
    archivo.close()
    parser.parse(datos)
    print("El código pudo ser leído correctamente.")

if __name__ == '__main__':
    main()