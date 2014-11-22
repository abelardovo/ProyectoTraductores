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
import numpy as np

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

Results = []


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
			sys.exit(1)

		self.dic[key] = value

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
		return self.row

	def getValue(self):
		return self.value

	def getInstance(self):
		return self.value

	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Literal Numerico Valor: ", self.value

	def typechecking(self,SymbolTable):

		return self.type

	def run(self,dic):

		return self.getValue()

class Identificator:
	"""Clase que maneja a los Identificador (ID)"""

	#Constructor de la clase
	def __init__(self,value,row):
		
		self.value = value
		self.row = row
		self.type = "id"
	
	def getRow(self):
		return self.row

	def getValue(self):
		return self.value
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Nombre: ", str(self.value)

	def findinDic(self,dic,identificador):

		i = len (Results) - 1

		while i >= 0:

			if Results[i].has_key(identificador):
				return Results[i][identificador]

			i = i-1

	def typechecking(self,SymbolTable):

		if SymbolTable.hasKey(self.value) == False:
			print "ERROR: El identificador no se encuentra en la Tabla de Simbolos: " + str(self.value)
			sys.exit(1)

		return SymbolTable.findTypeOf(self.value)

	def run(self,dic):

		return self.findinDic(dic,self.value)

class String:
	"""Clase que maneja a los String"""

	#Constructor de la clase
	def __init__(self,value,row):
		
		self.value = value
		self.row = row
		self.type = "string"

	
	def getRow(self):
		return self.row

	def getValue(self):
		return str(self.value)

	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, " String: ", self.value

	def typechecking(self,SymbolTable):

		return self.type

	def run(self,dic):

		return self.getValue()	

class Boolean:
	"""Clase que maneja a los Booleanos"""

	# Constructor de la clase
	def __init__(self,value,row):

		self.value = value
		self.row = row
		self.type = "boolean"
	
	def getRow(self):
		return self.row
		
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Boolean: "
		print cantidad, " Valor: ", str(self.value)		

	def typechecking(self,SymbolTable):

		return self.type

	def run(self,dic):

		if self.value == "true":
			return True
		elif self.value == "false":
			return False

		print "/ERROR/: EL boolenao mal declarado "
		sys.exit(1)

class Matrix:
	"""Clase que maneja a las Matrices "matrix(R,C)" """

	# Constructor de la clase
	def __init__(self,R,C,row):

		if isinstance(R.getInstance(),float) or isinstance(C.getInstance(),float):
			print "ERROR: Ni las filas ni las columnas pueden ser punto flotante"
			sys.exit(1)

		self.R = R
		self.C = C
		self.row = row
		self.type = "matriz"
	
	def getRow(self):
		return self.row

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

		if self.getR() == 0 or self.getC() == 0:
			print "ERROR: la matriz no puede ser declarada con filas o columnas iguales a cero"
			sys.exit(1)

		if self.R.typechecking(SymbolTable) <> "number" or self.C.typechecking(SymbolTable) <> "number":
			print "ERROR: R y C tienen que ser numeros"
			sys.exit(1)


		return self.type

class MatrixFormat:
	"""Clase que maneja a los formatos de las Matrices 
	"{valor1,valor2,valor3:valor4,valor5,valor6}" """

	# Constructor de la clase
	def __init__(self,row,MatrixValue):

		self.MatrixValue = MatrixValue 
		self.row = row
	
	def getRow(self):
		return self.row

	def transform(self):
		
		matrizPy = []
		listaAux = []

		for i in self.MatrixValue:
			if i == ",":
				pass
			elif i == ":":
				matrizPy.append(listaAux)
				listaAux = []
			else:
				listaAux.append(i.getValue())
		return matrizPy

	def getR(self):

		j = 1
		k = 1
		mayork = 1

		for i in self.MatrixValue:

			if i == ":":

				if j <> 1 and k <> mayork:
					print "ERROR: La cantidad de columnas no son iguales en todas las columnas"
					sys.exit(1)
					
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
					sys.exit(1)
					
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
					sys.exit(1)
					
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
					sys.exit(1)

				j = j + 1
				k = 1

			elif i == ",":
				k = k + 1

				if j == 1 and k > mayork:
					mayork = k

			else:

				if i.typechecking(SymbolTable) <> "number":
					print "ERROR: Los elementos de la matriz solo puede ser de tipo Numerico"
					sys.exit(1)

		return "matriz"
		#return Matrix(Number(self.getR(),self.row),Number(self.getC(),self.row),self.row)

	def run(self,dic):

		return self.transform()

