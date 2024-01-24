import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse

# ノードの位置と方向
nodes = {
    "1": {"position": (8.5353798e-11, 2.3586731e-12), "orientation": 6.46369985e-11},
    "2": {"position": (2, -4.74793416e-12), "orientation": 5.98996275e-11},
    "3": {"position": (4, 2.38926106e-12), "orientation": 5.99195006e-11}
}

# 分散共分散行列
covariances = {
    "1": np.array([
        [0.00828571429,  7.82228372e-14, -2.06607043e-13],
        [7.82228372e-14,  0.00944444444, -0.00305555556],
        [-2.06607043e-13, -0.00305555556,  0.00819444445]
    ]),
    "2": np.array([
        [0.00714285714,  3.80266543e-14, -5.38289642e-14],
        [3.80266543e-14,  0.00777777778, -0.00111111111],
        [-5.38289642e-14, -0.00111111111,  0.00819444444]
    ]),
    "3": np.array([
        [0.00828571429, 6.60868131e-14, 1.73935528e-13],
        [6.60868131e-14,  0.00944444444,  0.00305555556],
        [1.73935528e-13,  0.00305555556,  0.0181944444]
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

# グラフのプロット
fig, ax = plt.subplots()
for node_id, node_data in nodes.items():
    x, y = node_data["position"]
    ax.plot(x, y, 'o', label=f"Node {node_id}")
    plot_ellipse(ax, (x, y), covariances[node_id], 'blue')

# エッジ（ファクター）のプロット
ax.plot([nodes["1"]["position"][0], nodes["2"]["position"][0]], [nodes["1"]["position"][1], nodes["2"]["position"][1]], 'k-')
ax.plot([nodes["2"]["position"][0], nodes["3"]["position"][0]], [nodes["2"]["position"][1], nodes["3"]["position"][1]], 'k-')

# グラフの設定
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.set_title('GTSAM Factor Graph Visualization')

plt.show()
