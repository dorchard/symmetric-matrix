from smatrix import smatrix

def test_constructors():
  # All these constructors should succeed
  empty = smatrix.zeros(0)
  assert empty.data == []

  singleton = smatrix.zeros(1)
  assert singleton.data == [[0]]

  two = smatrix.zeros(2)
  assert two.data == [[0, 0], [0]]


def test_identity():
  # 1 0
  # 0 1
  empty = smatrix.identity(0)
  assert empty.data == []

  singleton = smatrix.identity(1)
  assert singleton.data == [[1]]

  two = smatrix.identity(2)
  assert two.data == [[1, 0], [1]]

  four = smatrix.identity(4)
  assert four.data == [[1, 0, 0, 0], [1, 0, 0], [1, 0], [1]]