class Expre_If_Else:
	"""Clase que maneja a los condicionales IF <condicion> THEN <Intrucciones> END;"""

	#Constructor de la clase
	def __init__(self,row,condition,instruction=None, instruction2 = None):
		
		self.condition = condition
		self.instruction = instruction
		self.instruction2 = instruction2
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion IF: "
		print cantidad, " Condicion: "
		self.condition.printI(Identacion(cantidad)) #imprime la condicion

		print cantidad, "Expresion THEN: "

		if self.instruction:
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
			sys.exit(1)

		if self.instruction:
			for j in self.instruction:
				j.typechecking(SymbolTable)	

		if self.instruction2:
			for k in self.instruction2:
				k.typechecking(SymbolTable)

	def run(self,dic):
		if self.condition.run(dic):
			if self.instruction:
				for j in self.instruction:
					j.run(dic)

		else:	
			if self.instruction2:
				for k in self.instruction2:
					k.run(dic)		



class Expre_Set:
	"""Clase que maneja los SET <ID> = expresion """

	# Constructor de la clase
	def __init__(self,identificator,expression,row):

		self.identificator = identificator 	
		self.expression = expression
		self.row = row
	
	def getRow(self):
		return self.row
		
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
			sys.exit(1)

		else:

			identificatorType = self.identificator.typechecking(SymbolTable)
			expressionType = self.expression.typechecking(SymbolTable)


			if expressionType == "matriz":
				expressionType = self.expression

			if identificatorType == "number" or identificatorType == "boolean" or expressionType== "number" or expressionType== "boolean":

				if identificatorType <> expressionType:
					print "ERROR: el tipo de las expresion es distinto al del identificador "
					sys.exit(1)

			elif (isinstance(identificatorType, Matrix) and isinstance(expressionType, Matrix)) or (isinstance(identificatorType, Matrix) and isinstance(expressionType, MatrixFormat)):

				if identificatorType.getR() <> expressionType.getR() or identificatorType.getC() <> expressionType.getC():
					print "ERROR: el tamanio de la matriz en el identificador es distinto al de la expresion"
					sys.exit(1)

	def run(self,dic):

		#print self.identificator

		dic[self.identificator.getValue()] = self.expression.run(dic)


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
		return self.row

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
			sys.exit(1)

		if self.expression <> None:

			if self.identificator_type == "number" or self.identificator_type == "boolean":

				if self.expression.typechecking(SymbolTable) <> self.identificator_type:
					print "ERROR: El tipo declarado no coincide con el tipo de la expresion"
					sys.exit(1)

			elif isinstance(self.identificator_type, Matrix):

				if isinstance(self.expression,MatrixFormat):

					if self.expression.typechecking(SymbolTable) <> "matriz":
						print "ERROR: El tipo declarado no coincide con el tipo de la expresion matrix"
						sys.exit(1)

					if self.expression.getR() <> self.identificator_type.getR() or self.expression.getC() <> self.identificator_type.getC():
						print "ERROR: Las filas o las columnas no coinciden"
						sys.exit(1)

				elif isinstance(self.expression,Exp_Binaria):

					if self.expression.typechecking(SymbolTable).typechecking(SymbolTable) <> "matriz":
						print "ERROR: El tipo declarado no coincide con el tipo de la expresion matrix"
						sys.exit(1)

					if self.expression.typechecking(SymbolTable).getR() <> self.identificator_type.getR() or self.expression.typechecking(SymbolTable).getC() <> self.identificator_type.getC():
						print "ERROR: Las filas o las columnas no coinciden"
						sys.exit(1)

		if isinstance(self.identificator_type,Matrix):
			self.identificator_type.typechecking(SymbolTable)

		SymbolTable.addSymbol(self.identificator.getValue(),self.identificator_type)

	def run(self,dic):

		if self.expression: 

			dic[self.identificator.getValue()] = self.expression.run(dic)

		else:

			dic[self.identificator.getValue()] = self.identificator_type



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
			sys.exit(1)

		if self.identificator.typechecking(SymbolTable) == "boolean" or self.identificator.typechecking(SymbolTable) == "number":
			pass
		
		else:

			print "ERROR: El identificador solo puede ser booleano o un numero"
			sys.exit(1)

	def run(self,dic):

		entrada = raw_input()

		if entrada== "true" and self.identificator.run(dic) == "boolean":

			entrada = True

		elif entrada== "false" and self.identificator.run(dic) == "boolean": 

			entrada = False 

		elif isinstance(int(entrada),int) and self.identificator.run(dic) == "number":

			entrada = int(entrada)

		else:

			print "ERROR: solo se aceptan booleanos o enteros y debe coincidir con el tipo declarado"
			exit()

		dic[self.identificator.getValue()] = entrada

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
		return self.row

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


		ExpresionBaseI = self.identificator

		if isinstance(ExpresionBaseI, Exp_Unaria):
			ExpresionBaseI.typechecking(SymbolTable)

		if isinstance(ExpresionBaseI, Identificator):

			if isinstance(ExpresionBaseI.typechecking(SymbolTable), Matrix) == False:
				print "ERROR: el identificador no es una matriz declarada"
				sys.exit(1)

			ExpresionBaseI = ExpresionBaseI.typechecking(SymbolTable)


		elif isinstance(ExpresionBaseI, Matrix) or isinstance(ExpresionBaseI, MatrixFormat):
			ExpresionBaseI = self.identificator
		
		elif isinstance(ExpresionBaseI, Exp_Binaria):
			ExpresionBaseI = ExpresionBaseI.typechecking(SymbolTable)



		if self.fila.typechecking(SymbolTable) <> "number":
			print "ERROR: el tipo de la fila tiene que ser un numero"
			sys.exit(1)

		else:

			if self.columna <> None:
				if self.columna.typechecking(SymbolTable) <> "number":
					print "ERROR: el tipo de la columna tiene que ser un numero"
					sys.exit(1)

				else: 

					# if (self.columna.getValue() > ExpresionBaseI.getC()):
					# 	print "ERROR: La cantidad de columnas pedida es mayor a la cantidad de columnas que tiene la matriz"
					# 	sys.exit(1) 

					# elif (self.fila.getValue() > ExpresionBaseI.getR()):
					# 	print "ERROR: La cantidad de filas pedida es mayor a la cantidad de filas que tiene la matriz"
					# 	sys.exit(1) 


					return "number"

			else:

				# if self.fila.typechecking(SymbolTable) <> "number":
				# 	print "ERROR: La cantidad de fila pedida es mayor a la cantidad de filas que tiene la matriz"
				# 	sys.exit(1) 

				return "number"

	def run(self, dic):


		ExpresionBaseI = self.identificator

		if isinstance(ExpresionBaseI, Exp_Unaria):
			ExpresionBaseI.run(dic)

		if isinstance(ExpresionBaseI, Identificator):
			ExpresionBaseI = ExpresionBaseI.run(dic)


		elif isinstance(ExpresionBaseI, Matrix) or isinstance(ExpresionBaseI, MatrixFormat):
			ExpresionBaseI = self.identificator.run(dic)
		
		elif isinstance(ExpresionBaseI, Exp_Binaria):
			ExpresionBaseI = ExpresionBaseI.run(dic)

		if self.columna:

			return ExpresionBaseI[self.fila.getValue() - 1][self.columna.getValue() - 1]

		return ExpresionBaseI[self.fila.getValue() -1 ]



