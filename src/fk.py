import numpy as np

def forward_kinematics(theta1, theta2, l1, l2):
    """
    Computes the (x, y) position of the end-effector
    for a planar 2-DOF robotic arm.
    Angles are in radians.
    """
    x = l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2)
    y = l1 * np.sin(theta1) + l2 * np.sin(theta1 + theta2)
    return x, y


if __name__ == "__main__":
    l1 = 1.0
    l2 = 1.0

    tests = [
        (0, 0),
        (np.pi / 2, 0),
        (0, np.pi / 2)
    ]

    for theta1, theta2 in tests:
        x, y = forward_kinematics(theta1, theta2, l1, l2)
        print(f"theta1={theta1:.2f}, theta2={theta2:.2f} -> x={x:.2f}, y={y:.2f}")
