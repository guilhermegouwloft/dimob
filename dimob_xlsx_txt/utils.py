class FieldCleaner:

    def cnpj_cpf(value):
        cleaned_value = str(int(value))
        if len(cleaned_value) <= 11:
            prefix = (11 - len(cleaned_value)) * "0"
            cleaned_value = prefix + cleaned_value
            posfix = (14 - len(cleaned_value)) * " "
            cleaned_value += posfix
        if len(cleaned_value) > 11 and len(cleaned_value) < 14:
            prefix = (14 - len(cleaned_value)) * "0"
            cleaned_value = prefix + cleaned_value
        return cleaned_value

    def year(value):
        return str(int(value))

    def sale_seq(value):
        cleaned_value = str(int(value))
        if len(cleaned_value) <= 5:
            prefix = (5 - len(cleaned_value)) * "0"
            cleaned_value = prefix + cleaned_value
        return cleaned_value

    def name(value):
        cleaned_value = str(value)
        if len(cleaned_value) <= 60:
            posfix = (60 - len(cleaned_value)) * " "
            cleaned_value += posfix
        return cleaned_value

    def contract_code(value):
        cleaned_value = str(int(value))
        if len(cleaned_value) <= 6:
            posfix = (6 - len(cleaned_value)) * " "
            cleaned_value += posfix
        return cleaned_value

    def contract_date(value):
        cleaned_value = str(int(value))
        if len(cleaned_value) <= 8:
            prefix = (8 - len(cleaned_value)) * "0"
            cleaned_value = prefix + cleaned_value
        return cleaned_value

    def money_values(value):
        cleaned_value = str(value)
        cents = cleaned_value.split(".")
        cleaned_value = cleaned_value.replace(".", "")

        if len(cleaned_value) <= 14 and len(cents[-1]) == 2:
            prefix = (14 - len(cleaned_value)) * "0"
            cleaned_value = prefix + cleaned_value

        elif len(cleaned_value) <= 14 and len(cents[-1]) == 1:
            prefix = (13 - len(cleaned_value)) * "0"
            cleaned_value += "0"
            cleaned_value = prefix + cleaned_value
        return cleaned_value

    def real_estate_address(value):
        cleaned_value = str(value)
        if len(cleaned_value) <= 60:
            posfix = (60 - len(cleaned_value)) * " "
            cleaned_value += posfix
        return cleaned_value

    def cep(value):
        return str(int(value))

    def city_code(value):
        return str(int(value))

    def reserved(spaces):
        return " " * spaces

    def rectifying_statement(value):
        if value:
            return "1"
        else:
            return "0"

    def receipt_number(value):
        if not value:
            value = " " * 10
        return str(value)
