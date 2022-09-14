from smatrix import smatrix

def test_constructors():
  # All these constructors show succeed
  empty = smatrix.zeros(0)
  assert empty.data == []

  singleton = smatrix.zeros(1)
  assert singleton.data == [[0]]
  
  two = smatrix.zeros(2)
  assert two.data == [[0, 0], [0]]

def test_identity():
  empty = smatrix.identity(0)
  assert empty.data == []

  singleton = smatrix.identity(1)
  assert singleton.data == [[1]]
  
  two = smatrix.identity(2)
  assert two.data == [[1, 0], [1]]
  # Captures the idea of
  # 1 0
  # 0 1

  three = smatrix.identity(3)
  assert three.data == [[1, 0, 0], [1, 0], [1]]
  

def test_addition():
  singleton = smatrix.identity(1)
  empty = smatrix.zeros(1)
  assert(smatrix.add(singleton, empty) == singleton)

  doubled_identity = [[2]]
  assert(smatrix.add(singleton, singleton).data == doubled_identity)
