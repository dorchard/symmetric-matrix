import typing
import itertools

def zeros(shape: int):
    """
    Return an symmetric matrix of given shape and type, filled with zeros.
    Parameters
    ----------
    shape : int
        Shape of the matrix

    Returns
    -------
    out : Smatrix
        Zero matrix of given shape.
    """
    row_sizes = range(shape, 0, -1)
    zeros_data = [[0.0 for _ in range(0, row_size)] for row_size in row_sizes]
    return Smatrix(shape, zeros_data)
    
class Smatrix:
    # Attributes
    shape: int        = 0
    data: list[float] = []

    """
    Construct a symmetrix matrix (necessarily a square matrix)

    Parameters
    ----------
    shape : int
        Size of the matrix

    data : {sequence of sequence of floats}
        Data for the symmetric matrix in row-order, where len(data[i]) = shape[i]
    """
    def __init__(self, shape: int, data: list[float]):
        # Check invariants on relationship between shape and data
        for row, size in zip(data, range(shape, 0, -1)):
            if len(row) != size:
                raise RuntimeError('Invalid data', 'Row of length ' + str(len(row))
                                                 + ' should be of length ' + str(size))
        # If we have reached here then the data invariant is met
        self.shape = shape
        self.data  = data

def transpose(m):
    return m

# (...this only works for 1,2,3-matrices... shhhhh)
def transpose_alt(m):
    l = m.shape
    d = list(reversed(list(itertools.chain.from_iterable(m.data))))
    if l > 0 and l % 2 == 0:
        tmp = d[l//2 - 1]
        d[l//2 - 1] = d[l//2]
        d[l//2] = tmp
    m.data = unflatten(d, l)
    return m

def unflatten(l, n):
    """
    Takes a flat list and a shape, and
    attempts to create an smatrix of the requested shape.
    """
    ls = []
    i = 0
    j = 0
    for el in l:
        if j == 0:
            ls.append([])
        ls[i].append(el)
        if j == (n-1) - i:
            i += 1
            j = 0
        else:
            j += 1
    return ls
