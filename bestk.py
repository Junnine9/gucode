import pyupbit
import numpy as np


def get_ror(k=0.3):
    df = pyupbit.get_ohlcv("KRW-BTT", count=28)
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0005
    df['ror'] = np.where(df['high'] > df['target'],
                         df['close'] / df['target'] - fee,
                         1)

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.1):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))

    # 04월 26일 기준 / fee 없이
    # 14일 - k값 0.3 일 때 하락장 시작 / 04월 13일 ~ 04월 26일 - 하락장이였음
    # 21일 - k값 0.5 일 때 하락장 시작 / 04월 06일 ~ 04월 26일 - 하락장이였음
    # 28일 - k값 0.4 일 때 이 때는 상승장 / 03월 30일 ~ 04월 26일 
    # 하락장일 땐 k 값은 0.3

  # 04월 26일 기준 / fee
    # 14일 - k값 0.3 일 때 하락장 시작 / 04월 13일 ~ 04월 26일 - 하락장이였음
    # 21일 - k값 0.5 일 때 하락장 시작 / 04월 06일 ~ 04월 26일 - 하락장이였음
    # 28일 - k값 0.4 일 때 이 때는 상승장 / 03월 30일 ~ 04월 26일 
    # 하락장일 땐 k 값은 0.3

