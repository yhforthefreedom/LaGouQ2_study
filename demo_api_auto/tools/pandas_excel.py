import pandas as pd


class PandasExcel:
    def get_data(self, file_name, sheet_name):
        df = pd.read_excel(file_name, sheet_name)
        test_data = []
        for i in df.index.values:  # 对行号的索引进行遍历
            row_data = df.ix[i, ["case_id", "url", "data", "title", "http_method"]].to_dict()
            test_data.append(row_data)
