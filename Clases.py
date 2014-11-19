#!/usr/bin/python

'''
 Traductores e Interpretadores                                                       
 CI-3725  

 Integrantes:   

	 10-10738 Abelardo Jesus Valino Ovalle                                                
	 10-10353 Andres Rafael Hernandez Monterola

 Modulo Clases            
'''

import sys

# Diccionario para guardar operadores y usarlos posteriormente en las 
# clases con mayor facilidad

symbolsDic = {	
						"+" 	: "Plus",
						"<=" 	: "Less equal",
						"==" 	: "Equal",
						".*." 	: "Times Cross",
						"./." 	: "Div Cross",
						".mod."	: "Mod Cross",
						"|" 	: "Or",
						".-." 	: "Minus Cross",
						"/" 	: "Div",
						"%" 	: "Mods",
						"div"	: "Division",
						">" 	: "Greater",
						">=" 	: "Greater equal",
						"mod"	: "Mod",
						"-" 	: "Minus",
						"*" 	: "Times",
						"\/=" 	: "distint",
						"&" 	: "and",
						".%." 	: "mods cross",
						".div."	: "div cross",
						"<" 	: "Less",
						".+." 	: "plus cross",
					} 




# Funcion para impresion de tab
def Identacion(cantidad):
	i=0

	while (i<4):	
		cantidad +=  "  "
		i+=1

	return cantidad;


class SymbolTable():
	"""Clase que maneja la tabla de simbolos"""

	#Constructor de la clase
	def __init__(self, father):
		
		self.dic = {}
		#self.functions = {}
		self.sons = []
		self.father = father
	
	def addSymbol(self,key,value):

		if self.dic.has_key(key):
			exit()

		self.dic[key] = value

	# def addFunction(self,key, returntype, ParamList):

	# 	if self.functions.has_key(key):
	# 		exit()

	# 	value = []

	# 	value.append(returntype)

	# 	if ParamList <> None:
	# 		for i in ParamList:
	# 			value.append(i)

	# 	self.functions[key] = value

	def hasKey(self,key):

		if self.dic.has_key(key):
			return True

		if self.father <> None:

			return self.father.hasKey(key)

		else:
			
			return False

	def findTypeOf(self,key):

		if self.dic.has_key(key):
			return self.dic[key]

		if self.father <> None:

			return self.father.findTypeOf(key)

		else:
			return "NotDeclared"


	def born(self,son):
		self.sons.append(son)

	def printI(self, cantidad):
		
		print self.dic

		if self.sons:
			for i in self.sons:
				i.printI(Identacion(cantidad))

class Number():
	"""Clase que maneja a los numeros"""

	#Constructor de la clase
	def __init__(self,value,row):
		
		self.value = value
		self.row = row
		self.type = "number"
	
	def getRow(self):
		return set.row

	def getValue(self):
		return int(self.value)

	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Literal Numerico Valor: ", self.value

	def typechecking(self,SymbolTable):

		return self.type


class Identificator:
	"""Clase que maneja a los Identificador (ID)"""

	#Constructor de la clase
	def __init__(self,value,row):
		
		self.value = value
		self.row = row
		self.type = "id"
	
	def getRow(self):
		return set.row

	def getValue(self):
		return self.value
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Nombre: ", str(self.value)

	def typechecking(self,SymbolTable):

		if SymbolTable.hasKey(self.value) == False:
			print "ERROR: El identificador no se encuentra en la Tabla de Simbolos: " + str(self.value)
			exit()

		return SymbolTable.findTypeOf(self.value)

class String:
	"""Clase que maneja a los String"""

	#Constructor de la clase
	def __init__(self,value,row):
		
		self.value = value
		self.row = row
		self.type = "string"

	
	def getRow(self):
		return set.row

	def getValue(self):
		return str(self.value)

	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, " String: ", self.value

	def typechecking(self,SymbolTable):

		return self.type

