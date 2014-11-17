#!/usr/bin/python

'''
 Traductores e Interpretadores                                                       
 CI-3725  

 Integrantes:   

	 10-10738 Abelardo Jesus Valino Ovalle                                                
	 10-10353 Andres Rafael Hernandez Monterola

 Modulo Parser            

'''
import sys
import ply.yacc as yacc
import LexerF as Lexer
import Clases

#inicio del programa
start = ""


#Gramatica para el inicio del programa con o sin funciones
def p_ProgramEnd(p):
	'''ProgramEnd : Function TK_Program Instructions TK_End TK_Semicolon
				  | TK_Program Instructions TK_End TK_Semicolon'''

	if len(p) == 6:
		p[0] = Clases.Exp_ProgramEnd(p.lineno,p[3],p[1])
	else:
		p[0] = Clases.Exp_ProgramEnd(p.lineno,p[2])
	

#Gramatica para los identificadores
def p_ID(p):
	'''ID : TK_ID'''
	p[0] = Clases.Identificator(p[1],p.lineno)

#Gramatica para los Strings
def p_String(p):
	'''String : TK_String'''
	p[0] = Clases.String(p[1],p.lineno)

#Gramatica para los numeros
def p_Number(p):
	'''Number : TK_FNumber'''
	p[0] = Clases.Number(p[1],p.lineno)

#Gramatica para la declaracion de variables
def p_VariableDeclaration(p):
	'''VariableDeclaration : Type ID TK_Semicolon
						   | Type ID TK_Assign Expresion TK_Semicolon'''
	
	if len(p) == 6:	
		p[0] = Clases.Variable_Declaration(p.lineno,p[1],p[2],p[4]) 

	elif len(p) == 4:

		p[0] = Clases.Variable_Declaration(p.lineno,p[1], p[2]) 
	
#Gramatica para la asignacion
def p_Set(p):
	'''Set : TK_Set ID TK_Assign Expresion TK_Semicolon
		   | TK_Set Vector TK_Assign Expresion TK_Semicolon
		   | TK_Set ID TK_Assign LlamadoFuncion TK_Semicolon'''
	p[0] = Clases.Expre_Set(p[2],p[4],p.lineno) 

#Gramatica para los booleanos 
def p_Boolean(p):
	'''Boolean : TK_False
			   | TK_True '''
	p[0] = Clases.Boolean(p[1],p.lineno)

#Gramatica para los tipos de expresiones
def p_ExpresionAtom(p):
	'''Expresion : Boolean
				 | Number
				 | ID
				 | Vector
				 | MatrixFormatI'''

	p[0] = p[1]

#Gramatica para las expresiones en parentesis
def p_ExpresionParen(p):
	'''Expresion : TK_ParenI Expresion TK_ParenD'''

	p[0] = Clases.Exp_Paren(p.lineno,p[1],p[2],p[3])

#Gramatica para el not 
def p_ExpresionUnario(p):
	'''Expresion : TK_Not Expresion
				 | TK_Minus Expresion'''

	p[0] = Clases.Exp_Unaria(p.lineno,p[1],p[2])

#gramatica para los operadores binarios 
def p_ExpresionBinarios(p):
	'''Expresion : Expresion TK_Sum Expresion
				 | Expresion TK_Minus Expresion
				 | Expresion TK_Times Expresion
				 | Expresion TK_Divide Expresion
				 | Expresion TK_Div Expresion
				 | Expresion TK_Mod Expresion
				 | Expresion TK_ModS Expresion
				 | Expresion TK_Equal Expresion
				 | Expresion TK_Greatereq Expresion
				 | Expresion TK_Greater Expresion
				 | Expresion TK_Lesseq Expresion
				 | Expresion TK_Less Expresion
				 | Expresion TK_Distint Expresion
				 | Expresion TK_And Expresion
				 | Expresion TK_Or Expresion
				 | Expresion TK_Sumcross Expresion
				 | Expresion TK_Modcross Expresion
				 | Expresion TK_Minuscross Expresion
				 | Expresion TK_Divcross Expresion
				 | Expresion TK_ModScross Expresion
				 | Expresion TK_Dividecross Expresion
				 | Expresion TK_Timescross Expresion'''

	p[0] = Clases.Exp_Binaria(p.lineno,p[1],p[2],p[3])

#Gramatica para el return
def p_ReturnI(p):
	'''ReturnI : TK_Return Expresion TK_Semicolon'''
	p[0] = Clases.Expre_ReturnExpresion(p[2],p.lineno) 

#Gramatica para el Read
def p_Read(p):
	'''Read : TK_Read ID TK_Semicolon'''
	p[0] = Clases.Expre_Read(p[2],p.lineno) 

#Gramatica para los comentarios
def p_Comments(p):
	'''Comments : TK_CommentConNumeral'''
	p[0] = Clases.Exp_Comments(p.lineno,p[1]) 

#Gramatica para los prints
def p_Print(p):
	'''Print : TK_Print CommaString TK_Semicolon'''
	p[0] = Clases.Inst_PrintExpresion(p.lineno, p[2]) 

