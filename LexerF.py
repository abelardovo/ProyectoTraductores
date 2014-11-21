#!/usr/bin/python

'''
 Traductores e Interpretadores                                                       
 CI-3725  

 Integrantes:   

	 10-10738 Abelardo Jesus Valino Ovalle                                                
	 10-10353 Andres Rafael Hernandez Monterola
	 hola

 Modulo Lexer            

'''

import ply.lex as lex
import sys

reservado = {
	'false'		: 'TK_False',
	'true'		: 'TK_True',
	'boolean'	: 'TK_Bool',
	'number'	: 'TK_Number',
	'matrix'	: 'TK_Matrix',
	'row'		: 'TK_Row',
	'col'		: 'TK_Col',
	'program'	: 'TK_Program',
	'use'		: 'TK_Use',
	'in'		: 'TK_In',
	'print'		: 'TK_Print',
	'read'		: 'TK_Read',
	'if'		: 'TK_If',
	'then'		: 'TK_Then',
	'else'		: 'TK_Else',
	'end'		: 'TK_End',
	'set'		: 'TK_Set',
	'for'		: 'TK_For',
	'do'		: 'TK_Do',
	'not'		: 'TK_Not',
	'div'		: 'TK_Div',
	'mod'		: 'TK_Mod',
	'while'		: 'TK_While',
	'return'	: 'TK_Return',
	'function'	: 'TK_Function',
	'begin'		: 'TK_Begin'
}

tokens = [

	'TK_Divide', 
	'TK_ModS', 
	'TK_Comma', 
	'TK_Colon', 
	'TK_ID', 
	'TK_NuevaLinea',
	'TK_Minus', 
	'TK_Timescross',
	'TK_Times',
	'TK_Less', 
	'TK_Sum', 
	'TK_Sumcross',
	'TK_Greater', 
	'TK_Greatereq', 
	'TK_Lesseq', 
	'TK_Distint', 
	'TK_And', 
	'TK_Or', 
	'TK_Equal', 
	'TK_KeyI', 
	'TK_KeyD', 
	'TK_CommentConNumeral',
	'TK_ParenI', 
	'TK_ParenD', 
	'TK_FNumber', 
	'TK_Minuscross', 
	'TK_String', 
	'TK_Assign', 
	'TK_Semicolon',
	'TK_Modcross',
	'TK_Divcross',
	'TK_ModScross',
	'TK_Dividecross',
	'TK_Comit',
	'TK_BracketI',
	'TK_BracketD'
	] + list(reservado.values())

t_TK_Comma 		= r'\,'
t_TK_Colon 		= r'\:'
t_TK_Semicolon 	= r'\;'
t_TK_Divide 	= r'\/'
t_TK_ModS 		= r'\%'
t_TK_KeyI 		= r'\{'
t_TK_KeyD 		= r'\}'
t_TK_ParenI 	= r'\('
t_TK_ParenD 	= r'\)'
t_TK_BracketI 	= r'\['
t_TK_BracketD 	= r'\]'
t_TK_And 		= r'\&'
t_TK_Or 		= r'\|'
t_TK_Equal 		= r'\=\='
t_TK_Assign 	= r'\='
t_TK_Distint 	= r'\/\='
t_TK_Greatereq 	= r'\>\='
t_TK_Greater 	= r'\>'
t_TK_Lesseq 	= r'\<\='
t_TK_Less 		= r'\<'
t_TK_Sum 		= r'\+'
t_TK_Minus 		= r'\-'
t_TK_Times 		= r'\*'
t_TK_Sumcross 	= r'\.\+\.'
t_TK_Minuscross = r'\.\-\.'
t_TK_Timescross = r'\.\*\.'
t_TK_Modcross 	= r'\.mod\.'
t_TK_Divcross 	= r'\.div\.'
t_TK_ModScross 	= r'\.\%\.'
t_TK_Dividecross= r'\.\/\.'
t_TK_Comit		= r'\''
t_ignore 		= ' \t'

''' Definimos las funciones para los Token que tienen un valor, 
	tales como son los numeros y las variables.'''

''' Funcion para Numeros Decimales o Punto Flotantes'''
def t_TK_FNumber(t):
	r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
	try:
		t.value = int(t.value)
		return t

	except ValueError:
		t.value = float(t.value)
		return t		

''' Funcion para cadena de caracteres '''
def t_TK_ID(t):
	r'[a-zA-Z]([a-zA-Z_\d])*'
	t.type = reservado.get(t.value,'TK_ID') 
	return t

'''Funcion para manejar los Saltos de Linea'''
def t_TK_NuevaLinea(t):
	r'\n+'
	t.lexer.lineno += len(t.value) 

'''Funcion para Comentarios'''
def t_TK_CommentConNumeral(t):
	r'\#.*'
	t.type = reservado.get(t.value,'TK_CommentConNumeral') 
	return t

'''Funcion para TK_String'''
def t_TK_String(t):
	r'\".*?\"'
	t.type = reservado.get(t.value,'TK_String') 
	return t

'''Manejador de Errores'''
def t_error(t):
    ErroresEncontrados.append(t)
    t.lexer.skip(1)

'''Funcion para conseguir columna'''
def find_column(input,token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
		last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

'''Procedimiento interpretador del codigo'''
def AnalizadorLex(ArchivoTrinitytxt):

	try:
		# Construimos el lexer
		lexer = lex.lex()

		#Se Construye una lista con los tokens encontrados 
		TokensEncontrados = []

		#Se Construye una lista con los tokens que no pertenecen al lenguaje
		global ErroresEncontrados 
		ErroresEncontrados = []

		#Se abre el archivo 
		ArchivoTrinity = open(ArchivoTrinitytxt, 'r')

		#Se guarda en data lo que se encuentra en el ArchivoTrinity
		data = ArchivoTrinity.read()

		lexer.input(data)

		#Se revisa hasta que no haya mas tokens
		while True:
		    tok = lexer.token()
		    if not tok: break      

		    TokensEncontrados.append(tok)

		#Se cierra el archivo
		ArchivoTrinity.close()

	except IOError:

		print "ERROR: No se pudo abrir el ArchivoTrinity %s" % ArchivoTrinitytxt
		exit()

	#Se clasifican los tokens encontrados
	if (len(ErroresEncontrados) == 0):

		# i = 0

		# while i < len(TokensEncontrados):

		# 	Actual = TokensEncontrados[i]

		# 	if Actual.type == 'TK_FNumber':
		# 		print "%s : Linea: %d, Columna: %d  %d" % (Actual.type, Actual.lineno, find_column(data,Actual),Actual.value)
		# 	elif (Actual.type == 'TK_ID') or (Actual.type == 'TK_String') or (Actual.type == 'TK_CommentConNumeral'):
		# 		print "%s : Linea: %d, Columna: %d  %s " % (Actual.type, Actual.lineno, find_column(data,Actual),Actual.value)
		# 	else :
		# 		print "%s : Linea: %d, Columna: %d" %(Actual.type, Actual.lineno, find_column(data,Actual))
			
		# 	i = i +1

		return TokensEncontrados;

	else :
		#Si hay errores, se expresan en consola

		j = 0

		while j < len(ErroresEncontrados):

			ERROR = ErroresEncontrados[j]
			
			print "ERROR: Caracter no perteneciente al lenguaje Trinity"
			print "       '%s' : Linea: %d, Columna: %d" % (ERROR.value[0], ERROR.lineno, find_column(data,ERROR) )

			j = j + 1