class Boolean:
	"""Clase que maneja a los Booleanos"""

	# Constructor de la clase
	def __init__(self,value,row):

		self.value = value
		self.row = row
		self.type = "boolean"
	
	def getRow(self):
		return set.row
		
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Boolean: "
		print cantidad, " Valor: ", str(self.value)		

	def typechecking(self,SymbolTable):

		return self.type

class Matrix:
	"""Clase que maneja a las Matrices "matrix(R,C)" """

	# Constructor de la clase
	def __init__(self,R,C,row):

		self.R = R
		self.C = C
		self.row = row
		self.type = "matriz"
	
	def getRow(self):
		return set.row

	def getR(self):
		return int(self.R.getValue())

	def getC(self):
		return int(self.C.getValue())	

	#Funcion para imprimir
	def printI(self, cantidad):


		if self.R.getValue() == 0:

			print cantidad, "Vector Columna: "
			self.C.printI(Identacion(cantidad))

		elif self.C.getValue() == 0:

			print cantidad, "Vector Fila: "
			self.R.printI(cantidad)

		else:
			print cantidad, "Matrix: "
			print cantidad, "  Valor Fila: "
			self.R.printI(Identacion(cantidad)) #imprime la fila
			print cantidad, "  Valor Columna: "
			self.C.printI(Identacion(cantidad)) #imprime la coloumna

	def typechecking(self,SymbolTable):

		return self.type

# class Row:
# 	"""Clase que maneja a las Filas "row(r)" """

# 	# Constructor de la clase
# 	def __init__(self,R,row):

# 		self.R = R
# 		self.row = row
	
# 	def getRow(self):
# 		return set.row
		
# 	#Funcion para imprimir
# 	def printI(self, cantidad):

# 		print cantidad, "Vector Fila: "
# 		self.R.printI(Identacion(cantidad))


# class Column:
# 	"""Clase que maneja a las Columnas "column(c)" """

# 	# Constructor de la clase
# 	def __init__(self,C,row):

# 		self.C = C
# 		self.row = row
	
# 	def getRow(self):
# 		return set.row
		
# 	#Funcion para imprimir
# 	def printI(self, cantidad):

# 		print cantidad, "Vector Columna: "
# 		self.C.printI(Identacion(cantidad))

# class RowFormat:
# 	"""Clase que maneja a los formatos de las Filas 
# 	"{valor1,valor2,valor3}" """

# 	# Constructor de la clase
# 	def __init__(self,row,R = None):

# 		self.R = R 	#Lista de Filas
# 		self.row = row
	
# 	def getRow(self):
# 		return set.row
		
# 	#Funcion para imprimir
# 	def printI(self, cantidad):

# 		print cantidad, "Fila: "
		
# 		if self.R:
# 			for i in self.R:
# 				print cantidad, " Valor: "
# 				self.R.printI(Identacion(cantidad))
# 		else: 
# 			print cantidad, " Valor: Vacio"


# class ColumnFormat:
# 	"""Clase que maneja a los formatos de las Columnas 
# 	"{valor1:valor2:valor3}" """

# 	# Constructor de la clase
# 	def __init__(self,row,C = None):

# 		self.C = C 	#Lista de Columnas
# 		self.row = row
	
# 	def getRow(self):
# 		return set.row
		
# 	#Funcion para imprimir
# 	def printI(self, cantidad):

# 		print cantidad, "Columna: "
		
# 		if self.C:
# 			for i in self.C:
# 				print cantidad, " Valor: "
# 				self.C.printI(Identacion(cantidad))
# 		else: 
# 			print cantidad, " Valor: Vacio"


