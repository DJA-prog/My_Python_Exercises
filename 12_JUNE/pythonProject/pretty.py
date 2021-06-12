from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name",["Chespin","Quilladin","Chesnaught","Fennekin"])
table.add_column("Atrib", ["Grass","Grass","Grass Fighting","Fire"])


print(table)