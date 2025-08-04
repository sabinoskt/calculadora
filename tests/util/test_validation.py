
from faker import Faker

from src.util.operacao import adicao, subtracao, multiplicacao, divisao

fake = Faker()


def test_adicao():
    num1, num2 = fake.random_number(), fake.random_number()
    expected_value = num1 + num2
    test_adicao_function = adicao(num1, num2)
    assert expected_value.__eq__(test_adicao_function)


def test_subtracao():
    num1, num2 = fake.random_number(), fake.random_number()
    expected_value = num1 - num2
    test_subtracao_function = subtracao(num1, num2)
    assert expected_value.__eq__(test_subtracao_function)


def test_multiplicacao():
    num1, num2 = fake.random_number(), fake.random_number()
    expected_value = num1 * num2
    test_multiplicacao_function = multiplicacao(num1, num2)
    assert expected_value.__eq__(test_multiplicacao_function)


def test_divisao():
    num1, num2 = fake.random_number(), fake.random_number()
    expected_value = num1 / num2
    test_divisao_function = divisao(num1, num2)
    assert expected_value.__eq__(test_divisao_function)