class MatrixFormat:
	"""Clase que maneja a los formatos de las Matrices 
	"{valor1,valor2,valor3:valor4,valor5,valor6}" """

	# Constructor de la clase
	def __init__(self,row,MatrixValue):

		self.MatrixValue = MatrixValue 
		self.row = row
	
	def getRow(self):
		return set.row

	def getR(self):

		j = 1
		k = 1
		mayork = 1

		for i in self.MatrixValue:

			if i == ":":

				if j <> 1 and k <> mayork:
					print "ERROR: La cantidad de columnas no son iguales en todas las columnas"
					exit()
					
				j = j + 1
				k = 1

			elif i == ",":
				k = k + 1

				if j == 1 and k > mayork:
					mayork = k

		return j - 1

	def getC(self):

		j = 1
		k = 1
		mayork = 1

		for i in self.MatrixValue:

			if i == ":":

				if j <> 1 and k <> mayork:
					print "ERROR: La cantidad de columnas no son iguales en todas las filas"
					exit()
					
				j = j + 1
				k = 1

			elif i == ",":
				k = k + 1

				if j == 1 and k > mayork:
					mayork = k

		return mayork

		
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Matriz: "
		j = 1
		k = 1
		mayorj = 0
		mayork = 1

		for i in self.MatrixValue:

			if i == ":":

				if j <> 1 and k <> mayork:
					print "ERROR: La cantidad de columnas no son iguales en todas las filas"
					exit()
					
				j = j + 1
				k = 1

			elif i == ",":
				k = k + 1

				if j == 1 and k > mayork:
					mayork = k


			else:

				print cantidad, " Fila: ", j, " Columna: ", k
				print cantidad, " Valor: "
				i.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):
		
		j = 1
		k = 1
		mayorj = 0
		mayork = 1

		for i in self.MatrixValue:

			if i == ":":

				if j <> 1 and k <> mayork:
					print "ERROR: La cantidad de columnas no son iguales en todas las columnas"
					exit()

				j = j + 1
				k = 1

			elif i == ",":
				k = k + 1

				if j == 1 and k > mayork:
					mayork = k

			else:

				if i.typechecking(SymbolTable) <> "number":
					print "ERROR: Los elementos de la matriz solo puede ser de tipo Numerico"
					exit()

		return "matriz"
		#return Matrix(Number(self.getR(),self.row),Number(self.getC(),self.row),self.row)



class Expre_If_Else:
	"""Clase que maneja a los condicionales IF <condicion> THEN <Intrucciones> END;"""

	#Constructor de la clase
	def __init__(self,row,condition,instruction=None, instruction2 = None):
		
		self.condition = condition
		self.instruction = instruction
		self.instruction2 = instruction2
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion IF: "
		print cantidad, " Condicion: "
		self.condition.printI(Identacion(cantidad)) #imprime la condicion

		print cantidad, "Expresion THEN: "
		for j in self.instruction:
			print cantidad, " Instruciones: "
			j.printI(Identacion(cantidad))	#imprime la instruccion

		#imprime siguiente instruccion si la hay
		if self.instruction2 <> None:
			print cantidad, "Expresion ELSE: "
			for k in self.instruction2:
				print cantidad, " Instruciones: "
				k.printI(Identacion(cantidad)) 

	def typechecking(self,SymbolTable):

		if self.condition.typechecking(SymbolTable) <> "boolean":
			print "ERROR: El tipo del condicional del if tiene que ser booleano"
			exit()

		for j in self.instruction:
			j.typechecking(SymbolTable)	

		if self.instruction2:
			for k in self.instruction2:
				k.typechecking(SymbolTable)



class Expre_Set:
	"""Clase que maneja los SET <ID> = expresion """

	# Constructor de la clase
	def __init__(self,identificator,expression,row):

		self.identificator = identificator 	
		self.expression = expression
		self.row = row
	
	def getRow(self):
		return set.row
		
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Se Asigna a: "	
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))
		print cantidad, "Expresion: "
		self.expression.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		if SymbolTable.hasKey(self.identificator.getValue()) == False:
			print "ERROR: Variable no ha sido declarada: " + str(self.identificator.getValue())
			exit()

		else:

			identificatorType = self.identificator.typechecking(SymbolTable)
			expressionType = self.expression.typechecking(SymbolTable)

			if identificatorType == "number" or identificatorType == "boolean":

				if identificatorType <> expressionType:
					print "ERROR: el tipo de las expresion es distinto al del identificador "
					exit()

			elif isinstance(identificatorType, Matrix) and isinstance(expressionType, Matrix):

				if identificatorType.getR() <> expressionType.getR() or identificatorType.getC() <> expressionType.getC():
					print "ERROR: el tamanio de la matriz en el identificador es distinto al de la expresion"
					exit()


