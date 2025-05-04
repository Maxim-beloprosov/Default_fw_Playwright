import allure
import psycopg2 as psycopg2
import pyodbc as pyodbc

from fw.fw_base import FWBase


class SQLBase(FWBase):

    @allure.step('sql_query')
    def sql_query(self, SQL_query, DATABASE):

        SQL_SERVER = self.manager.settings.GLOBAL[self.manager.settings.branch]['SQL_SERVER']

        conn = psycopg2.connect(dbname=DATABASE,
                                user=DATABASE,
                                password=SQL_SERVER['password'],
                                host=SQL_SERVER['SERVER'],
                                port=SQL_SERVER['PORT'])
        cursor = conn.cursor()
        try:
            conn.commit()
            cursor.execute(SQL_query)
            data = cursor.fetchall()
            return data
        except psycopg2.Error as err:
            print(f"Connection error: {err}")
        except pyodbc.ProgrammingError as e:
            print(f"ProgrammingError: {e}")
        finally:
            cursor.close()
            conn.close()

    @allure.step('SQL_query_INSERT')
    def sql_query_INSERT(self, SQL_query, DATABASE):

        SQL_SERVER = self.manager.settings.GLOBAL[self.manager.settings.branch]['SQL_SERVER']

        conn = psycopg2.connect(dbname=DATABASE,
                                user=DATABASE,
                                password=SQL_SERVER['password'],
                                host=SQL_SERVER['SERVER'],
                                port=SQL_SERVER['PORT'])
        cursor = conn.cursor()
        try:
            cursor.execute(SQL_query)
            conn.commit()
            data = cursor.fetchall()
            return data
        except psycopg2.Error as err:
            print(f"Connection error: {err}")
        except pyodbc.ProgrammingError as e:
            print(f"ProgrammingError: {e}")
        finally:
            cursor.close()
            conn.close()

    def sql_query_UPDATE(self, sql, DATABASE):

        SQL_SERVER = self.manager.settings.GLOBAL[self.manager.settings.branch]['SQL_SERVER']

        conn = None
        updated_rows = 0
        try:
            conn = psycopg2.connect(dbname=DATABASE,
                                    user=DATABASE,
                                    password=SQL_SERVER['password'],
                                    host=SQL_SERVER['SERVER'],
                                    port=SQL_SERVER['PORT'])

            cur = conn.cursor()
            cur.execute(sql)
            updated_rows = cur.rowcount
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
        return updated_rows