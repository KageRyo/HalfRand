import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def randomNum(n):
    """
    生成 n 個半隨機亂數。

    Args:
      n: 亂數數量。

    Returns:
      一個包含 n 個半隨機亂數的列表。
    """
    # 生成第一個隨機數。
    first_number = np.random.random()

    # 生成剩下的隨機數。
    numbers = [first_number]
    for i in range(1, n):
        # 計算下一個隨機數。
        next_number = numbers[i - 1] + np.random.uniform(-0.1, 0.1)
        # 將下一個隨機數加入列表。
        numbers.append(next_number)
    return numbers

def main():
    # 生成 100 個半隨機亂數。
    numbers = randomNum(100)

    # 將數據轉換為 Pandas 資料框。
    df = pd.DataFrame({
        "序列": range(len(numbers)),
        "日期時間": [datetime.datetime.now() + datetime.timedelta(seconds=i) for i in range(len(numbers))],
        "數值": numbers
    })

    # 繪製圖表。
    plt.plot(df["日期時間"], df["數值"])
    plt.title("halfRand")
    plt.show()

    # 輸出結果。
    print(df)
    df.to_csv("randNum.csv")

if __name__ == "__main__":
    main()