class Variable_Declaration:
	"""Clase que maneja la declaracion de las variables 

		<type> <variable>;
		<type> <variable> = expression;

	 """

	# Constructor de la clase
	def __init__(self,row,identificator_type,identificator,expression=None):

		self.identificator_type = identificator_type
		self.identificator = identificator 	
		self.expression = expression
		self.row = row
	
	def getRow(self):
		return set.row

	def getIdentificator(self):
		return self.identificator.getValue()

	def getType(self,SymbolTable):

		identificador = self.identificator_type

		if isinstance(identificador, str):
		 	return identificador

		if isinstance(identificador, Matrix):
			return identificador

		return identificador.typechecking(SymbolTable)
		
	#Funcion para imprimir
	def printI(self, cantidad):

		# Impresion de variable y tipo
		print cantidad, "Variable: "

		if (isinstance(self.identificator_type,int) or isinstance(self.identificator_type,str)):
			print cantidad," Tipo:",self.identificator_type
		else:
			self.identificator_type.printI(Identacion(cantidad))	

		#Impresion del identificador
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))
		
		#Impresion de la expresion
		if self.expression:
			print cantidad, " Expresion: "
			self.expression.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		if SymbolTable.dic.has_key(self.identificator.getValue()):
			print "ERROR: Variable ya declarada dentro del alcance"
			exit()

		if self.expression <> None:

			if self.identificator_type == "number" or self.identificator_type == "boolean":

				if self.expression.typechecking(SymbolTable) <> self.identificator_type:
					print "ERROR: El tipo declarado no coincide con el tipo de la expresion"
					exit()

			elif isinstance(self.identificator_type, Matrix):

				if isinstance(self.expression,MatrixFormat):

					if self.expression.typechecking(SymbolTable) <> "matriz":
						print "ERROR: El tipo declarado no coincide con el tipo de la expresion matrix"
						exit()

					if self.expression.getR() <> self.identificator_type.getR() or self.expression.getC() <> self.identificator_type.getC():
						print "ERROR: Las filas o las columnas no coinciden"
						exit()

				elif isinstance(self.expression,Exp_Binaria):

					if self.expression.typechecking(SymbolTable).typechecking(SymbolTable) <> "matriz":
						print "ERROR: El tipo declarado no coincide con el tipo de la expresion matrix"
						exit()

					if self.expression.typechecking(SymbolTable).getR() <> self.identificator_type.getR() or self.expression.typechecking(SymbolTable).getC() <> self.identificator_type.getC():
						print "ERROR: Las filas o las columnas no coinciden"
						exit()


		SymbolTable.addSymbol(self.identificator.getValue(),self.identificator_type)


class Expre_Read:
	"""Clase que maneja la lectura por linea de comando

		read <identificator>;
	"""

	#Constructor de la clase
	def __init__(self,identificator,row):
		
		self.identificator = identificator 	
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion Read: "
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		if SymbolTable.hasKey(self.identificator.getValue()) == False:
			print "ERROR: El identificador no esta declarado"

			exit()

		# if self.identificator.typechecking(SymbolTable) <> "NotDeclared":
		# 	print "ERROR: El identificador esta siendo utilizado en otro lado"
		# 	exit()

