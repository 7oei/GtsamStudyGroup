import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルのパス
csv_path = 'tutorial4.csv'

# CSVを読み込む（ヘッダーがないため、列名を手動で設定）
df = pd.read_csv(csv_path, header=None)
df.columns = ['x', 'y', 'z']  # 3列目はこの例では使用しない

# 2Dポーズをプロット
plt.figure(figsize=(8, 6))
plt.plot(df['x'], df['y'], marker='o', linestyle='-', color='blue')  # 点をプロットし、点同士を直線で結ぶ
plt.title('2D Pose')  # グラフのタイトル
plt.xlabel('X')  # X軸のラベル
plt.ylabel('Y')  # Y軸のラベル
plt.grid(True)  # グリッドを表示
plt.gca().set_aspect('equal', adjustable='box')  # アスペクト比を1:1に設定
plt.show()
