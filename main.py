# from fql.FqlDb import FqlDb
import fql
from fql import types
from fql import modifiers as m

def main():
    print("hello")
    db = fql.open("mydb.db")

    # get all table names in the db
    print(db.tables.table_name.select())

    db.create_table("users", ('id', 'name', 'age'), (types.Int4, types.String, types.Int2))

    # or
    db.create_table("users", [('id', types.Int4, m.PrimaryKey, m.NotNull), ('name', types.String, m.NotNull), ('age',types.Int2)])

    u = db.table("users")
    u.id.modify(m.AutoIncrement)
    db.table("users").insert(columns=('id', 'name', 'age'), values=[[24, 'Иван', 20], [2, 'Виктор', 19], [3, 'Алла', 28]])

    # get columns
    print(u.columns)

    # select all
    result = u.select()
    print(result)

    result = u.where(u.age>=20 and u.name.startswith("A")).select(u.name, u.age)
    print(result)

    result = u.limit(2).where(u.name.len() == 4).shift(1).select(u.id)
    print(result)

    result = u.sort_by(u.name, reverse=True).select(u.name)
    print(result)

    u.where(u.id == 2).delete()

    u.save()

if __name__ == '__main__':

    main()

