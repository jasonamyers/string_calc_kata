import nose
from nose.tools import assert_equals, raises

from kata import string_calculator

class TestStringCalc:

    def test_empty_string(self):
        assert_equals(0, string_calculator.add(''))

    def test_one_number(self):
        assert_equals(1, string_calculator.add('1'))

    def test_two_numbers(self):
        assert_equals(3, string_calculator.add('1,2'))

    def test_three_numbers(self):
        assert_equals(6, string_calculator.add('1,2,3'))

    def test_four_numbers(self):
        assert_equals(10, string_calculator.add('1,2,3,4'))

    def test_four_numbers_with_newline(self):
        assert_equals(10, string_calculator.add('1\n,2,3,4'))

    def test_four_numbers_with_delimiter_change(self):
        assert_equals(10, string_calculator.add('//;\n1;2;3;4'))

    @raises(ValueError)
    def test_one_negative_number(self):
        string_calculator.add('-1')

    @raises(ValueError)
    def test_two_numbers_with_negative(self):
        string_calculator.add('-1,2')

    @raises(ValueError)
    def test_three_numbers_with_negative(self):
        string_calculator.add('1,2,-3')

    @raises(ValueError)
    def test_four_numbers_with_negative(self):
        string_calculator.add('1,-2,3,4')

    @raises(ValueError)
    def test_four_numbers_with_negative_and_delimiter_change(self):
        string_calculator.add('//;\n1,-2,3,4')

    def test_numbers_over_1000_are_ignored(self):
        assert_equals(10, string_calculator.add('1,2,3,4,10001,100002'))

    def test_numbers_upto_1000_are_allowed(self):
        assert_equals(1010, string_calculator.add('1,2,3,4,1000,100002'))

    def test_four_numbers_with_two_character_delimiter_change(self):
        assert_equals(10, string_calculator.add('//;;\n1;;2;;3;;4'))

    def test_four_numbers_with_three_character_delimiter_change(self):
        assert_equals(10, string_calculator.add('//***\n1***2***3***4'))

    @raises(ValueError)
    def test_four_numbers_with_three_character_delimiter_change_and_negative(self):
        string_calculator.add('//***\n1***2***-3***4')

    def test_three_numbers_with_multiple_delimiters(self):
        assert_equals(6, string_calculator.add('//[*][@]\n1*2@3'))

    def test_four_numbers_with_three_character_multiple_delimiter_change(self):
        assert_equals(10, string_calculator.add('//[***][---]\n1***2***3***4'))

    @raises(ValueError)
    def test_four_numbers_with_three_character_mutiple_delimiter_change_and_negative(self):
        string_calculator.add('//[***][---]\n1***2***-3***4')
