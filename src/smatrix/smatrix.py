import typing

def descending_range(upper: int):
    return range(upper, 0, -1)

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
    row_sizes = descending_range(shape)
    zeros_data = [[0.0 for _ in range(0, row_size)] for row_size in row_sizes]
    return Smatrix(shape, zeros_data)

def identity(shape: int):
    """
    Return a symmetric identity matrix based on the shape (size) given.

    Parameters
    ----------
    shape : int
        Shape of the matrix

    Returns
    -------
    out : Smatrix
        Identity matrix of the given shape.
    """
    row_sizes = descending_range(shape)
    data = [[1.0] + [0.0 for _ in range(0, row_size - 1)] for row_size in row_sizes]
    return Smatrix(shape, data)

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
                raise ValueError('Invalid data', 'Row of length ' + str(len(row))
                                                 + ' should be of length ' + str(size))
        # If we have reached here then the data invariant is met
        self.shape = shape
        self.data  = data

def add(mat1: Smatrix, mat2: Smatrix) -> Smatrix:
    """
    Add two matrices

    Parameters
    ----------
    mat1: Smatrix
    mat2: Smatrix

    Returns
    -------
    out : Smatrix
        Pointwise addition of two symmetric matrices
    """
    if mat1.shape == mat2.shape:
        # Zip the rows, and zip the elements
        data = [[elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
                                for row1, row2 in zip(mat1.data, mat2.data)]
        return Smatrix(mat1.shape, data)
    else:
        raise ValueError('Shape mismatch', 'Cannot add symmetric matrices of different size.')
