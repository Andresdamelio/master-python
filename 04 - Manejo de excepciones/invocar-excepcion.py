""" 
======================================================================
    Invocar excepciones
======================================================================
"""

def test(algo = None):
    try:
      if algo is None:
        raise ValueError("Error, no se permite un valor nulo")
    except ValueError as e:
      print(e)

test()