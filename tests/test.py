import pandas as pd


def getTestData(test_case_name):
    book = pd.read_excel("C:\\Users\\vigne\\PycharmProjects\\pythonProject2\\TestData\\PythonDemo.xlsx", index_col=0)
    tmp = book.loc[test_case_name]
    keys = list(tmp.to_dict().keys())
    lst = []
    for i in tmp:
        lst.append(i)
    Dict = (dict(zip(keys, lst)))
    return [Dict]

print(getTestData("TestCase1"))