class Expre_Vector:
	"""Clase que maneja los vectores

		e[i,j];
		e[i];
	"""

	#Constructor de la clase
	def __init__(self,row,identificator,fila,columna=None):
		
		self.identificator = identificator
		self.fila = fila
		self.columna = columna 	
		self.row = row
		self.type = "vector"
	
	def getRow(self):
		return set.row

	def getValue(self):
		return self.identificator.getValue()
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Vector: "
		print cantidad, " Identificador: " 
		self.identificator.printI(Identacion(cantidad))
		print cantidad, " Numero de fila: "
		self.fila.printI(Identacion(cantidad))
		if self.columna <> None:
			print cantidad, " Numero de columna: " 
			self.columna.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		if isinstance(self.identificator.typechecking(SymbolTable), Matrix) == False:
			print "ERROR: el identificador no es una matriz declarada"

		if self.fila.typechecking(SymbolTable) <> "number":
			print "ERROR: el tipo de la fila tiene que ser un numero"
			exit()

		else:

			if self.columna <> None:
				if self.columna.typechecking(SymbolTable) <> "number":
					print "ERROR: el tipo de la columna tiene que ser un numero"
					exit()

				else: 

					if (self.columna.getValue() > self.identificator.typechecking(SymbolTable).getC()):
						print "ERROR: La cantidad de columnas pedida es mayor a la cantidad de columnas que tiene la matriz"
						exit() 

					elif (self.fila.getValue() > self.identificator.typechecking(SymbolTable).getR()):
						print "ERROR: La cantidad de filas pedida es mayor a la cantidad de filas que tiene la matriz"
						exit() 


					return "number"

			else:

				if self.fila.typechecking(SymbolTable) <> "number":
					print "ERROR: La cantidad de fila pedida es mayor a la cantidad de filas que tiene la matriz"
					exit() 

				return "number"


class Expre_ReturnExpresion:
	"""Clase que maneja los return

		return <expresion>;
	"""

	#Constructor de la clase
	def __init__(self,expresion,row):
		
		self.expresion = expresion 	
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Return: "
		print cantidad, " Expresion: "
		self.expresion.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		self.expresion.typechecking(SymbolTable)


class Inst_PrintExpresion:
	"""Clase que maneja la impresion 

		print <Expresion>
	"""

	#Constructor de la clase
	def __init__(self,row,PrintExpresion):
		
		self.PrintExpresion = PrintExpresion 	
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion Print: "
		print cantidad, " Expresion: "
		for j in self.PrintExpresion:
			j.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		for j in self.PrintExpresion:
			j.typechecking(SymbolTable)

class Expre_UseIn:
	"""Clase que maneja los Use-In 

		use 
			<VariableDeclaration>
		in
			<Instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,declarations,instructions):
		
		self.declarations = declarations	#Lista de declaracion
		self.instructions = instructions 	#Lista de instruction
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion Use: "

		for i in self.declarations:
			print cantidad, " Declaracion: "
			i.printI(Identacion(cantidad))
	
		print cantidad, "Expresion In: "

		for j in self.instructions:
			print cantidad, " Instruccion: "
			j.printI(Identacion(cantidad))

	def typechecking(self,STable):

		NewSymbolTable = SymbolTable(STable)
		STable.born(NewSymbolTable)

		for i in self.declarations:

			if isinstance(i, Exp_Comments) or isinstance(i, Variable_Declaration) :
				i.typechecking(NewSymbolTable)	
			else:
				print "ERROR: dentro del alcance del USE no puede haber una instruccion que sea distinta de 'Declaracion de Variables'"
				exit()



		for j in self.instructions:

			if isinstance(j, Variable_Declaration):
				print "ERROR: solo se puede declarar variables dentro del alcance del USE"
				exit()

			j.typechecking(NewSymbolTable)		


class Expre_While:
	"""Clase que maneja los ciclos del while  

		while <condition> do 
			<Instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,condition,instructions=None):
		
		self.condition = condition	#Lista de condiciones
		self.instructions = instructions 	#Lista de instruction
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion While: "
		print cantidad, " Condicion: "
		self.condition.printI(Identacion(cantidad))

		for j in self.instructions:
			print cantidad, " Instruccion: "
			j.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		if self.condition.typechecking(SymbolTable) <> "boolean":
			print "ERROR: el tipo de la condicion del while no es un booleano"
			exit()

		for j in self.instructions:
			j.typechecking(SymbolTable)		