class Expre_ReturnExpresion:
	"""Clase que maneja los return

		return <expresion>;
	"""

	#Constructor de la clase
	def __init__(self,expresion,row):
		
		self.expresion = expresion 	
		self.row = row
	
	def getRow(self):
		return self.row

	def getExpression(self):
		return self.expresion
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Return: "
		print cantidad, " Expresion: "
		self.expresion.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		return self.expresion.typechecking(SymbolTable)

	def run(self,dic):
		
		return self.expresion.run(dic)



class Inst_PrintExpresion:
	"""Clase que maneja la impresion 

		print <Expresion>
	"""

	#Constructor de la clase
	def __init__(self,row,PrintExpresion):
		
		self.PrintExpresion = PrintExpresion 	
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion Print: "
		print cantidad, " Expresion: "
		for j in self.PrintExpresion:
			j.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		for j in self.PrintExpresion:
			j.typechecking(SymbolTable)

	def run(self,dic):

		aux = ""
		for j in self.PrintExpresion:
			aux = aux + " " +str(j.run(dic))	

		print aux


class Expre_UseIn:
	"""Clase que maneja los Use-In 

		use 
			<VariableDeclaration>
		in
			<Instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,declarations=None,instructions=None):
		
		self.declarations = declarations	#Lista de declaracion
		self.instructions = instructions 	#Lista de instruction
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion Use: "

		if self.declarations:
			for i in self.declarations:
				print cantidad, " Declaracion: "
				i.printI(Identacion(cantidad))
	
		print cantidad, "Expresion In: "

		if self.instructions:
			for j in self.instructions:
				print cantidad, " Instruccion: "
				j.printI(Identacion(cantidad))

	def typechecking(self,STable):

		NewSymbolTable = SymbolTable(STable)
		STable.born(NewSymbolTable)

		if self.declarations:
			for i in self.declarations:

				if isinstance(i, Exp_Comments) or isinstance(i, Variable_Declaration) :
					i.typechecking(NewSymbolTable)	
				else:
					print "ERROR: dentro del alcance del USE no puede haber una instruccion que sea distinta de 'Declaracion de Variables'"
					sys.exit(1)


		if self.instructions:
			for j in self.instructions:

				if isinstance(j, Variable_Declaration):
					print "ERROR: solo se puede declarar variables dentro del alcance del USE"
					sys.exit(1)

				j.typechecking(NewSymbolTable)	

	def run(self, dic):

		dic= {}		
		Results.append(dic)


		if self.declarations:
			for i in self.declarations:
				i.run(dic)	

		if self.instructions:
			for j in self.instructions:
				j.run(dic)	

		Results.pop()



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
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion While: "
		print cantidad, " Condicion: "
		self.condition.printI(Identacion(cantidad))

		if self.instructions:
			for j in self.instructions:
				print cantidad, " Instruccion: "
				j.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):

		if self.condition.typechecking(SymbolTable) <> "boolean":
			print "ERROR: el tipo de la condicion del while no es un booleano"
			sys.exit(1)

		if self.instructions:
			for j in self.instructions:
				j.typechecking(SymbolTable)	

	def run(self,dic):

		while self.condition.run(dic):

			if self.instructions:
				for j in self.instructions:
					j.run(dic)			


class Expre_For:
	"""Clase que maneja los ciclos del for  

		for <identificator> in <expression> do 
			<Instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,identificator,expression,instructions=None):
		
		self.identificator = identificator	#Lista de identificadores
		self.instructions = instructions 	#Lista de instruction
		self.expression = expression 		#Lista de expresion 
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Expresion For: "
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))
		print cantidad, " Expresion: "
		self.expression.printI(Identacion(cantidad))

		if self.instructions:
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
			sys.exit(1)

		if self.instructions:

			for j in self.instructions:
				j.typechecking(NewSymbolTable)

	def run(self,dic):


		dic = {}

		Results.append(dic)

		ExpressionType = self.expression.run(dic)

		identificadorAux = self.identificator.getValue()

		dic[identificadorAux] = None

		for identificador in ExpressionType:
			
			for j in identificador:

				dic[identificadorAux] = j

				if self.instructions:

					for k in self.instructions:
						k.run(dic)

		Results.pop()


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
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Funcion: "
		print cantidad, " Identificador: "
		self.identificator.printI(Identacion(cantidad))

		if self.ListIdentification:
			for j in self.ListIdentification:
				print cantidad, " Parametro: "
				j.printI(Identacion(cantidad))

	def findinDic(self,dic,identificador):

		i = len (Results) - 1

		while i >= 0:

			if Results[i].has_key(identificador):
				return Results[i][identificador]

			i = i-1

	def typechecking(self,STable):

		if STable.hasKey(self.identificator.getValue()) == False:
			print "ERROR: La funcion no existe"
			sys.exit(1)

		FunctionType = STable.findTypeOf(self.identificator.getValue())

		returnType = FunctionType[0]
		ParameterOrder = FunctionType[1]
		FunctionTable = FunctionType[2]

		if self.ListIdentification:
			if len(ParameterOrder) <> len(self.ListIdentification):
				print "ERROR: la cantidad de parametros no son iguales"
				sys.exit(1)

			i = 0

			while i < len(ParameterOrder):


				if FunctionTable.findTypeOf(ParameterOrder[i]) == "number" or FunctionTable.findTypeOf(ParameterOrder[i]) == "boolean":
					if FunctionTable.findTypeOf(ParameterOrder[i]) <> self.ListIdentification[i].typechecking(STable):
						print "ERROR: Los tipos de los paramatros no son iguales"
						sys.exit(1)

				elif FunctionTable.findTypeOf(ParameterOrder[i]) == "matriz":

					if isinstance(self.ListIdentification[i].typechecking(STable), Matrix) == False:
						print "ERROR: Los tipos de los paramatros no son igualesss"
						sys.exit(1)	

				elif isinstance(FunctionTable.findTypeOf(ParameterOrder[i]), Matrix):

					if (FunctionTable.findTypeOf(ParameterOrder[i])).getR() <> self.ListIdentification[i].getR():
						print "ERROR: la cantidad de filas es distinta"
						sys.exit(1)

					elif FunctionTable.findTypeOf(ParameterOrder[i]).getC() <> self.ListIdentification[i].getC():
						print "ERROR: la cantidad de columnas es distinta"
						sys.exit(1)


				i = i + 1

		if isinstance(returnType, str):
			return returnType

		if isinstance(returnType, Matrix):
			return returnType

		return returnType.typechecking(STable)

	def run(self,dic):

		InstanceFuncion = self.findinDic(dic,self.identificator.getValue())

		listaAux = []

		for i in self.ListIdentification:

			listaAux.append(i.run(dic))

		dic = {}

		Results.append(dic)

		return InstanceFuncion.run2(dic,listaAux)




