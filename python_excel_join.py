import pandas
df1 = pandas.read_excel('Book1.xlsx')
df2 = pandas.read_excel('Book2.xlsx')

final_file = pandas.merge(df1, df2, left_on='Roll no.', right_on='Roll no.')
final_file.to_excel('file3.xlsx', index=False)