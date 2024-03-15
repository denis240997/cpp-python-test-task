import pytest
from wrapper import multiply_matrices


@pytest.fixture
def zero_matrix():
    return [[0, 0], [0, 0]]


@pytest.fixture
def identity_matrix():
    return [[1, 0], [0, 1]]


@pytest.fixture(params=[-(2**31), 2**31 - 1])
def int32_boundary(request):
    return request.param


@pytest.fixture(params=[-(2**31 + 1), 2**31])
def int32_overflow(request):
    return request.param


@pytest.fixture(params=[1.0, 1 + 1j, "string"])
def element_of_invalid_type(request):
    return request.param


def test_basic_functionality():
    matrix_a = [[1, 2], [3, 4]]
    matrix_b = [[2, 0], [1, 2]]
    expected = [[4, 4], [10, 8]]
    assert multiply_matrices(matrix_a, matrix_b) == expected


def test_non_square_matrices():
    matrix_a = [[1, 2, 3]]
    matrix_b = [[1], [2], [3]]
    expected = [[14]]
    assert multiply_matrices(matrix_a, matrix_b) == expected


def test_dimension_mismatch():
    matrix_a = [[1, 2, 3], [4, 5, 6]]
    matrix_b = [[1, 2], [3, 4]]
    with pytest.raises(ValueError):
        multiply_matrices(matrix_a, matrix_b)


@pytest.mark.parametrize(
    "matrix_a, matrix_b",
    [
        ([[]], [[]]),
        ([[]], [[1, 2], [3, 4]]),
        ([[1, 2], [3, 4]], [[]]),
    ],
)
def test_empty_matrices(matrix_a, matrix_b):
    with pytest.raises(ValueError):
        multiply_matrices(matrix_a, matrix_b)


def test_single_element_matrices():
    assert multiply_matrices([[2]], [[3]]) == [[6]]


def test_identity_matrix(identity_matrix):
    matrix_a = [[1, 2], [3, 4]]
    assert multiply_matrices(matrix_a, identity_matrix) == matrix_a


def test_zero_matrix(zero_matrix):
    matrix_a = [[1, 2], [3, 4]]
    assert multiply_matrices(matrix_a, zero_matrix) == zero_matrix


def test_negative_numbers():
    matrix_a = [[-1, -2], [-3, -4]]
    matrix_b = [[2, 0], [1, 2]]
    expected = [[-4, -4], [-10, -8]]
    assert multiply_matrices(matrix_a, matrix_b) == expected


def test_int32_boundary(int32_boundary, identity_matrix):
    matrix_a = [[int32_boundary, int32_boundary], [int32_boundary, int32_boundary]]
    assert multiply_matrices(matrix_a, identity_matrix) == matrix_a


def test_int32_overflow(int32_overflow, identity_matrix):
    matrix_a = [[int32_overflow, int32_overflow], [int32_overflow, int32_overflow]]
    with pytest.raises(ValueError):
        multiply_matrices(matrix_a, identity_matrix)


def test_boolean_input():
    matrix_a = [[True, False], [False, True]]
    matrix_b = [[False, True], [True, False]]
    expected = [[False, True], [True, False]]
    assert multiply_matrices(matrix_a, matrix_b) == expected


def test_invalid_input_type(element_of_invalid_type, zero_matrix):
    matrix_a = [
        [element_of_invalid_type, element_of_invalid_type],
        [element_of_invalid_type, element_of_invalid_type],
    ]
    with pytest.raises(TypeError):
        multiply_matrices(matrix_a, zero_matrix)


# TODO: test_invalid_matrix_shape
