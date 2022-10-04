import numpy as np
# @pytest.fixture
# def sequences():
#    return ["agctctt", "tggtgta", "gcttagt", "aaaagtctgt"]


def add_scalar(vector, number):
    """Add a scalar to a vector

    Parameters
    ----------
    vector : np.ndarray
        shape=(n,)
    number : Number
        scalar

    Examples
    --------
    >>> a = np.array([1, 2, 3])
    >>> add_scalar(a, 5)
    np.array([6, 7, 8])
    """
    return [n+number for n in vector]


def add_vectors(vector_a, vector_b):
    """Add two vectors

    Parameters
    ----------
    vector_a : np.ndarray
        shape=(n, )
    vector_b : np.ndarray
        shape=(n, )

    Examples
    --------
    >>> a = np.array([1, 2, 3])
    >>> b = np.array([10, 20, 20])
    >>> add_vectors(a, b)
    [11, 22, 23]
    """
    return [a+b for a, b in zip(vector_a, vector_b)]


def add_matrices(matrix_a, matrix_b):
    """Add two matrices

    Parameters
    ----------
    matrix_a : np.ndarray
        shape=(n, m)
    matrix_b : np.ndarray
        shape=(n, m)

    Examples
    --------
    >>> a = np.array([[1, 2, 3],
                      [4, 5, 6]])
    >>> b = np.array([[10, 20, 20],
                      [20, 10, 10]])
    >>> add_matrices(a, b)
    [[11, 22, 23],
     [24, 15, 16]]
    """
    return [add_vectors(vector_a, vector_b)
            for vector_a, vector_b in zip(matrix_a, matrix_b)]


def add_row_vector_to_matrix(matrix, vector):
    """Add a vector to each row of the matrix

    Parameters
    ----------
    matrix : np.ndarray
        shape=(n, m)
    vector : np.ndarray
        shape=(m, )

    Examples
    --------
    >>> a = np.array([[1, 2, 3],
                      [4, 5, 6]])
    >>> b = np.array([10, 20, 20])
    >>> add_row_vector_to_matrix(a, b)
    [[11, 22, 23],
     [14, 25, 26]]
    """

    return [add_vectors(vector, row) for
            row in matrix]


def add_column_vector_to_matrix(matrix, column):
    """Add a vector to each column of the matrix

    Parameters
    ----------
    matrix : np.ndarray
        shape=(n, m)
    vector : np.ndarray
        shape=(n, )

    Examples
    --------
    >>> a = np.array([[1, 2, 3],
                      [4, 5, 6]])
    >>> b = np.array([10, 20])
    >>> add_row_vector_to_matrix(a, b)
    [[11, 12, 13],
     [24, 25, 26]]
    """
    return [add_scalar(row, number) for
            row, number in zip(matrix, column)]


def filter(vector: np.ndarray) -> np.ndarray:
    """Filter elements lower than 3

    Parameters
    ----------
    vector : np.ndarray
        shape = (n,)

    Returns
    -------
    np.ndarray
        shape=(<=n, )

    Examples
    --------
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> filter(a)
    [4, 5, 6]
    """
    return [v for v in vector if v > 3]


def if_else(vector: np.ndarray) -> np.ndarray:
    """Copies vector but sets elements lower than 3 to 0

    Parameters
    ----------
    vector : np.ndarray
        shape = (n, )

    Returns
    -------
    np.ndarray
        shape = (n, )

    Examples
    --------
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> if_else(a)
    [0, 0, 0, 4, 5, 6]
    """
    return [v if v > 3 else 0 for v in vector]


def select_many(vector: np.ndarray, indices: list) -> np.ndarray:
    """Select elements from indices

    Parameters
    ----------
    vector : np.ndarray
        shape = (n, )
    indices : list
        shape= (m, )

    Returns
    -------
    np.ndarray
        shape= (m, )

    Examples
    --------
    >>> a = np.array([1, 2, 3, 4, 5, 6])
    >>> select_many(a, [0, 3, 4])
    [1, 4, 5]
    """
    return [vector[i] for i in indices]
