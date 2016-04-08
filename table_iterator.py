class TableIterator:
    def __init__(self):
        pass

    @staticmethod
    def _check_table(table):
        """
        operand table: 6
        operand row_cels: 2
        operand row: 2
        operand list: 2

        operands 4: 12

        functions isinstance: 2
        operator if: 4
        operator not: 5
        operator raise: 4
        operator or: 1
        operator for: 1
        operator in: 1
        operator is: 1
        operator =: 1
        operator =: 1
        function TypeError: 2
        function ValueError: 2
        function len: 2

        operators 13: 27

        predicates: 5
        """
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
        """
        operand table: 3
        operand rows_num: 2
        operand row_cels: 2

        operands 3: 7

        operator =: 3
        operator return: 1
        operator []: 1
        function len: 2
        function TableIterator._check_table: 1

        operators 5: 8

        predicates: 0
        """
        TableIterator._check_table(table=table)
        rows_num = len(table)
        row_cels = len(table[0])
        return rows_num, row_cels

    @staticmethod
    def _get_indexes_column(rows_num, row_cels):
        """
        operand rows_num: 2
        operand row_cels: 1
        operand column_index: 4
        operand row_index: 4
        operand column_index: 4

        operands 5: 15

        operator %: 1
        operator is: 1
        operator if: 1
        operator else: 1
        operator for: 3
        operator in: 3
        operator yield: 2
        operator {}: 2
        function xrange: 3
        function reversed: 1
        function TableIterator._check_table: 1

        operators 5: 8

        predicates: 4
        """
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
        """
        operand: rows_num - 3
        operand: row_cels - 3
        operand: cur_row - 5
        operand: cur_column - 5
        operand: cells - 3
        operand: row_iter - 4
        operand: column_iter - 4
        operand: row_pass - 4
        operand: cell_pass - 4

        operands: unique - 9, usage - 44


        operator: + 3
        operator: - 3
        operator: % 1
        operator: * 1
        operator: = 9
        operator: += 5
        operator: == 1
        operator: >= 2
        operator: > 2
        operator: < 1
        operator: < 1
        operator: and 1
        operator: not 4
        operator: or 1
        operator: if 3
        operator: elif 2
        operator: else 1
        operator: for 1
        operator: while 1
        operator: in 1
        operator: break 1
        operator: {} 1
        function: yield 1
        function: xrange 1

        operators: unique - 24 usage - 48

        predicates: 7
        """
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
        """
        operand: table 2
        operand: rows_num 2
        operand: row_cels 2
        operand: indexes 2
        operand: index 2

        operands: unique - 5, usage -10
        _get_indexes_column 5      15
        _get_table_dims    3         7
        _check_table        4        12
        total:       17          44



        operator: = 5
        operator: in 1
        operator: for 1
        operator: yield 1
        operator: [] 4
        function: TableIterator._get_table_dims 1
        function: TableIterator._get_indexes_column 1

        operators: unique - 7, usage - 14
        _get_indexes_column 5      8
        _get_table_dims     5      8
        _check_table        13     27
        total:       30          57

        pridicattes: 1
        _get_indexes_column 4
        _get_table_dims    0
        _check_table       5
        total:   10+1 = 11
        """
        rows_num, row_cels = TableIterator._get_table_dims(table=table)
        indexes = TableIterator._get_indexes_column(rows_num=rows_num, row_cels=row_cels)
        for index in indexes:
            yield table[index['row']][index['column']]

    @staticmethod
    def get_items_diagonal(table):
        """
        operand: table 2
        operand: rows_num 2
        operand: row_cels 2
        operand: indexes 2
        operand: index 2

        operands: unique - 5, usage -10
        _get_indexes_diagonal 9      44
        _get_table_dims    3         7
        _check_table        4        12
        total:       21          73


        operator: = 5
        operator: in 1
        operator: for 1
        operator: yield 1
        operator: [] 4
        function: TableIterator._get_table_dims 1
        function: TableIterator._get_indexes_diagonal 1

        operators: unique - 7, usage - 14
        _get_indexes_diagonal 24      48
        _get_table_dims     5      8
        _check_table        13     27
        total:       49          97

        pridicattes: 1
        _get_indexes_diagonal 7
        _get_table_dims    0
        _check_table       5
        total:       13+1 = 14

        """
        rows_num, row_cels = TableIterator._get_table_dims(table=table)
        indexes = TableIterator._get_indexes_diagonal(rows_num=rows_num, row_cels=row_cels)
        for index in indexes:
            yield table[index['row']][index['column']]




