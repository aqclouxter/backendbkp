from databaseManager.table import Table



#Table.add_foreign_key("firstTable", "secondTable")
#Table.add_foreign_key("secondTable", "thirdTable")

#Table.delete_columns("secondTable", "category_id")

first = Table('firstTable')
second = Table('secondTable')
#third = Table('thirdTable')

#Table.delete('thirdTable')
#Table.delete('secondTable')
#Table.delete('firstTable')


#third = Table('thirdTable')
#Table.insert_record('firstTable', 'infraestructura')
#Table.child_insert_record(1, 'secondTable', 'crear vpc')
#Table.child_insert_record(3, 'thirdTable', 'disenar segmentos de red')
#Table.modify_record("firstTable",'documentation', 1)

#tables = Table.show_tables()

#print(tables)