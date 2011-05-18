'''
Created on 17 May 2011

@author: Moises Vega
'''

def HoppityHop( positiveInteger ):

    for anIterator in range( 1 , positiveInteger + 1 ):
        if( anIterator % 3 == 0 and anIterator % 5 == 0 ):
            print( "Hop" )
        elif anIterator % 3 == 0:
            print( "Hoppity" )
        elif anIterator % 5 == 0:
            print( "Hophop" )



HoppityHop( 15 )
