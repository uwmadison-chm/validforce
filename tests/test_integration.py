import pytest
import os
import xlrd
import csv
import warnings

from .base import *
import validforce

def run_test(mutator, data, expected):
    mutator(mutator, data, expected)

    expected_content = open(from_subdir("expected", expected)).read()
    actual_content = open(from_subdir("output", expected)).read()
    assert actual_content == expected_content


def test_basic_integration():
    run_test("001_mutator.json", "001_data.csv", "001_expected.csv")

