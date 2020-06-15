import pandas
#enter two excel file names in below two lines orelse path
df1 = pandas.read_excel('Book1.xlsx')
df2 = pandas.read_excel('Book2.xlsx')
#write the requred equivalent fields name in place of Roll No. (Contact me at adithya.kasula@gmail.com if it doesnt work.)
final_file = pandas.merge(df1, df2, left_on='Roll no.', right_on='Roll no.')
final_file.to_excel('file3.xlsx', index=False)
