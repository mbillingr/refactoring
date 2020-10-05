class PerformanceCalculator:
    def __init__(self, a_performance):
        self.performance = a_performance


def create_statement_data(invoice, plays):
    def enrich_performance(a_performance):
        calculator = PerformanceCalculator(a_performance)

        result = dict(**a_performance)
        result['play'] = play_for(result)
        result['amount'] = amount_for(result)
        result['volume_credits'] = volume_credits_for(result)
        return result

    def play_for(a_performance):
        return plays[a_performance['playID']]

    def amount_for(a_performance):
        result = 0
        if a_performance['play']['type'] == "tragedy":
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance['audience'] - 30)
        elif a_performance['play']['type'] == "comedy":
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance['audience'] - 20)
            result += 300 * a_performance['audience']
        else:
            raise ValueError(f"unknown type: {a_performance['play']['type']}")
        return result

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance['audience'] - 30, 0)
        if "comedy" == a_performance['play']['type']:
            result += a_performance['audience'] // 5
        return result

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
