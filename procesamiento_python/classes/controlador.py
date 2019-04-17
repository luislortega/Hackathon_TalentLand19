class ControladorDatos:
    # Guardamos la entidades y poblaciones del 2010
    def controlador_poblacion_2010(self, database, datos):
        entidades_federativas = []
        poblacion = []

        for elemento in datos:
            entidades_federativas.append(elemento[0])
            poblacion.append({'2010':elemento[1]})
        
        print("[✔] datos del 2010 procesados")
        database.insertar_entidades_poblacion_2010(entidades_federativas, poblacion)
    # Obteno los resultados calculado desde el 2010 hasta el 2017 poblacion_2011 = poblacion_2010 + natalidad_2011 - mortalidad_2011 
    def controlador_poblacion_2010_2017(self, database, poblacion_2010, natalidad_2011_2017, mortalidad_2011_2017):
        lista_poblacion_2010 = []
        no_lista_poblacion = []
        lista_final = []

        for elemento_2010 in poblacion_2010:
            lista_final.append({"2010": elemento_2010[1]})
            lista_poblacion_2010.append(elemento_2010[1])
        
        for contador_ano in range(2011, 2018):
            entidad_federativa = 0
            for natalidad, mortalidad in zip(natalidad_2011_2017, mortalidad_2011_2017): 
                poblacion = int(lista_poblacion_2010[entidad_federativa]) + int(natalidad[str(contador_ano)]) - int(mortalidad[str(contador_ano)])       
                no_lista_poblacion.append({str(contador_ano):str(poblacion)})
                lista_poblacion_2010[entidad_federativa] = str(poblacion)
                entidad_federativa += 1

        for x in range(0, 32):
            lista_final[x] = {**lista_final[x], **no_lista_poblacion[x],**no_lista_poblacion[x+32], **no_lista_poblacion[x+64], **no_lista_poblacion[x+96], **no_lista_poblacion[x+128], **no_lista_poblacion[x+160], **no_lista_poblacion[x+192]}
        
        print("[✔] Calculos matematicos para obtener la poblacion hasta el 2017 Pt = Pi + Nt - Mt")
        database.insertar_poblacion_2010_2017(lista_final)

    def controlador_poblacion_2018_2019(self,database, poblacion_total):
        poblacion_2018_ordenada = []
        poblacion_2019_ordenada = []
        poblacion_2018_2019 = []
        contador_entidad = 1

        for x in range(0, 32):
            poblacion_2018_ordenada.append(0)
            poblacion_2019_ordenada.append(0)

        for x in range(1, (219*32)):
            poblacion_2018_ordenada[contador_entidad-1] += int(poblacion_total[0][x].replace("\n", ""))
            poblacion_2019_ordenada[contador_entidad-1] += int(poblacion_total[1][x].replace("\n", ""))
            if x == ((219*contador_entidad)+(contador_entidad-1)):
                contador_entidad += 1
            
        for x in range(0, 32):
            poblacion_2018_2019.append({"2018": poblacion_2018_ordenada[x], "2019": poblacion_2019_ordenada[x]})

        print("[✔] Procesamiento de +500.000 de datos para obtener las aproximaciones del 2018 y 2019")
        database.insertar_poblacion_2018_2019(poblacion_2018_2019)

    def controlador_patentes_2010_2018(self, database, patentes_2010_2018):
        patentes_2010_2018_final = []

        for x in range(0, 32):
            patentes_2010_2018_final.append({"2010": patentes_2010_2018[x][1],
             "2011": patentes_2010_2018[x][2], "2012": patentes_2010_2018[x][3], "2013": patentes_2010_2018[x][4]})

        print("[DEV] Procesamiento de las patentes 2010 hasta el 2018")