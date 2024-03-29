from openpyxl import load_workbook

from utils import FieldCleaner as clean


workbook = load_workbook(filename="files/DIMOB-CEP-TESTE.xlsx")
sheet = workbook["Planilha1"]

with open("reports/foxter_output_2.txt", "a") as file:
    for i in range(2, 4):
        current_row = sheet[i]

        fields = {
            "tipo": current_row[0].value,
            "cnpj_declarante": clean.cnpj_cpf(current_row[1].value),
            "ano_calendario": clean.year(current_row[2].value),
            "seq_venda": clean.sale_seq(current_row[3].value),
            "cnpj_comprador": clean.cnpj_cpf(current_row[4].value),
            "nome_comprador": clean.name(current_row[5].value),
            "cnpj_vendedor": clean.cnpj_cpf(current_row[6].value),
            "nome_vendedor": clean.name(current_row[7].value),
            "numero_contrato": clean.contract_code(current_row[8].value),
            "data_contrato": clean.contract_date(current_row[9].value),
            "valor_venda": clean.money_values(current_row[10].value),
            "valor_comissao": clean.money_values(current_row[11].value),
            "tipo_imovel": current_row[12].value,
            "endereco_imovel": clean.real_estate_address(current_row[13].value),
            "cep": clean.cep(current_row[14].value),
            "codigo_municipio": clean.city_code(current_row[15].value),
            "reservado_1": clean.reserved(20),
            "uf": current_row[16].value,
            "reservado_2": clean.reserved(10),
        }

        file.write(fields["tipo"])
        file.write(fields["cnpj_declarante"])
        file.write(fields["ano_calendario"])
        file.write(fields["seq_venda"])
        file.write(fields["cnpj_comprador"])
        file.write(fields["nome_comprador"])
        file.write(fields["cnpj_vendedor"])
        file.write(fields["nome_vendedor"])
        file.write(fields["numero_contrato"])
        file.write(fields["data_contrato"])
        file.write(fields["valor_venda"])
        file.write(fields["valor_comissao"])
        file.write(fields["tipo_imovel"])
        file.write(fields["endereco_imovel"])
        file.write(fields["cep"])
        file.write(fields["codigo_municipio"])
        file.write(fields["reservado_1"])
        file.write(fields["uf"])
        file.write(fields["reservado_2"])
        file.write("\n")
    file.write("T9" + clean.reserved(100))