#Gramatica para la separacion de tipos de impresion
def p_CommaStringTipoDato(p): 
	''' CommaStringTipoDato : String
							| Expresion'''

	p[0] = p[1]

def p_CommaStringRecursive(p): 
	''' CommaString : CommaStringTipoDato
					| CommaString TK_Comma CommaStringTipoDato'''

	if len(p) == 2:
		p[0] = []
		p[0].append(p[1])
	elif len(p) == 4:
		p[0] = p[1]
		p[0].append(p[3])

#Gramatica para las instrucciones
def p_InstructionsRecursivo(p):
	'''Instructions : InstructionsBase
					| Instructions InstructionsBase'''

	if len(p) == 2:
		p[0] = []
		p[0].append(p[1])
	elif len(p) == 3:
		p[0] = p[1]
		p[0].append(p[2])

def p_InstructionsBase(p):
	'''InstructionsBase : Set
						| Read
						| Print
						| ReturnI
						| VariableDeclaration
						| If_Else
						| Use_In
						| While
						| For
						| LlamadoFuncion
						| Comments
						| Expresion TK_Semicolon'''

	p[0] = p[1]

#Gramatica para los condicionales IF y ELSE
def p_If_Else(p):
	'''If_Else : TK_If Expresion TK_Then Instructions TK_End TK_Semicolon
			   | TK_If Expresion TK_Then Instructions TK_Else Instructions TK_End TK_Semicolon'''


	if len(p) == 7:

		p[0] = Clases.Expre_If_Else(str(p.lineno),p[2],p[4])
	else:
		p[0] = Clases.Expre_If_Else(str(p.lineno),p[2],p[4],p[6])

#Gramatica para el formato de la matriz 
def p_MatrixFormat(p):
	'''MatrixFormatI : TK_KeyI MatrixNumber TK_KeyD'''

	p[2].append(":")
	p[0] = Clases.MatrixFormat(p.lineno,p[2])

def p_CommaNumber(p):
	'''CommaNumber : Expresion'''
	p[0] = []
	p[0].append(p[1])

def p_CommaNumberList(p):
	'''CommaNumber : CommaNumber TK_Comma Expresion'''
	p[0] = p[1]
	p[0].append(",")
	p[0].append(p[3])

def p_MatrixNumberBase(p):
	'''MatrixNumber : CommaNumber'''
	p[0] = p[1]

def p_MatrixNumberList(p):
	'''MatrixNumber : MatrixNumber TK_Colon CommaNumber'''
	p[0] = p[1]
	p[0].append(":")
 	for i in p[3]:
 		p[0].append(i)

#Gramatica para el Use-In
def p_Use_In(p):
	'''Use_In :  TK_Use Instructions TK_In Instructions TK_End TK_Semicolon
			  |  TK_Use Instructions TK_In TK_End TK_Semicolon '''

	p[0] = Clases.Expre_UseIn(p.lineno,p[2],p[4])

#Gramatica para el For
def p_For(p):
	'''For :  TK_For ID TK_In Expresion TK_Do Instructions TK_End TK_Semicolon'''
	p[0] = Clases.Expre_For(p.lineno,p[2],p[4],p[6])

#Gramatica para el While
def p_While(p):
	'''While :  TK_While Expresion TK_Do Instructions TK_End TK_Semicolon'''

	p[0] = Clases.Expre_While(p.lineno,p[2],p[4])

#Gramatica para los tipos
def p_Type(p):
	'''Type : TK_Bool
			| TK_Number
			| Matrix
			| Row
			| Column'''

	p[0] = p[1]

#Gramatica para las Funciones
def p_FunctionBase(p):
	'''Function :  TK_Function ID TK_ParenI Argumento TK_ParenD TK_Return Type TK_Begin Instructions TK_End TK_Semicolon
			    |  TK_Function ID TK_ParenI TK_ParenD TK_Return Type TK_Begin Instructions TK_End TK_Semicolon'''
	
	p[0] = []

	if len(p) == 12:
		p[0].append(Clases.Function(p.lineno,p[2],p[7],p[9],p[4]))	
	else:
		p[0].append(Clases.Function(p.lineno,p[2],p[6],p[8]))

def p_Function(p):
	'''Function : Function TK_Function ID TK_ParenI Argumento TK_ParenD TK_Return Type TK_Begin Instructions TK_End TK_Semicolon
			    | Function TK_Function ID TK_ParenI TK_ParenD TK_Return Type TK_Begin Instructions TK_End TK_Semicolon'''
	
	p[0] = p[1]
	if len(p) == 13:
		p[0].append(Clases.Function(p.lineno,p[3],p[8],p[10],p[5]))
	else:
		p[0].append(Clases.Function(p.lineno,p[3],p[7],p[9]))

#Gramatica para los argumentos dentro de las firmas de las funciones
def p_ArgumentoDeclaracionFuncionBase(p): 
	''' Argumento : Type ID'''

	p[0] = []
	p[0].append(Clases.Variable_Declaration(p.lineno, p[1], p[2]))

def p_ArgumentoDeclaracionFuncionRecursive(p): 
	''' Argumento : Argumento TK_Comma Type ID'''
	p[0] = p[1]
	p[0].append(Clases.Variable_Declaration(p.lineno, p[3], p[4]))