class Function:
	"""Clase que maneja las funciones 

		function <identificator>(<variable_declaration>) return <type>
		begin
			<instructions>
		end;

	"""

	#Constructor de la clase
	def __init__(self,row,identificator,returntype,instructions=None,variable_declaration=None):
		
		self.identificator = identificator	
		self.variable_declaration = variable_declaration 	#Lista de variable_declaration
		self.returntype = returntype
		self.instructions = instructions 		#Lista de instructions 
		self.row = row
	
	def getRow(self):
		return self.row

	def getVD(self):
		return self.variable_declaration

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
		
		if self.instructions:

			for i in self.instructions:
				print cantidad, " Instruccion: "

				if (isinstance(i,int) or isinstance(i,str)):
					print cantidad, i
				else:
					i.printI(Identacion(cantidad))

	def typechecking(self,STable):

		if STable.hasKey(self.identificator):
			print "ERROR: ya existe una funcion con ese Nombre"
			sys.exit(1)

		NewSymbolTable = SymbolTable(STable)
		STable.born(NewSymbolTable)

		ParameterOrder = []

		returnsDentroDeFuncion = []

		if self.variable_declaration <> None:

			for i in self.variable_declaration:

				if NewSymbolTable.hasKey(i.getIdentificator()):
					print "ERROR: identificador ya fue declarado"
					sys.exit(1)

				ParameterOrder.append(i.getIdentificator())
				NewSymbolTable.addSymbol(i.getIdentificator(),i.getType(STable))

		FunctionType = []

		FunctionType.append(self.returntype)
		FunctionType.append(ParameterOrder)
		FunctionType.append(NewSymbolTable)		

		STable.addSymbol(self.identificator.getValue(),FunctionType)

		if self.instructions:
			for j in self.instructions:

				if isinstance(j, Expre_ReturnExpresion):

					if j.typechecking(NewSymbolTable) <> "matriz":
						returnsDentroDeFuncion.append(j.typechecking(NewSymbolTable))
					else:
						returnsDentroDeFuncion.append(j.getExpression())

				j.typechecking(NewSymbolTable)


		SonDistintos = False

		if returnsDentroDeFuncion <> []:
			for k in returnsDentroDeFuncion:

				if k == self.returntype:
					pass
				elif (isinstance(k,Matrix) and isinstance(self.returntype,Matrix)) or (isinstance(k,MatrixFormat) and isinstance(self.returntype,Matrix)) or (isinstance(k,Matrix) and isinstance(self.returntype,MatrixFormat)) or (isinstance(k,MatrixFormat) and isinstance(self.returntype,MatrixFormat)) :

					if k.getR() <> self.returntype.getR() or k.getC() <> self.returntype.getC():
						print "ERROR: las matrices en los return son de distinto tamanio"
						sys.exit(1)
				else:
					SonDistintos = True

			
			if SonDistintos: 
				print "ERROR: los tipos de los return son distintos"
				sys.exit(1)

	def run(self,dic):

		dic[self.identificator.getValue()] = self

	def run2(self,dic, Parametros):

		if self.variable_declaration:
			i = len (self.variable_declaration) - 1
			while i>=0:

				dic[self.variable_declaration[i].getIdentificator()] = Parametros[i]

				i=i-1

		if self.instructions:
			for j in self.instructions:

				if isinstance(j,Expre_ReturnExpresion):
					return j.run(dic)

				

