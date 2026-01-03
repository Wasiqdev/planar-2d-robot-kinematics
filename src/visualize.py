import numpy as np
import matplotlib.pyplot as plt

from fk import forward_kinematics


def plot_arm(theta1, theta2, l1, l2):
    x0, y0 = 0, 0

    x1 = l1 * np.cos(theta1)
    y1 = l1 * np.sin(theta1)

    x2, y2 = forward_kinematics(theta1, theta2, l1, l2)

    plt.plot([x0, x1], [y0, y1], 'o-', linewidth=3)
    plt.plot([x1, x2], [y1, y2], 'o-', linewidth=3)

    plt.axis('equal')
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2-DOF Planar Robotic Arm")


# Figure 1: Visualization of the planar 2-DOF robotic manipulator for a representative joint configuration, illustrating the geometric interpretation of the forward kinematics model.

if __name__ == "__main__":
    l1 = 1.0
    l2 = 1.0

    plot_arm(theta1=0, theta2=np.pi/2, l1=l1, l2=l2)

    plt.show()



# Figure 2: Reachable workspace of the planar 2-DOF manipulator obtained by sweeping joint angles within their feasible ranges.

if __name__ == "__main__":
    theta1_values = np.linspace(-np.pi, np.pi, 400)
    theta2_values = np.linspace(-np.pi, np.pi, 400)

    xs = []
    ys = []

    for t1 in theta1_values:
        for t2 in theta2_values:
            x, y = forward_kinematics(t1, t2, 1, 1)

            xs.append(x)
            ys.append(y)


    plt.figure(figsize=(6,6))
    plt.scatter(xs, ys, s=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Workspace of 2-DOF Planar Manipulator')
    plt.axis('equal')
    plt.grid(True)
    plt.show()