class Expre_For:
	"""Clase que maneja los ciclos del for  

		for <identificator> in <expression> do 
			<Instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,identificator,expression,instructions):
		
		self.identificator = identificator	#Lista de identificadores
		self.instructions = instructions 	#Lista de instruction
		self.expression = expression 		#Lista de expresion 
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion For: "
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))
		print cantidad, " Expresion: "
		self.expression.printI(Identacion(cantidad))
		for j in self.instructions:
			print cantidad, " Instruccion: "
			j.printI(Identacion(cantidad))

	def typechecking(self,STable):

		NewSymbolTable = SymbolTable(STable)
		STable.born(NewSymbolTable)

		NewSymbolTable.addSymbol(self.identificator.getValue(),"number")

		ExpressionType = self.expression.typechecking(NewSymbolTable)

		if isinstance(ExpressionType, Matrix):
			ExpressionType = ExpressionType.typechecking(NewSymbolTable)

		if ExpressionType <> "matriz":
			print "ERROR: la expresion no es de tipo matricial"
			exit()

		for j in self.instructions:
			j.typechecking(NewSymbolTable)


class LlamadoFunction:
	"""Clase que maneja las funciones 

		<identificator>(List<identificator>)

	"""

	#Constructor de la clase
	def __init__(self,row,identificator,ListIdentification=None):
		
		self.identificator = identificator	
		self.ListIdentification = ListIdentification 	#Lista de ListIdentification
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Funcion: "
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))
		for j in self.ListIdentification:
			print cantidad, " Parametro: "
			j.printI(Identacion(cantidad))

	def typechecking(self,STable):

		if STable.hasKey(self.identificator.getValue()) == False:
			print "ERROR: La funcion no existe"
			exit()

		FunctionType = STable.findTypeOf(self.identificator.getValue())

		returnType = FunctionType[0]
		ParameterOrder = FunctionType[1]
		FunctionTable = FunctionType[2]

		if len(ParameterOrder) <> len(self.ListIdentification):
			print "ERROR: la cantidad de parametros no son iguales"
			exit()

		i = 0

		while i < len(ParameterOrder):

			if FunctionTable.findTypeOf(ParameterOrder[i]) == "number" or FunctionTable.findTypeOf(ParameterOrder[i]) == "boolean":
				if FunctionTable.findTypeOf(ParameterOrder[i]) <> self.ListIdentification[i].typechecking(STable):
					print "ERROR: Los tipos de los paramatros no son iguales"
					exit()

			elif FunctionTable.findTypeOf(ParameterOrder[i]) == "matriz":

				if isinstance(self.ListIdentification[i].typechecking(STable), Matrix) == False:
					print "ERROR: Los tipos de los paramatros no son igualesss"
					exit()					

			i = i + 1

		if isinstance(returnType, str):
			return returnType

		return returnType.typechecking(STable)


class Function:
	"""Clase que maneja las funciones 

		function <identificator>(<variable_declaration>) return <type>
		begin
			<instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,identificator,returntype,instructions,variable_declaration=None):
		
		self.identificator = identificator	
		self.variable_declaration = variable_declaration 	#Lista de variable_declaration
		self.returntype = returntype
		self.instructions = instructions 		#Lista de instructions 
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Funcion: "
		print cantidad, " Identificador: "		
		self.identificator.printI(Identacion(cantidad))

		if self.variable_declaration <> None:

			for j in self.variable_declaration:
				print cantidad, " Parametro: "
				j.printI(Identacion(cantidad))


		print cantidad, " Retornar: "
		if (isinstance(self.returntype,str)):
			print cantidad, self.returntype
		else:
			self.returntype.printI(Identacion(cantidad))

		for i in self.instructions:
			print cantidad, " Instruccion: "

			if (isinstance(i,int) or isinstance(i,str)):
				print cantidad, i
			else:
				i.printI(Identacion(cantidad))

	def typechecking(self,STable):

		if STable.hasKey(self.identificator):
			print "ERROR: ya existe una funcion con ese Nombre"
			exit()

		NewSymbolTable = SymbolTable(STable)
		STable.born(NewSymbolTable)

		ParameterOrder = []

		if self.variable_declaration <> None:

			for i in self.variable_declaration:

				if NewSymbolTable.hasKey(i.getIdentificator()):
					print "ERROR: identificador ya fue declarado"
					exit()

				ParameterOrder.append(i.getIdentificator())
				NewSymbolTable.addSymbol(i.getIdentificator(),i.getType(STable))

		FunctionType = []

		FunctionType.append(self.returntype)
		FunctionType.append(ParameterOrder)
		FunctionType.append(NewSymbolTable)		

		STable.addSymbol(self.identificator.getValue(),FunctionType)

		#STable.printI(Identacion(""))

		for j in self.instructions:
			j.typechecking(NewSymbolTable)



