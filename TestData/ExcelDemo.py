import pandas as pd


def getExcelData():
    book = pd.read_excel("C:\\Users\\vigne\\PycharmProjects\\pythonProject2\\TestData\\PythonDemo.xlsx", index_col=0)
    keys = list(book.to_dict().keys())
    row = book.shape[0]
    lst = []
    result = []
    for i in range(row):
        lst.append([])
        tmp = book.iloc[i]
        for j in tmp:
            if type(j) is None:
                pass
            else:
                lst[i].append(j)
    for i in range(row):
        result.append(dict(zip(keys, lst[i])))
    return result


print(getExcelData())
