#!/usr/bin/env python

"""Tests for `iteretor_tutorial` package."""

import pytest
import numpy as np

from iteretor_tutorial.numpy_tutorial import (
    add_scalar,
    add_vectors,
    add_matrices,
    add_row_vector_to_matrix,
    add_column_vector_to_matrix,
    filter,
    if_else
)


@pytest.fixture
def numbers():
    return np.array([10, 20, 40, 30, 12])


@pytest.fixture
def numbers_2():
    return np.array([2, 3, 4, 5, 6])


@pytest.fixture
def matrix():
    return np.array(
        [[2, 3, 4, 5, 6],
         [10, 12, 13, 10, 20]])


@pytest.fixture
def matrix_2():
    return np.array(
        [[1, 2, 3, 4, 5],
         [10, 11, 13, 2, 19]])


def test_scalar(numbers):
    np.testing.assert_equal(
        add_scalar(numbers, 5),
        [n+5 for n in numbers])


def test_vectors(numbers, numbers_2):
    np.testing.assert_equal(
        add_vectors(numbers, numbers_2),
        numbers+numbers_2)


def test_matrix(matrix, matrix_2):
    np.testing.assert_equal(
        add_matrices(matrix, matrix_2),
        matrix+matrix_2)


def test_matrix_plus_row(matrix, numbers):
    np.testing.assert_equal(
        add_row_vector_to_matrix(matrix, numbers),
        matrix+numbers)


def test_matrix_plus_column(matrix, numbers):
    matrix = matrix.T
    np.testing.assert_equal(
        add_column_vector_to_matrix(matrix, numbers),
        matrix+numbers[..., np.newaxis])


def test_filter(numbers):
    np.testing.assert_equal(
        filter(numbers),
        [v for v in numbers if v > 3])


def test_if_else(numbers):
    np.testing.assert_equal(
        if_else(numbers),
        [v if v > 3 else 0 for v in numbers])
