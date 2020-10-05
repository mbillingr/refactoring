def statement(invoice, plays):
    def enrich_performance(a_performance):
        result = dict(**a_performance)
        result['play'] = play_for(result)
        return result

    def play_for(a_performance):
        return plays[a_performance['playID']]

    statement_data = {}
    statement_data['customer'] = invoice['customer']
    statement_data['performances'] = list(map(enrich_performance,
                                              invoice['performances']))
    return render_plain_text(statement_data, plays)


def render_plain_text(data, plays):
    def play_for(a_performance):
        return plays[a_performance['playID']]
    def amount_for(a_performance):
        result = 0
        if play_for(a_performance)['type'] == "tragedy":
            result = 40000
            if a_performance['audience'] > 30:
                result += 1000 * (a_performance['audience'] - 30)
        elif play_for(a_performance)['type'] == "comedy":
            result = 30000
            if a_performance['audience'] > 20:
                result += 10000 + 500 * (a_performance['audience'] - 20)
            result += 300 * a_performance['audience']
        else:
            raise ValueError(f"unknown type: {play_for(a_performance)['type']}")
        return result

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance['audience'] - 30, 0)
        if "comedy" == play_for(a_performance)['type']:
            result += a_performance['audience'] // 5
        return result

    def usd(cents):
        return "${:,.2f}".format(cents / 100)

    def total_volume_credits():
        result = 0
        for perf in data['performances']:
            result += volume_credits_for(perf)
        return result

    def total_amount():
        result = 0
        for perf in data['performances']:
            result += amount_for(perf)
        return result

    result = f"Statement for {data['customer']}\n"

    for perf in data['performances']:
        result += f"  {play_for(perf)['name']}: {usd(amount_for(perf))} ({perf['audience']} seats)\n"

    result += f"Amount owed is {usd(total_amount())}\n"
    result += f"You earned {total_volume_credits()} credits\n"
    return result
