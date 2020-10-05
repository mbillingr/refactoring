from statement_data import create_statement_data

PLAYS = {'hamlet': {'name': 'Hamlet', 'type': 'tragedy'},
         'as-like': {'name': 'As You Like It', 'type': 'comedy'},
         'othello': {'name': 'Othello', 'type': 'tragedy'}}


def test_big_co():
    invoice = {'customer': 'BigCo',
               'performances': [{'playID': 'hamlet', 'audience': 55},
                                {'playID': 'as-like', 'audience': 35},
                                {'playID': 'othello', 'audience': 40}]}
    statement_data = create_statement_data(invoice, PLAYS)
    assert statement_data == dict(customer='BigCo',
                                  total_amount=173000,
                                  total_volume_credits=47,
                                  performances=[dict(amount=65000,
                                                     audience=55,
                                                     playID='hamlet',
                                                     volume_credits=25,
                                                     play=PLAYS['hamlet']),
                                                dict(amount=58000,
                                                     audience=35,
                                                     playID='as-like',
                                                     volume_credits=12,
                                                     play=PLAYS['as-like']),
                                                dict(amount=50000,
                                                     audience=40,
                                                     playID='othello',
                                                     volume_credits=10,
                                                     play=PLAYS['othello'])])


def test_empty_invoice():
    invoice = {'customer': 'NullCorp',
               'performances': []}
    statement_data = create_statement_data(invoice, PLAYS)
    assert statement_data == dict(customer='NullCorp',
                                  total_amount=0,
                                  total_volume_credits=0,
                                  performances=[])


def test_tragedy_no_audience():
    play = {'name': 'A Tragedy', 'type': 'tragedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 0}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=40000,
                                  total_volume_credits=0,
                                  performances=[dict(amount=40000,
                                                     audience=0,
                                                     playID='default',
                                                     volume_credits=0,
                                                     play=play)])


def test_tragedy_small_audience():
    play = {'name': 'A Tragedy', 'type': 'tragedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 30}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=40000,
                                  total_volume_credits=0,
                                  performances=[dict(amount=40000,
                                                     audience=30,
                                                     playID='default',
                                                     volume_credits=0,
                                                     play=play)])


def test_tragedy_large_audience():
    play = {'name': 'A Tragedy', 'type': 'tragedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 31}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=41000,
                                  total_volume_credits=1,
                                  performances=[dict(amount=41000,
                                                     audience=31,
                                                     playID='default',
                                                     volume_credits=1,
                                                     play=play)])


def test_tragedy_huge_audience():
    play = {'name': 'A Tragedy', 'type': 'tragedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 40}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=50000,
                                  total_volume_credits=10,
                                  performances=[dict(amount=50000,
                                                     audience=40,
                                                     playID='default',
                                                     volume_credits=10,
                                                     play=play)])


def test_comedy_no_audience():
    play = {'name': 'A Comedy', 'type': 'comedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 0}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=30000,
                                  total_volume_credits=0,
                                  performances=[dict(amount=30000,
                                                     audience=0,
                                                     playID='default',
                                                     volume_credits=0,
                                                     play=play)])


def test_comedy_small_audience():
    play = {'name': 'A Comedy', 'type': 'comedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 20}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=36000,
                                  total_volume_credits=4,
                                  performances=[dict(amount=36000,
                                                     audience=20,
                                                     playID='default',
                                                     volume_credits=4,
                                                     play=play)])


def test_comedy_large_audience():
    play = {'name': 'A Comedy', 'type': 'comedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 21}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=46800,
                                  total_volume_credits=4,
                                  performances=[dict(amount=46800,
                                                     audience=21,
                                                     playID='default',
                                                     volume_credits=4,
                                                     play=play)])


def test_comedy_huge_audience():
    play = {'name': 'A Comedy', 'type': 'comedy'}
    plays = {'default': play}
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 40}]}
    statement_data = create_statement_data(invoice, plays)
    assert statement_data == dict(customer='Foo',
                                  total_amount=62000,
                                  total_volume_credits=18,
                                  performances=[dict(amount=62000,
                                                     audience=40,
                                                     playID='default',
                                                     volume_credits=18,
                                                     play=play)])