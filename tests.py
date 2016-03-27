from pytest import fixture

from table_iterator import TableIterator


class TestTableIterator:
    @fixture(params=[
        {
            'data': [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            'answer':[1, 4, 2, 3, 5, 7, 8, 6, 9]
         },
        {
            'data': [
                [0, 2, 3, 9, 10],
                [1, 4, 8, 11, 18],
                [5, 7, 12, 17, 19],
                [6, 13, 16, 20, 23],
                [14, 15, 21, 22, 24]
            ],
            'answer':[i for i in xrange(25)]
         },
    ])
    def case_diagonal(self, request):
        return request.param

    def test_diagonal_iterator(self, case_diagonal):
        res = TableIterator.get_items_diagonal(table=case_diagonal['data'])
        ind = 0
        for item in res:
            assert item == case_diagonal['answer'][ind]
            ind += 1

    @fixture(params=[
        {
            'data': [
                [1, 6, 7],
                [2, 5, 8],
                [3, 4, 9],
            ],
            'answer':[i for i in xrange(1, 10)]
         },
        {
            'data': [
                [0, 9, 10, 19, 20],
                [1, 8, 11, 18, 21],
                [2, 7, 12, 17, 22],
                [3, 6, 13, 16, 23],
                [4, 5, 14, 15, 24]
            ],
            'answer': [i for i in xrange(25)]
         },
    ])
    def case_column(self, request):
        return request.param

    def test_column_iterator(self, case_column):
        res = TableIterator.get_items_column(table=case_column['data'])
        ind = 0
        for item in res:
            assert item == case_column['answer'][ind]
            ind += 1

