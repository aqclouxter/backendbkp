import connect



class Table:

    def __init__(self, table_name):
        self.cursor = connect.mydb.cursor()
        self.table = self.__create_table(table_name)

    def __create_table(self, table_name):
        self.cursor.execute("CREATE TABLE " + table_name + "(task_id int not null auto_increment primary key, task VARCHAR(255), INDEX (task_id))")
        return table_name

    def table_name(self):
        return self.table

    @staticmethod
    def delete(id):
        cursor = connect.mydb.cursor()
        tables = Table.show_tables()
        tables = tables['tables']
        cursor.execute("DROP TABLE " + tables[int(id)][0])


    @staticmethod
    def add_columns(table_name, *args):
        cursor = connect.mydb.cursor()
        for col in args:
            cursor.execute("ALTER TABLE "+ table_name +" ADD COLUMN "+ col +" VARCHAR(255)")

    @staticmethod
    def delete_columns(table_name, *args):
        cursor = connect.mydb.cursor()
        for col in args:
            cursor.execute("ALTER TABLE "+ table_name +" DROP COLUMN "+ col)

    @staticmethod
    def add_foreign_key(parent_table, child_table):
        cursor = connect.mydb.cursor()
        cursor.execute("ALTER TABLE " + child_table + " ADD COLUMN category_id int")
        cursor.execute("alter table " + child_table + " add constraint fk_" + child_table + " foreign key (category_id) references " + parent_table + " (task_id) ON DELETE CASCADE ON UPDATE CASCADE")

    @staticmethod
    def show_tables():
        cursor = connect.mydb.cursor()
        cursor.execute("SHOW TABLES")
        return {'tables':cursor.fetchall()}

    @staticmethod
    def abort_if_table_does_not_exists(table_name):
        tables = Table.show_tables()
        for tab in tables['tables']:
            if tab[0] == table_name:
                return True
            else:
                return False

    @staticmethod
    def get_categories(id):
        cursor = connect.mydb.cursor()
        cursor.execute("SELECT task from firstTable")
        return {'categories': cursor.fetchall()}

    @staticmethod
    def post_category(category):
        cursor = connect.mydb.cursor()
        cursor.execute("INSERT INTO firstTable (task) values ('" + category + "')")
        connect.mydb.commit()
        return {'category': category}

    @staticmethod
    def update_category(id, category):
        cursor = connect.mydb.cursor()
        cursor.execute("UPDATE firstTable SET task='" + category + "' WHERE task_id=" + id)
        connect.mydb.commit()
        return {'category_id': id, 'category': category}

    @staticmethod
    def delete_category(id):
        cursor = connect.mydb.cursor()
        cursor.execute("DELETE FROM firstTable WHERE task_id=" +id)
        connect.mydb.commit()
        return ''

    @staticmethod
    def get_tasks(id):
        cursor = connect.mydb.cursor()
        cursor.execute("SELECT task from secondTable WHERE category_id=" + id)
        return {'tasks': cursor.fetchall()}

    @staticmethod
    def post_task(id, task):
        cursor = connect.mydb.cursor()
        cursor.execute("insert into secondTable (task, category_id) values ('" + task + "', " + id + ")")
        connect.mydb.commit()

        return {'category_id': id, 'task': task}

    @staticmethod
    def get_task(id, tid):
        cursor = connect.mydb.cursor()
        cursor.execute("SELECT task from secondTable WHERE task_id=" + tid + " AND category_id =" + id)
        return {'task': cursor.fetchone()}

    @staticmethod
    def update_task(id, tid, task):
        cursor = connect.mydb.cursor()
        cursor.execute("UPDATE secondTable SET task='" + task + "' WHERE task_id=" + tid + " AND category_id="+ id)
        connect.mydb.commit()
        return {'category_id': id, 'task_id': tid, 'task': task}

    @staticmethod
    def delete_task(id, tid):
        cursor = connect.mydb.cursor()
        cursor.execute("DELETE from secondTable WHERE task_id=" + tid + " AND category_id =" + id)
        connect.mydb.commit()
        return ''

























