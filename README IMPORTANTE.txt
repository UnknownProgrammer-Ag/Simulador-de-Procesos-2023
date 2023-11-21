Bienvenido Usuario de Simulador Round Robin 2023:
######################################

Antes de comenzar a utilizar este programa queremos aclararle que este es un simulador que utiliza un tipo de archivo .csv, sin excepciones.
Por lo tanto queremos mostrarle como hacer un archivo .csv funcional para poder testear la simulación.

######################################

Para empezar debe tener en cuenta que en un csv (Comma Separate Values) cada linea es una fila, cada valor separado por una coma es una columna.

Para que el simulador lea correctamente la informacion debe seguir este orden de datos:

#Header
ID ,Tamaño ,T_Arribo ,T_Irrupción
#Cuerpo
ValorID , ValorTamaño, ValorArribo, ValorIrrupcion

#######ACLARACIONES###########################################################
Todos los valores deben ser enteros, en caso de que no lo sean incurrira en un malfuncionamiento del simulador, al igual que si mezcla las columnas. 

Otra aclaración es que la cantidad máxima permitida para simular es de 10 procesos (ID 10 Maximo), cualquier proceso posterior a ese valor será ignorado.
Igual a esto, cualquier proceso cuyo tamaño supere la medida de 250 sera ignorado debido a limitaciones de memoria.

Si necesita una mejor ilustración de un csv funcional puede utilizar el "Archivo_Procesos_Test.csv" que adjuntamos al simulador.

Los espacios no afectan a la ejecución del programa.



Muchas gracias por usar el simulador, y por leer este documento.
Atte. Equipo Caché