# class Instruccion:
# 	"""Clase que maneja las Instruccion  

# 		<Instruccion>

# 	"""

# 	#Constructor de la clase
# 	def __init__(self,row,instruccion):
			
# 		self.instruccion = instruccion 		#Lista de instrucciones
# 		self.row = row
	
# 	def getRow(self):
# 		return set.row
	
# 	#Funcion para imprimir
# 	def printI(self, cantidad):

# 		print cantidad, "Instruccion: "
# 		for i in self.instruccion:
# 			print cantidad, " "
# 			i.printI(Identacion(cantidad))

class Exp_Comments:
	"""Clase que maneja los Comentarios   

		# <Comments>

	"""

	#Constructor de la clase
	def __init__(self,row,comentario):
			
		self.comentario = comentario 		
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Comentario: ", self.comentario

	def typechecking(self,SymbolTable):
		print "Revision "
		return "comments"

class Exp_Paren:
	"""Clase que maneja las expresiones binarias 

		(Exp)

	"""

	#Constructor de la clase
	def __init__(self,row,pareni,exp,parend):
		
		self.pareni = pareni	#Lista de expresiones al lado izq del operador
		self.exp = exp 	
		self.parend = parend 		#Lista de expresiones al lado der del operador 
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Parentesis Izq: "
		print cantidad, " Expresion: "
		self.exp.printI(Identacion(cantidad))
		print cantidad, "Parentesis Der"			

	def typechecking(self,SymbolTable):

		return self.exp.typechecking(SymbolTable)


