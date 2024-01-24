import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# 新しいノードの位置と方向
nodes = {
    "1": {"position": (7.46978309e-16, -5.34409095e-16), "orientation": -1.78381861e-16},
    "2": {"position": (2, -1.09236636e-15), "orientation": -2.48671177e-16},
    "3": {"position": (4, -1.70076056e-15), "orientation": -2.50943862e-16}
}

# 新しい分散共分散行列
covariances = {
    "1": np.array([
        [0.09, 3.2e-33, 2.8e-33],
        [3.2e-33, 0.09, 2.6e-17],
        [2.8e-33, 2.6e-17, 0.01]
    ]),
    "2": np.array([
        [0.13, 1.2e-18, 6.1e-19],
        [1.2e-18, 0.17, 0.02],
        [6.1e-19, 0.02, 0.02]
    ]),
    "3": np.array([
        [0.17, 8.6e-18, 2.7e-18],
        [8.6e-18, 0.37, 0.06],
        [2.7e-18, 0.06, 0.03]
    ])
}

def plot_ellipse(ax, mean, covariance, color):
    """ 楕円をプロットする関数 """
    # 2x2の共分散行列に対してのみ固有値分解を行う
    cov_2x2 = covariance[0:2, 0:2]
    eigenvalues, eigenvectors = np.linalg.eig(cov_2x2)
    
    # 楕円のパラメータを計算
    angle = np.degrees(np.arctan2(*eigenvectors[:,0][::-1]))
    width, height = 2 * np.sqrt(eigenvalues)
    
    # 楕円を描画
    ellipse = Ellipse(xy=mean, width=width, height=height, angle=angle, color=color, alpha=0.5)
    ax.add_patch(ellipse)

# グラフの再プロット
fig, ax = plt.subplots()
for node_id, node_data in nodes.items():
    x, y = node_data["position"]
    ax.plot(x, y, 'o', label=f"Node {node_id}")
    plot_ellipse(ax, (x, y), covariances[node_id], 'green')

# エッジ（ファクター）のプロット
ax.plot([nodes["1"]["position"][0], nodes["2"]["position"][0]], [nodes["1"]["position"][1], nodes["2"]["position"][1]], 'k-')
ax.plot([nodes["2"]["position"][0], nodes["3"]["position"][0]], [nodes["2"]["position"][1], nodes["3"]["position"][1]], 'k-')

# グラフの設定
ax.set_xlim(-1, 5)
ax.set_ylim(-2, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.set_title('GTSAM Factor Graph Visualization (Updated)')

plt.show()