#Gramatica para la llamada de las funciones
def p_LlamadoFuncion(p):
	'''LlamadoFuncion : ID TK_ParenI Parameter TK_ParenD TK_Semicolon
					  | ID TK_ParenI TK_ParenD TK_Semicolon'''				

	if len(p) == 6:
		p[0] = Clases.LlamadoFunction(p.lineno,p[1],p[3])
	else:
		p[0] = Clases.LlamadoFunction(p.lineno,p[1])

#Gramatica para los paramatros que van dentro de las firmas de las funciones
def p_ParameterRecursive(p): 
	''' Parameter : Parameter TK_Comma Expresion'''
	

	p[0] = p[1]
	p[0].append(p[3])

def p_ParameterBase(p): 
	''' Parameter : Expresion'''

	p[0] = []
	p[0].append(p[1])

#Gramatica para el tipo matrix
def p_Matrix(p):
	'''Matrix : TK_Matrix TK_ParenI Number TK_Comma Number TK_ParenD
			  | TK_Matrix TK_ParenI ID TK_Comma ID TK_ParenD
			  | TK_Matrix TK_ParenI Number TK_Comma ID TK_ParenD
			  | TK_Matrix TK_ParenI ID TK_Comma Number TK_ParenD'''
	p[0] = Clases.Matrix(p[3],p[5],p.lineno)

#Gramatica para el tipo Row
def p_Row(p):
	'''Row : TK_Row TK_ParenI Number TK_ParenD 
		   | TK_Row TK_ParenI ID TK_ParenD '''
	p[0] = Clases.Matrix(Clases.Number(1,p.lineno),p[3],p.lineno)

#Gramatica para el tipo column
def p_Column(p):
	'''Column : TK_Col TK_ParenI Number TK_ParenD
			  | TK_Col TK_ParenI ID TK_ParenD'''
	p[0] = Clases.Matrix(p[3],Clases.Number(1,p.lineno),p.lineno)

#Gramatica para los vectores e[i,j] o e[i]
def p_Vector(p):
	''' Vector : Expresion TK_BracketI Expresion TK_BracketD
			   | Expresion TK_BracketI Expresion TK_Comma Expresion TK_BracketD'''

				 # ID TK_BracketI ID TK_BracketD
			  #  | ID TK_BracketI Number TK_BracketD
			  #  | ID TK_BracketI ID TK_Comma ID TK_BracketD
			  #  | ID TK_BracketI Number TK_Comma Number TK_BracketD
			  #  | ID TK_BracketI ID TK_Comma Number TK_BracketD
			  #  | ID TK_BracketI Number TK_Comma ID TK_BracketD
			  #  | Matrix TK_BracketI Number TK_Comma ID TK_BracketD
			  #  | Matrix TK_BracketI ID TK_Comma ID TK_BracketD
			  #  | Matrix TK_BracketI ID TK_Comma Number TK_BracketD
			  #  | Matrix TK_BracketI Number TK_Comma Number TK_BracketD

	if len(p) == 5:
		p[0] = Clases.Expre_Vector(p.lineno,p[1],p[3])
	else:
		p[0] = Clases.Expre_Vector(p.lineno,p[1],p[3],p[5])


# Error
def p_error(p):
#	print  "Error de sintaxis en linea %d,  columna %d: token  \'%s\'  inesperado." % (p.lineno, lexer.findCol(data, p), p.value[0])
#	print "Error de sintaxis"
	if p is not None:
	        print "Syntax error at line " + str(p.lineno) +  " Unexpected token  " + str(p.value) + ", " + str(p)
	        sys.exit(1)
	else:
	        print "Syntax error at line: " #+ str(cminus_lexer.lexer.lineno) 
	        sys.exit(1)


precedence = (
	('left','TK_Times','TK_Div','TK_Mod','TK_Divide','TK_ModS'),
	('left','TK_Sum','TK_Minus'),
	('left','TK_Sumcross','TK_Minuscross'),
	('left','TK_Timescross','TK_Divcross','TK_Modcross','TK_Dividecross','TK_ModScross'),
	('left','TK_Not'),
	('left','TK_And'),
	('left','TK_Or'),
	('nonassoc', 'TK_Assign','TK_Equal','TK_Distint','TK_Greater','TK_Greatereq','TK_Less','TK_Lesseq'),	
)


def AnalizadorParser(ArchivoTrinitytxt):

	try:


		tokens = Lexer.tokens
		#tokensEncontrados = Lexer.AnalizadorLex(ArchivoTrinitytxt)

		#Se abre el archivo 
		ArchivoTrinity = open(ArchivoTrinitytxt, 'r')
		
		global data

		#Se guarda en data lo que se encuentra en el ArchivoTrinity
		data = ArchivoTrinity.read()

		# Construimos el parser
		parser = yacc.yacc()

		parser.parse(data)

		#Se cierra el archivo
		ArchivoTrinity.close()

		return 0

	except IOError:

		print "ERROR: No se pudo abrir el ArchivoTrinity %s" % ArchivoTrinitytxt
		exit()	