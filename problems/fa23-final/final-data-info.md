# Data Overview: Fraudulent Transactions

Today, we're diving into the high-stakes world of fraud detection. Each row in the DataFrame `txn` represents one online transaction, or purchase. The `txn` DataFrame is indexed by `"transaction_id" (int)`, which is a unique identifier for a transaction. The columns of `txn` are as follows:

- `"is_fraud" (bool)`: `True` if the transaction was fraudulent and `False` if not.
- `"amount" (float)`: The dollar amount of the transaction.
- `"method" (str)`: The payment method; either `"debit"` or `"credit"`.
- `"card" (str)`: The payment network of the card used for the transaction; either `"visa"`, `"mastercard"`, `"american express"`, or `"discover"`.
- `"lifetime" (float)`: The total transaction amount of all transactions made with this card over its lifetime.
- `"browser" (str)`: The web browser used for the online transaction. There are 100 distinct browser types in this column; some examples include `"samsung browser 6.2"`, `"mobile safari 11.0"`, and `"chrome 62.0"`.    

The first few rows of `txn` are shown below, though `txn` has 140,000 rows in total. Assume that the data in `txn` is a simple random sample from the much larger population of **all** online transactions.


<center><img src='../assets/images/fa23-final/final-data-info.png' width=800></center>

Throughout this exam, assume that we have already run `import babypandas as bpd` and `import numpy as np`.