# main
import modulo as m
import os


def main():
    opc = -1
    temas = []
    mat_generada = False
    while opc != 0:
        m.print_menu()
        opc = int(input('OPCIÓN: '))
        print('--' * 40)

        if opc == 1:
            m.cargar_vector(temas, 'musica.csv')
            m.mostrar_vector(temas)

        else:
            if len(temas) == 0 and opc != 0:
                print('¡ERROR! Primero debe cargar la opcion 1... ')

            elif opc == 2:
                n = m.validar_mayor_que(0, 'Ingrese cantidad de temas: ')
                lista_opt2 = [''] * n
                i = m.validar_entre(0, 4, 'Ingrese el idioma: ')

                m.fill_list(lista_opt2, i, temas)

                empty_flag = m.empty_pos(lista_opt2)
                if empty_flag:
                    print('No se ha podido completar la lista con', n, 'canciones')

                m.mostrar_lista_opt2(lista_opt2)

            elif opc == 3:
                mat = m.generar_matriz(temas)
                m.mostrar_matriz(mat)
                mat_generada = True
            elif opc == 4:
                # A partir de la matriz generada en el item 3,
                # determinar la cantidad de temas musicales para el género g, siendo g un valor ingresado por teclado.
                if not mat_generada:
                    print('Primero debe cargar la matriz (opcion 3)...')
                else:
                    g = m.validar_entre(0, 5, 'Ingrese código de género: ')
                    cant_g = m.contar_gen_mat(mat, g)
                    print('Hay', cant_g, 'temas musicales para el género', m.gen_cad[g])
            elif opc == 6:
                idioma_req = m.validar_entre(0, 4, 'Ingrese idioma que desea filtrar: ')
                m.gen_binario(idioma_req, temas)
            elif opc == 5:
                x = input('Ingrese título a buscar: ')
                pos = m.busqueda_binaria(temas, x)
                if pos == -1:
                    print('El título', x, 'no existe en esta lista.')
                else:
                    print(temas[pos])
            elif opc == 7:
                idioma_req = m.validar_entre(0, 4, 'Ingrese idioma: ')
                fd = m.gen_fd(idioma_req)
                if os.path.exists(fd):
                    m.leer_binario(idioma_req)
                else:
                    print('El archivo "', fd, '" no existe, pero será creado.')
                    m.gen_binario(idioma_req, temas)
                    m.leer_binario(idioma_req)
    print('\t\t\t\t\t\t\t\t¡Hasta luego!')
    print('--' * 40)


if __name__ == '__main__':
    main()
