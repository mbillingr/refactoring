def statement(invoice, plays):
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
        volume_credits = 0
        volume_credits += max(a_performance['audience'] - 30, 0)
        if "comedy" == play_for(a_performance)['type']:
            volume_credits += a_performance['audience'] // 5
        return volume_credits

    total_amount = 0
    volume_credits = 0
    result = f"Statement for {invoice['customer']}\n"
    format = "${:,.2f}".format

    for perf in invoice['performances']:
        volume_credits += volume_credits_for(perf)

        # print line for this order
        result += f"  {play_for(perf)['name']}: {format(amount_for(perf) / 100)} ({perf['audience']} seats)\n"
        total_amount += amount_for(perf)

    result += f"Amount owed is {format(total_amount / 100)}\n"
    result += f"You earned {volume_credits} credits\n"
    return result
