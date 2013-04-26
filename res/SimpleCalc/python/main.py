# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label           
import re

def names_to_buttons( names, op, targetLayout ) : 
	for name in names :
		b = Button( text=str(name), font_size=24 )
		b.bind( on_press=op )
		targetLayout.add_widget( b )		

class SimpleCalc( BoxLayout ) :

	def __init__( self, **kargs ) :
		BoxLayout.__init__( self, orientation="vertical" )

		#Kivy's Label supports unicode texts and bbcode for text makeup!!
		self.lblDisplay = Label( text="", \
                                 size_hint=(1, 0.3), \
                                 font_size=28
                               ) 

		#A container for the buttons
		buttons = GridLayout( cols=4, size_hint=(1, 0.7) )

		#Generating labels for the buttons
		names = [ "+", "-", "*", "/" ] + list( range( 1, 10 ) )+["0", "."]

		#Generating the buttons
		names_to_buttons( names, self.update, buttons ) 

		#A button to commit operations
		btnCalc = Button( text="=", size_hint=(1, 0.15), font_size=24  ) 
		btnCalc.bind( on_press=self.calc )

		#A button to clear all
		btnClear = Button( text="Clear", size_hint=(1, 0.15), font_size=24  ) 
		btnClear.bind( on_press=self.clear )

		#Adding all this widget to the main one
		self.add_widget( self.lblDisplay )
		self.add_widget( buttons )
		self.add_widget( btnCalc )
		self.add_widget( btnClear )
			
	def update( self, instance ) :
		self.lblDisplay.text += instance.text

	def clear( self, instance ) :
		self.lblDisplay.text = ""

	#Same approach used in the Java code
	def calc_JAVA_LIKE( self, instance ) :
		operands = []
		labels = []
		pattern = re.compile( "[+\\-*/]" )

		for operand in pattern.split( self.lblDisplay.text ) :
			operands.append( float(operand) )
			labels.append( operand )
		
		result = 0
		j = 0
		for i in range( 0, len( operands ) ) : 
			operand = operands[i]
			label = labels[i]
			operator = self.lblDisplay.text[j]
			j += len( label )
			if   operator == "*": result *= operand
			elif operator == "-": result -= operand
			elif operator == "/": result /= operand
			else: result += operand
		self.lblDisplay.text = str( result )

	#Using list comprehension
	def calc_LIST_COMPREHENSION( self, instance ) :	
		pattern = re.compile("[+\\-*/]")
		result = 0
		j = 0
		for operand, label in [ ( float(n), n ) for n in pattern.split(self.lblDisplay.text) ] :
			operator = self.lblDisplay.text[j]
			j += len( label )
			if   operator == "*": result *= operand
			elif operator == "-": result -= operand
			elif operator == "/": result /= operand
			else: result += operand
		self.lblDisplay.text = str( result )

	#Using eval
	def calc( self, instance ) :
		self.lblDisplay.text = str( eval(self.lblDisplay.text) )

class SimpleCalcApp( App ) : 

    title = 'Simple Calc'
    
    def build( self ) :
        return SimpleCalc()

    def on_pause( self ) : 
         return True

if __name__ in [ "__android__", "__main__" ] :
    SimpleCalcApp().run()
