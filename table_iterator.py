class TableIterator:
    def __init__(self):
        pass

    @staticmethod
    def _check_table(table):
        if not isinstance(table, list):
            raise TypeError('table has to be list')
        if (not table) or (not table[0]):
            raise ValueError('table has to be not empty')
        if not isinstance(table[0], list):
            raise TypeError('table\'s row has to be list')
        row_cels = len(table[0])
        for row in table:
            if len(row) is not row_cels:
                raise ValueError('all table row has to be the same length')

    @staticmethod
    def _get_table_dims(table):
        TableIterator._check_table(table=table)
        rows_num = len(table)
        row_cels = len(table[0])
        return rows_num, row_cels

    @staticmethod
    def _get_indexes_column(rows_num, row_cels):
        for column_index in xrange(row_cels):
            if column_index % 2 is 0:
                for row_index in xrange(rows_num):
                    yield {
                        'row': row_index,
                        'column': column_index
                    }
            else:
                for row_index in reversed(xrange(rows_num)):
                    yield {
                        'row': row_index,
                        'column': column_index
                    }

    @staticmethod
    def _get_indexes_diagonal(rows_num, row_cels):
        cur_row = -1
        cur_column = 1
        cells = 0
        for line_num in xrange(rows_num + row_cels - 1):
            if line_num % 2 == 0:
                row_iter = 1
                column_iter = -1
            else:
                row_iter = -1
                column_iter = 1
            while cells < rows_num*row_cels:
                row_pass = rows_num > cur_row + row_iter >= 0
                cell_pass = row_cels > cur_column + column_iter >= 0
                if row_pass and cell_pass:
                    cur_row += row_iter
                    cur_column += column_iter
                elif not row_pass:
                    cur_column += 1
                elif not cell_pass:
                    cur_row += 1
                yield {
                        'row': cur_row,
                        'column': cur_column
                    }
                cells += 1
                if not row_pass or not cell_pass:
                    break

    @staticmethod
    def get_items_column(table):
        rows_num, row_cels = TableIterator._get_table_dims(table=table)
        indexes = TableIterator._get_indexes_column(rows_num=rows_num, row_cels=row_cels)
        for index in indexes:
            yield table[index['row']][index['column']]

    @staticmethod
    def get_items_diagonal(table):
        rows_num, row_cels = TableIterator._get_table_dims(table=table)
        indexes = TableIterator._get_indexes_diagonal(rows_num=rows_num, row_cels=row_cels)
        for index in indexes:
            yield table[index['row']][index['column']]




