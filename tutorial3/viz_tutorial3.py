import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Ellipse, Circle

# ノードの位置と方向
nodes = {
    "1": {"position": (-2.7684295e-20, -8.15199774e-20), "orientation": 6.46369985e-11},
    "2": {"position": (2, -1.89295335e-19), "orientation": 5.98996275e-11},
    "3": {"position": (4, -3.42174082e-11), "orientation": 5.99195006e-11},
    "4": {"position": (4, 2), "orientation": 5.99195006e-11},
    "5": {"position": (2, 2), "orientation": 5.99195006e-11}
}

# 分散共分散行列
covariances = {
    "1": np.array([
        [0.09, -2.13e-18, -7.19e-18],
        [-2.13e-18, 0.09, -5.76e-17],
        [-7.19e-18, -5.76e-17, 0.01]
    ]),
    "2": np.array([
        [0.13, -2.52e-17, -2.01e-17],
        [-2.52e-17, 0.17, 0.02],
        [-2.01e-17, 0.02, 0.02]
    ]),
    "3": np.array([
        [0.362, -3.29e-12, 0.062],
        [-3.29e-12, 0.162, -0.002],
        [0.062, -0.002, 0.0265]
    ]),
    "4": np.array([
        [0.268, -0.128, 0.048],
        [-0.128, 0.378, -0.068],
        [0.048, -0.068, 0.028]
    ]),
    "5": np.array([
        [0.202, 0.036, -0.018],
        [0.036, 0.26, -0.051],
        [-0.018, -0.051, 0.0265]
    ])
}

# 推定位置
estimated_positions = {
    "1": (0.5, 0),
    "2": (2.3, 0.1),
    "3": (4.1, 0.1),
    "4": (4, 2),
    "5": (2.1, 2.1)
}

def plot_ellipse(ax, mean, covariance, color):
    """ 楕円をプロットする関数 """
    cov_2x2 = covariance[0:2, 0:2]
    eigenvalues, eigenvectors = np.linalg.eig(cov_2x2)
    
    angle = np.degrees(np.arctan2(*eigenvectors[:,0][::-1]))
    width, height = 2 * np.sqrt(eigenvalues)
    
    ellipse = Ellipse(xy=mean, width=width, height=height, angle=angle, color=color, alpha=0.5)
    ax.add_patch(ellipse)

def plot_circle(ax, center, radius, color):
    """ 円をプロットする関数 """
    circle = Circle(center, radius, color=color, fill=False)
    ax.add_patch(circle)

# グラフのプロット
fig, ax = plt.subplots()
for node_id, node_data in nodes.items():
    x, y = node_data["position"]
    ax.plot(x, y, 'o', label=f"Node {node_id}")
    plot_ellipse(ax, (x, y), covariances[node_id], 'blue')
    # 推定位置をプロット
    ex, ey = estimated_positions[node_id]
    ax.plot(ex, ey, 'x', color='red', label=f"Est {node_id}")

# エッジ（ファクター）のプロット
ax.plot([nodes["1"]["position"][0], nodes["2"]["position"][0]], [nodes["1"]["position"][1], nodes["2"]["position"][1]], 'k-')
ax.plot([nodes["2"]["position"][0], nodes["3"]["position"][0]], [nodes["2"]["position"][1], nodes["3"]["position"][1]], 'k-')
ax.plot([nodes["3"]["position"][0], nodes["4"]["position"][0]], [nodes["3"]["position"][1], nodes["4"]["position"][1]], 'k-')
ax.plot([nodes["4"]["position"][0], nodes["5"]["position"][0]], [nodes["4"]["position"][1], nodes["5"]["position"][1]], 'k-')
ax.plot([nodes["5"]["position"][0], nodes["2"]["position"][0]], [nodes["5"]["position"][1], nodes["2"]["position"][1]], 'k-')

# グラフの設定
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 3)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.set_title('GTSAM Factor Graph Visualization')
ax.set_aspect('equal')  # 縦横のスケールを1:1に設定

plt.show()
