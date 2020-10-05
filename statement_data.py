
def create_statement_data(invoice, plays):
    def enrich_performance(a_performance):
        calculator = create_performance_calculator(a_performance,
                                                   play_for(a_performance))

        result = dict(**a_performance)
        result['play'] = calculator.play
        result['amount'] = calculator.amount
        result['volume_credits'] = calculator.volume_credits
        return result

    def play_for(a_performance):
        return plays[a_performance['playID']]

    def total_volume_credits(data):
        return sum(map(lambda perf: perf['volume_credits'],
                       data['performances']))

    def total_amount(data):
        return sum(map(lambda perf: perf['amount'],
                       data['performances']))

    result = {}
    result['customer'] = invoice['customer']
    result['performances'] = list(map(enrich_performance,
                                              invoice['performances']))
    result['total_amount'] = total_amount(result)
    result['total_volume_credits'] = total_volume_credits(result)
    return result


def create_performance_calculator(a_performance, a_play):
    if a_play['type'] == 'tragedy':
        return TragedyCalculator(a_performance, a_play)
    elif a_play['type'] == 'comedy':
        return ComedyCalculator(a_performance, a_play)
    else:
        raise ValueError(f"unknown type: {a_play['type']}")


class PerformanceCalculator:
    def __init__(self, a_performance, a_play):
        self.performance = a_performance
        self.play = a_play

    @property
    def amount(self):
        raise NotImplementedError('subclass responsibility')

    @property
    def volume_credits(self):
        result = 0
        result += max(self.performance['audience'] - 30, 0)
        if "comedy" == self.play['type']:
            result += self.performance['audience'] // 5
        return result


class TragedyCalculator(PerformanceCalculator):
    @property
    def amount(self):
        result = 40000
        if self.performance['audience'] > 30:
            result += 1000 * (self.performance['audience'] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    @property
    def amount(self):
        result = 30000
        if self.performance['audience'] > 20:
            result += 10000 + 500 * (self.performance['audience'] - 20)
        result += 300 * self.performance['audience']
        return result
