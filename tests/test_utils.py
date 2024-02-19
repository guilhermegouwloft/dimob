from dimob_xlsx_txt.utils import FieldCleaner as clean
from dimob_xlsx_txt.utils import get_header


def test_cnpj_cpf_with_less_than_11_chars():
    assert clean.cnpj_cpf(123456789) == "00123456789   "


def test_cnpj_cpf_with_11_chars():
    assert clean.cnpj_cpf(12345678901) == "12345678901   "


def test_cnpj_cpf_with_14_chars():
    assert clean.cnpj_cpf(12345678901234) == "12345678901234"


def test_sale_seq_with_less_than_5_chars():
    assert clean.sale_seq(123) == "00123"


def test_sale_seq_with_5_chars():
    assert clean.sale_seq(12345) == "12345"


def test_name_with_less_than_60_chars():
    str_input = " essa string possui quarenta caracteres "
    str_output = " essa string possui quarenta caracteres                     "
    assert clean.name(str_input) == str_output


def test_name_with_60_chars():
    str_input = "           essa string possui sessenta caracteres           "
    str_output = "           essa string possui sessenta caracteres           "
    assert clean.name(str_input) == str_output


def test_contract_code_with_less_than_6_chars():
    assert clean.contract_code(1234) == "1234  "


def test_contract_code_with_6_chars():
    assert clean.contract_code(123456) == "123456"


def test_money_values_with_less_than_14_chars():
    assert clean.money_values(12345678.90) == "00001234567890"


def test_money_values_with_14_chars():
    assert clean.money_values(12345678901234) == "12345678901234"


def test_real_estate_address_with_less_than_60_chars():
    str_input = " essa string possui quarenta caracteres "
    str_output = " essa string possui quarenta caracteres                     "
    assert clean.real_estate_address(str_input) == str_output


def test_real_estate_address_with_60_chars():
    str_input = "           essa string possui sessenta caracteres           "
    str_output = "           essa string possui sessenta caracteres           "
    assert clean.real_estate_address(str_input) == str_output


def test_get_header():
    output = "DIMOB" + (" " * 369)
    assert get_header() == output


def test_rectifying_statement_no_value():
    assert clean.rectifying_statement("") == "0"


def test_rectifying_statement_with_value():
    assert clean.rectifying_statement("S") == "1"


def test_receipt_number_no_value():
    output = "          "
    assert clean.receipt_number("") == output


def test_receipt_number_with_value():
    output = "1234567890"
    assert clean.receipt_number(1234567890) == output
