import pyupbit

access = "i7o6WtEuKzMn0Tv8yAaTTPBEkTJkfCPdQCfRTft4"          # 본인 값으로 변경
secret = "mVU7XbyOfZMUpuXaGbDYJc3egxOXEXoHj6TgTxF3"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-ORBS"))     # KRW-ORBS 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회