class Exp_Binaria:
	"""Clase que maneja las expresiones binarias 

		Exp op Exp

	"""

	#Constructor de la clase
	def __init__(self,row,leftexpression,operator,rightexpression):
		
		self.leftexpression = leftexpression	#Lista de expresiones al lado izq del operador
		self.operator = operator 	
		self.rightexpression = rightexpression 		#Lista de expresiones al lado der del operador 
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Operador: ", str(symbolsDic[self.operator])
		print cantidad, " Expresion Izq: "
		self.leftexpression.printI(Identacion(cantidad))
		print cantidad, " Expresion Der: "
		self.rightexpression.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		RightType = self.rightexpression.typechecking(SymbolTable)
		LeftType = self.leftexpression.typechecking(SymbolTable)

		if isinstance(RightType, Matrix):
			RightType = RightType.typechecking(SymbolTable)

		if isinstance(LeftType, Matrix):
			LeftType = LeftType.typechecking(SymbolTable)

		A = self.operator == "+"
		B = self.operator == "-"
		C = self.operator == "*"
		D = self.operator == "\/"
		M = self.operator == "%"
		N = self.operator == "mod"
		O = self.operator == "div"

		E = self.operator == ">="
		F = self.operator == "<="
		G = self.operator == ">"
		H = self.operator == "<"

		I = self.operator == "=="
		J = self.operator == "/="

		K = self.operator == "&"
		L = self.operator == "|"

		P = self.operator == ".+."
		Q = self.operator == ".-."
		R = self.operator == ".*."
		S = self.operator == ".\/."
		T = self.operator == ".%."
		U = self.operator == ".mod."
		V = self.operator == ".div."

		if RightType == LeftType and RightType == "number":

			if A or B or C or D or M or N or O:
				return "number"

			elif E or F or G or H or I or J:
				return "boolean"

			else: 
				print "ERROR: El operador '", str(self.operator), "', no opera con numeros"
				exit()

		elif RightType == LeftType and RightType == "matriz":

			if A or B:

				if self.rightexpression.getR() == self.leftexpression.getR() and self.rightexpression.getC() == self.leftexpression.getC():
					return Matrix(Number(self.rightexpression.getR(),self.row),Number(self.rightexpression.getC(),self.row),self.row)

				else:
					print "ERROR: El tamanio de las filas y columna no son iguales"
					exit()

			elif C :

				if self.leftexpression.getC() == self.rightexpression.getR():
					return Matrix(Number(self.leftexpression.getR(),self.row),Number(self.rightexpression.getC(),self.row),self.row)

				else:
					print "ERROR: El tamanio de la columnas de la matriz izq no es igual a las filas de la matriz der"
					exit()

			elif I or J:
				return "boolean"

			else:
				print "ERROR: el operador no soporta operaciones con matrices"
				exit()

		elif (RightType == "matriz" and LeftType == "number"):

			if P or Q or R or S or T or U or V:
				return Matrix(Number(self.rightexpression.typechecking(SymbolTable).getR(),self.row),Number(self.rightexpression.typechecking(SymbolTable).getC(),self.row),self.row)
			else:
				print "ERROR: el operador no soporta operaciones entre matrices y numeros"
				exit()				


		elif (LeftType == "matriz" and RightType == "number"):
			
			if P or Q or R or S or T or U or V:

				return Matrix(Number(self.leftexpression.typechecking(SymbolTable).getR(),self.row),Number(self.leftexpression.typechecking(SymbolTable).getC(),self.row),self.row)
			else:
				print "ERROR: el operador no soporta operaciones entre matrices y numeros"
				exit()	

		elif RightType == LeftType and RightType == "boolean":

			if K or L or I or J:
				return "boolean"

			else:
				print "ERROR: el operador no soporta operaciones con booleanos"
				exit()

		else:

			print "ERROR: Los tipos de las expresiones no son comparables"
			exit()			

class Exp_Unaria:
	"""Clase que maneja las expresiones unarias 

		not Exp
	"""

	#Constructor de la clase
	def __init__(self,row,operator,rightexpression):
		
		self.operator = operator 	
		self.rightexpression = rightexpression 		#Lista de expresiones al lado der del operador 
		self.row = row
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Operador: not "
		self.rightexpression.printI(Identacion(cantidad))	

	def typechecking(self,SymbolTable):

		expType = self.rightexpression.typechecking(SymbolTable)

		if expType == "boolean":
			return "boolean"

		else:

			print "ERROR: La expresion: "
			self.rightexpression.printI(Identacion(cantidad))
			print "No es un booleano"
			exit()


class Exp_ProgramEnd:
	"""Clase que maneja las expresiones Program y End 

		<FunctionSpecification> 
		program
			<Instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,instructions= None,FunctionSpecification=None):
		
		self.FunctionSpecification = FunctionSpecification 	#Lista de FunctionSpecification
		self.instructions = instructions 		#Lista de instructions 
		self.row = row

		#self.printI("")
		NewSymbolTable = SymbolTable(None)

		#self.typechecking(NewSymbolTable)
	
	def getRow(self):
		return set.row
	
	#Funcion para imprimir el arbol
	def printI(self, cantidad):

		print cantidad, "TRINITY: "

		if self.FunctionSpecification:
			for j in self.FunctionSpecification:
				j.printI(Identacion(cantidad))

		print cantidad,"Abrir Program:"
		print cantidad,"  Instrucciones:"

		print cantidad, " Program: "
		
		if self.instructions:
			for i in self.instructions:
				i.printI(Identacion(cantidad))
		print cantidad, "Fin Del Progrma TRINITY"


	def typechecking(self,SymbolTable):

		if self.FunctionSpecification:
			for j in self.FunctionSpecification:
				j.typechecking(SymbolTable)
		
		if self.instructions:
			for i in self.instructions:
				i.typechecking(SymbolTable)
