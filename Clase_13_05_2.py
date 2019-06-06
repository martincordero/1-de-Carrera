ief calificación(nota):
    '''
    Función que devuelve la calificación correspondiente a una nota
    '''
    if nota<5:
        return 'SS'
    elif nota<7:
        return 'AP'
    elif nota<9:
        return 'NT'
    else:
        return 'SB'
    def aplica_calificación(notas):
        '''
        Función que devuelve una lista con las calificaciones
        '''
        return [calificación(x) for x in notas if x>=5 ]
    