class Exp_Comments:
	"""Clase que maneja los Comentarios   

		# <Comments>

	"""

	#Constructor de la clase
	def __init__(self,row,comentario):
			
		self.comentario = comentario 		
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Comentario: ", self.comentario

	def typechecking(self,SymbolTable):
		return "comments"

	def run(self,dic):
		pass

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
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Parentesis Izq: "
		print cantidad, " Expresion: "
		self.exp.printI(Identacion(cantidad))
		print cantidad, "Parentesis Der"			

	def typechecking(self,SymbolTable):

		return self.exp.typechecking(SymbolTable)

	def run(self,dic):
		return self.exp.run(dic)


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
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Operador: ", str(symbolsDic[self.operator])
		print cantidad, " Expresion Izq: "
		self.leftexpression.printI(Identacion(cantidad))
		print cantidad, " Expresion Der: "
		self.rightexpression.printI(Identacion(cantidad))

	def typechecking(self,SymbolTable):


		ExpresionBaseR =  self.rightexpression
		ExpresionBaseL = self.leftexpression

		RightType = ExpresionBaseR.typechecking(SymbolTable)
		LeftType = ExpresionBaseL.typechecking(SymbolTable)

		if isinstance(RightType, Matrix):
			RightType = RightType.typechecking(SymbolTable)

		if isinstance(LeftType, Matrix):
			LeftType = LeftType.typechecking(SymbolTable)

		if isinstance(ExpresionBaseL, Exp_Binaria):
			ExpresionBaseL = ExpresionBaseL.typechecking(SymbolTable)

		if isinstance(ExpresionBaseR, Exp_Binaria):
			ExpresionBaseR = ExpresionBaseR.typechecking(SymbolTable)

		if isinstance(ExpresionBaseL, Exp_Unaria):
			ExpresionBaseL = ExpresionBaseL.typechecking(SymbolTable)

		if isinstance(ExpresionBaseR, Exp_Unaria):
			ExpresionBaseR = ExpresionBaseR.typechecking(SymbolTable)

		if isinstance(ExpresionBaseL, LlamadoFunction):
			ExpresionBaseL = ExpresionBaseL.typechecking(SymbolTable)

		if isinstance(ExpresionBaseR, LlamadoFunction):
			ExpresionBaseR = ExpresionBaseR.typechecking(SymbolTable)


		A = self.operator == "+"
		B = self.operator == "-"
		C = self.operator == "*"
		D = self.operator == "/"
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
		S = self.operator == "./."
		T = self.operator == ".%."
		U = self.operator == ".mod."
		V = self.operator == ".div."

		# print LeftType,RightType

		if RightType == LeftType and RightType == "number":

			if A or B or C or D or M or N or O:
				return "number"

			elif E or F or G or H or I or J:
				return "boolean"

			else: 
				print "ERROR: El operador '", str(self.operator), "', no opera con numeros"
				sys.exit(1)

		elif RightType == LeftType and RightType == "matriz":


			if A or B:

				if ExpresionBaseR.getR() == ExpresionBaseL.getR() and ExpresionBaseR.getC() == ExpresionBaseL.getC():
					return Matrix(Number(ExpresionBaseR.getR(),self.row),Number(ExpresionBaseR.getC(),self.row),self.row)

				else:
					print "ERROR: El tamanio de las filas y columna no son iguales"
					sys.exit(1)

			elif C :

				if ExpresionBaseL.getC() == ExpresionBaseR.getR():
					return Matrix(Number(ExpresionBaseL.getR(),self.row),Number(ExpresionBaseR.getC(),self.row),self.row)

				else:
					print "ERROR: El tamanio de la columnas de la matriz izq no es igual a las filas de la matriz der"
					sys.exit(1)

			elif I or J:
				
				if ExpresionBaseR.getR() == ExpresionBaseL.getR() and ExpresionBaseR.getC() == ExpresionBaseL.getC():
					return "boolean"

				else:
					print "ERROR: El tamanio de las filas y columna no son iguales"
					sys.exit(1)
				return "boolean"

			else:
				print "ERROR: el operador no soporta operaciones con matrices"
				sys.exit(1)

		elif (RightType == "matriz" and LeftType == "number"):

			if P or Q or R or S or T or U or V:
				return Matrix(Number(ExpresionBaseR.getR(),self.row),Number(ExpresionBaseR.getC(),self.row),self.row)
			else:
				print "ERROR: el operador no soporta operaciones entre matrices y numeros"
				sys.exit(1)				


		elif (LeftType == "matriz" and RightType == "number"):
			
			if P or Q or R or S or T or U or V:

				return Matrix(Number(ExpresionBaseL.getR(),self.row),Number(ExpresionBaseL.getC(),self.row),self.row)
			else:
				print "ERROR: el operador no soporta operaciones entre matrices y numeros"
				sys.exit(1)	

		elif RightType == LeftType and RightType == "boolean":

			if K or L or I or J:
				return "boolean"

			else:
				print "ERROR: el operador no soporta operaciones con booleanos"
				sys.exit(1)

		else:

			print "ERROR: Los tipos de las expresiones no son comparables"
			sys.exit(1)	


	def run(self,dic):

		ExpresionBaseR =  self.rightexpression
		ExpresionBaseL = self.leftexpression

		RightType = ExpresionBaseR.run(dic)
		LeftType = ExpresionBaseL.run(dic)

		if isinstance(ExpresionBaseL, Identificator):
			ExpresionBaseL = Number(ExpresionBaseL.run(dic),ExpresionBaseL.getRow())

		if isinstance(ExpresionBaseR, Identificator):
			ExpresionBaseR = Number(ExpresionBaseR.run(dic),ExpresionBaseR.getRow())

		if isinstance(ExpresionBaseL, Exp_Binaria):
			ExpresionBaseL = Number(ExpresionBaseL.run(dic),ExpresionBaseL.getRow())

		if isinstance(ExpresionBaseR, Exp_Binaria):
			ExpresionBaseR = Number(ExpresionBaseR.run(dic),ExpresionBaseR.getRow())

		if isinstance(ExpresionBaseL, Exp_Unaria):
			ExpresionBaseL = Number(ExpresionBaseL.run(dic),ExpresionBaseL.getRow())

		if isinstance(ExpresionBaseR, Exp_Unaria):
			ExpresionBaseR = Number(ExpresionBaseR.run(dic),ExpresionBaseR.getRow())

		if isinstance(ExpresionBaseL, LlamadoFunction):
			ExpresionBaseL = ExpresionBaseL.run(dic)

		if isinstance(ExpresionBaseR, LlamadoFunction):
			ExpresionBaseR = ExpresionBaseR.run(dic)

		if isinstance(ExpresionBaseR,Number) and isinstance(ExpresionBaseL,Number):

			if self.operator == "+":
				return LeftType + RightType
			elif self.operator == "-":
				return LeftType - RightType
			elif self.operator == "*":
				return LeftType * RightType
			elif self.operator == "/":
				return LeftType / RightType
			elif self.operator == "%":
				return LeftType % RightType
			elif self.operator == "div":
				return int(LeftType / RightType)
			elif self.operator == "mod":
				return LeftType % RightType
			elif self.operator == "==":
				return LeftType == RightType
			elif self.operator == "/=":
				return LeftType != RightType
			elif self.operator == "<":
				return LeftType < RightType
			elif self.operator == ">":
				return LeftType > RightType
			elif self.operator == "<=":
				return LeftType <= RightType
			elif self.operator == ">=":
				return LeftType >= RightType

		elif isinstance(ExpresionBaseR,Boolean) and isinstance(ExpresionBaseL,Boolean):
			
			if self.operator == "==":
				return LeftType == RightType

			elif self.operator == "/=":
				return LeftType != RightType

			elif self.operator == "&":
				return LeftType and RightType

			elif self.operator == "|":
				return LeftType or RightType

		elif isinstance(ExpresionBaseR,MatrixFormat) and isinstance(ExpresionBaseL,MatrixFormat):

			MatrizIzq = np.matrix(ExpresionBaseL.run(dic))
			MatrizDer = np.matrix(ExpresionBaseR.run(dic))

			if self.operator == "+":
				return MatrizIzq + MatrizDer
			if self.operator == "-":
				return MatrizIzq - MatrizDer
			if self.operator == "*":
				return MatrizIzq * MatrizDer

		elif isinstance(ExpresionBaseR,MatrixFormat) and isinstance(ExpresionBaseL,Number):
			
			MatrizDer = np.matrix(ExpresionBaseR.run(dic))

			if self.operator == ".+.":
				return LeftType + MatrizDer
			elif self.operator == ".-.":
				return LeftType - MatrizDer
			elif self.operator == ".*.":
				return LeftType * MatrizDer
			elif self.operator == "./.":
				return LeftType / MatrizDer
			elif self.operator == ".mod.":
				return LeftType % MatrizDer
			elif self.operator == ".%.":
				return LeftType % MatrizDer
			elif self.operator == ".div.":
				return LeftType / MatrizDer

		elif isinstance(ExpresionBaseL,MatrixFormat) and isinstance(ExpresionBaseR,Number):
			
			MatrizIzq = np.matrix(ExpresionBaseL.run(dic))

			if self.operator == ".+.":
				return MatrizIzq + RightType
			elif self.operator == ".-.":
				return MatrizIzq - RightType
			elif self.operator == ".*.":
				return MatrizIzq * RightType
			elif self.operator == "./.":
				return MatrizIzq / RightType
			elif self.operator == ".mod.":
				return MatrizIzq % RightType
			elif self.operator == ".%.":
				return MatrizIzq % RightType
			elif self.operator == ".div.":
				return MatrizIzq / RightType


