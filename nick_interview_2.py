# Start 1335
# End 1417
# Feedback from Nick:
# - Make sure to strongly communicate even when doing an open-ended problem like this!

# Question was to try and predict, given a JSON file, when the next payday will be
# See plaid.json

import json
import datetime
from datetime import timedelta

with open('./plaid.json', 'r') as f:
    data = json.load(f)
    txns = data['transactions']
    payroll_txns = []
    for txn in txns:
        if 'category' not in txn:
            print("Category not in transaction")
            print(txn)
            continue
        if txn['category']:
            if 'Payroll' in txn['category']:
                payroll_txns.append(txn)

    dates = [(txn['date'], txn['amount']) for txn in payroll_txns]

    tds = []
    for idx, date in enumerate(dates):
        if idx == len(dates) - 1:
            pass
        else:
            d0 = datetime.datetime.strptime(date[0], "%Y-%m-%d").date()
            d1 = datetime.datetime.strptime(dates[idx+1][0], "%Y-%m-%d").date()
            tds.append(d0 - d1)
    timedeltadays = ([td.days for td in tds])
    mode = max(set(timedeltadays), key=timedeltadays.count)

    d = timedelta(days=mode)
    last_payment_date = datetime.datetime.strptime(
        dates[0][0], "%Y-%m-%d").date()

    next_payment_date = last_payment_date + d
    print(next_payment_date)

    # return next_payment_date
