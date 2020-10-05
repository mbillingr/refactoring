from statement import statement

PLAYS = {'hamlet': {'name': 'Hamlet', 'type': 'tragedy'},
         'as-like': {'name': 'As You Like It', 'type': 'comedy'},
         'othello': {'name': 'Othello', 'type': 'tragedy'}}


def test_big_co():
    invoice = {'customer': 'BigCo',
               'performances': [{'playID': 'hamlet', 'audience': 55},
                                {'playID': 'as-like', 'audience': 35},
                                {'playID': 'othello', 'audience': 40}]}
    stmt = statement(invoice, PLAYS)
    assert stmt == """Statement for BigCo
  Hamlet: $650.00 (55 seats)
  As You Like It: $580.00 (35 seats)
  Othello: $500.00 (40 seats)
Amount owed is $1,730.00
You earned 47 credits
"""


def test_empty_invoice():
    invoice = {'customer': 'NullCorp',
               'performances': []}
    stmt = statement(invoice, PLAYS)
    assert stmt == """Statement for NullCorp
Amount owed is $0.00
You earned 0 credits
"""


def test_tragedy_no_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 0}]}
    plays = {'default': {'name': 'A Tragedy', 'type': 'tragedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Tragedy: $400.00 (0 seats)
Amount owed is $400.00
You earned 0 credits
"""


def test_tragedy_small_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 30}]}
    plays = {'default': {'name': 'A Tragedy', 'type': 'tragedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Tragedy: $400.00 (30 seats)
Amount owed is $400.00
You earned 0 credits
"""


def test_tragedy_large_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 31}]}
    plays = {'default': {'name': 'A Tragedy', 'type': 'tragedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Tragedy: $410.00 (31 seats)
Amount owed is $410.00
You earned 1 credits
"""


def test_tragedy_huge_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 40}]}
    plays = {'default': {'name': 'A Tragedy', 'type': 'tragedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Tragedy: $500.00 (40 seats)
Amount owed is $500.00
You earned 10 credits
"""


def test_comedy_no_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 0}]}
    plays = {'default': {'name': 'A Comedy', 'type': 'comedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Comedy: $300.00 (0 seats)
Amount owed is $300.00
You earned 0 credits
"""


def test_comedy_small_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 20}]}
    plays = {'default': {'name': 'A Comedy', 'type': 'comedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Comedy: $360.00 (20 seats)
Amount owed is $360.00
You earned 4 credits
"""


def test_comedy_large_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 21}]}
    plays = {'default': {'name': 'A Comedy', 'type': 'comedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Comedy: $468.00 (21 seats)
Amount owed is $468.00
You earned 4 credits
"""


def test_comedy_huge_audience():
    invoice = {'customer': 'Foo',
               'performances': [{'playID': 'default', 'audience': 40}]}
    plays = {'default': {'name': 'A Comedy', 'type': 'comedy'}}
    stmt = statement(invoice, plays)
    assert stmt == """Statement for Foo
  A Comedy: $620.00 (40 seats)
Amount owed is $620.00
You earned 18 credits
"""
