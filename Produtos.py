from SqlHandler import SqlHandler


class Produtos:
    def __init__(self, connector: SqlHandler) -> None:
        self.connector = connector

    @staticmethod
    def prepare_join(join: bool | list):
        joins = ''
        if not join:
            return joins

        for item in join:
            joins += f"JOIN {item['table']} ON products.{item['foreing_key']} = {item['table']}.{item['primary_key']}"

        return joins

    def get_by_id(self, id, join: bool | list=False):
        join_query = self.prepare_join(join=join)

        where_query = f"""
            select
                *
            from 
                products
            {join_query}
            where 
                products.id = '{id}'
        """
        response = self.connector.exec_query(where_query)

        if not response:
            return False

        return response[0]

    def get_all(self, join: bool | list=False):
        join_query = self.prepare_join(join=join)

        where_query = f"""
            select
                *
            from 
                products
            {join_query}
        """
        response = self.connector.exec_query(where_query)

        if not response:
            return False

        return response

    def get_all_by_category(self, category, join: bool | list=False, select_join: str = '*'):
        join_query = self.prepare_join(join=join)

        where_query = f"""
            select
                {select_join}
            from 
                products
            {join_query}
            where
                products.category_id = {category}
        """
        response = self.connector.exec_query(where_query)

        if not response:
            return False

        return response
