#include <iostream>
#include <vector>
using namespace std;

using Matrix = vector<vector<int>>; // Alias for 2D vector of integers

// Function to multiply two matrices
Matrix multiplyMatrices(const Matrix &matrixA, const Matrix &matrixB)
{
    // Check if the matrices have valid dimensions for multiplication
    if (matrixA.empty() || matrixB.empty() || matrixA[0].size() != matrixB.size())
    {
        throw invalid_argument("Matrix dimensions are not suitable for multiplication.");
    }

    // Infer the dimensions of the matrices
    size_t m = matrixA.size(), n = matrixB.size(), p = matrixB[0].size();

    Matrix resultMatrix(m, vector<int>(p, 0)); // Initialize the resultant matrix with 0s

    // Multiply the matrices
    for (size_t i = 0; i < m; ++i)
    {
        for (size_t j = 0; j < p; ++j)
        {
            for (size_t k = 0; k < n; ++k)
            {
                resultMatrix[i][j] += matrixA[i][k] * matrixB[k][j];
            }
        }
    }
    return resultMatrix;
}

// Function to print a matrix
void printMatrix(const Matrix &matrix)
{
    for (const auto &row : matrix)
    {
        for (const auto &element : row)
        {
            cout << element << " ";
        }
        cout << endl;
    }
}

// Function to input a matrix
Matrix inputMatrix(size_t rows, size_t cols)
{
    Matrix matrix(rows, vector<int>(cols));
    for (size_t i = 0; i < rows; ++i)
    {
        for (size_t j = 0; j < cols; ++j)
        {
            cin >> matrix[i][j];
        }
    }
    return matrix;
}

int main()
{
    size_t rowsA, colsA, rowsB, colsB;
    // cout << "Enter rows and columns for Matrix A:";  // Uncomment this line for more interactive input
    cin >> rowsA >> colsA;
    // cout << "Enter Matrix A:\n";  // Uncomment this line for more interactive input
    Matrix matrixA = inputMatrix(rowsA, colsA);

    // cout << "Enter rows and columns for Matrix B:";  // Uncomment this line for more interactive input
    cin >> rowsB >> colsB;
    if (colsA != rowsB)
    {
        cerr << "Error: Matrix A columns must equal Matrix B rows for multiplication." << endl;
        return 1;
    }
    // cout << "Enter Matrix B:\n";  // Uncomment this line for more interactive input
    Matrix matrixB = inputMatrix(rowsB, colsB);

    try
    {
        Matrix resultMatrix = multiplyMatrices(matrixA, matrixB);
        // cout << "Resultant Matrix C (A x B):\n";  // Uncomment this line for more interactive output
        printMatrix(resultMatrix);
    }
    catch (const invalid_argument &e)
    {
        cerr << "Matrix multiplication error: " << e.what() << endl;
    }

    return 0;
}