class Exp_Unaria:
	"""Clase que maneja las expresiones unarias 

		not Exp
		- Exp
		exp '
	"""

	#Constructor de la clase
	def __init__(self,row,operator,rightexpression):
		
		self.operator = operator 	
		self.rightexpression = rightexpression 		#Lista de expresiones al lado der del operador 
		self.row = row
	
	def getRow(self):
		return self.row
	
	#Funcion para imprimir
	def printI(self, cantidad):

		print cantidad, "Operador: not "
		self.rightexpression.printI(Identacion(cantidad))	

	def typechecking(self,SymbolTable):

		expType = self.rightexpression.typechecking(SymbolTable)

		if expType == "boolean" and self.operator == "not":
			return "boolean"

		elif expType == "number" and self.operator == "-":
			return "number"

		elif ((isinstance(expType, Exp_Unaria) or isinstance(expType, Matrix) ) and self.operator == "'"):

			return Matrix(Number(expType.getC(),self.row),Number(expType.getR(),self.row),self.row) 

		elif ((isinstance(expType, Exp_Unaria) or isinstance(expType, Matrix) ) and self.operator == "-"):

			return Matrix(Number(expType.getR(),self.row),Number(expType.getC(),self.row),self.row) 

		elif (expType == "matriz" and self.operator == "-"):
			

			return Matrix(Number(self.rightexpression.getR(),self.row),Number(self.rightexpression.getC(),self.row),self.row) 


		elif (expType == "matriz" and self.operator == "'"):
			
			return Matrix(Number(self.rightexpression.getC(),self.row),Number(self.rightexpression.getR(),self.row),self.row) 

			# return "matriz"

		else:

			print "ERROR: La expresion: "
			self.rightexpression.printI("")
			sys.exit(1)

	def run(self, dic):

		expType = self.rightexpression.run(dic)

		if isinstance(expType,bool) and self.operator == "not":

			return not (expType)

		elif isinstance(expType, int) and self.operator == "-":
			return -(expType)

		elif ((isinstance(expType, Exp_Unaria) or isinstance(expType, Matrix) ) and self.operator == "'"):

			return Matrix(Number(expType.getC(),self.row),Number(expType.getR(),self.row),self.row) 

		elif ((isinstance(expType, Exp_Unaria) or isinstance(expType, Matrix) ) and self.operator == "-"):

			return Matrix(Number(expType.getR(),self.row),Number(expType.getC(),self.row),self.row) 

		elif (expType == "matriz" and self.operator == "-"):
			

			return Matrix(Number(self.rightexpression.getR(),self.row),Number(self.rightexpression.getC(),self.row),self.row) 


		elif (expType == "matriz" and self.operator == "'"):
			
			return Matrix(Number(self.rightexpression.getC(),self.row),Number(self.rightexpression.getR(),self.row),self.row) 

			# return "matriz"

		else:

			print "ERROR: La expresion: "
			self.rightexpression.printI("")
			sys.exit(1)



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

		self.typechecking(NewSymbolTable)
		self.run({})
	
	def getRow(self):
		return self.row
	
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

	def run(self,dic):

		if self.FunctionSpecification:
			for j in self.FunctionSpecification:
				j.run(dic)

		Results.append(dic)
		
		if self.instructions:
			for i in self.instructions:				
				i.run(dic)

