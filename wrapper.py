import subprocess

MIN_INT32_VALUE = -(2**31)
MAX_INT32_VALUE = 2**31 - 1


def safe_cast_to_int32_string(value: int) -> str:
    """
    Casts an integer to a string and checks if it is within the int32 range.
    """
    if not isinstance(value, int):
        raise TypeError(f"Value {value} is not an integer")
    if not MIN_INT32_VALUE <= value <= MAX_INT32_VALUE:
        raise ValueError(f"Value {value} is not within the int32 range")
    return str(
        int(value)
    )  # int for case where value is a bool, because bool is a subclass of int in Python


def multiply_matrices(
    matrix_a: list[list[int]], matrix_b: list[list[int]]
) -> list[list[int]]:
    """
    Multiplies two matrices and returns the result.
    """
    # Infer the dimensions of the matrices
    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    # Build the input string for the binary
    input_str = f"{rows_a} {cols_a}\n"
    input_str += (
        "\n".join([" ".join(map(safe_cast_to_int32_string, row)) for row in matrix_a])
        + "\n"
    )
    input_str += f"{rows_b} {cols_b}\n"
    input_str += (
        "\n".join([" ".join(map(safe_cast_to_int32_string, row)) for row in matrix_b])
        + "\n"
    )

    # Invoke the binary
    process = subprocess.Popen(
        ["./build/multiplyMatrices"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    output, errors = process.communicate(input=input_str)

    # Errors handling
    match process.returncode:
        case 0:
            pass
        case 1:  # Assuming the binary returns 1 for dimension mismatch
            raise ValueError(
                f"Inner dimensions of matrices do not match: A ({rows_a}x{cols_a}), B ({rows_b}x{cols_b})"
            )
        case _:  # Other return codes are unexpected
            raise Exception(f"Error executing multiplyMatrices: {errors}")

    # Parse the output
    # This parsing assumes the binary's output format is known and consistent.
    lines = output.splitlines()
    result_matrix = [list(map(int, line.split())) for line in lines if line.strip()]

    return result_matrix
