import numpy as np

def inverse_kinematics(x, y, l1, l2):
    """
    Computes the inverse kinematics for a planar 2-DOF robotic arm.
    Returns two solutions (elbow-up and elbow-down) if reachable.
    """

    r2 = x**2 + y**2
    cos_theta2 = (r2 - l1**2 - l2**2) / (2 * l1 * l2)

    # Reachability check
    if cos_theta2 < -1 or cos_theta2 > 1:
        return None  # unreachable target

    theta2_pos = np.arccos(cos_theta2)
    theta2_neg = -theta2_pos

    solutions = []

    for theta2 in [theta2_pos, theta2_neg]:
        k1 = l1 + l2 * np.cos(theta2)
        k2 = l2 * np.sin(theta2)

        theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)
        solutions.append((theta1, theta2))

    return solutions

if __name__ == "__main__":
    from fk import forward_kinematics

    l1 = 1.0
    l2 = 1.0

    targets = [
        (1.0, 1.0),
        (0.0, 2.0),
        (2.0, 0.0),
        (3.0, 0.0)  # unreachable
    ]

    for x, y in targets:
        sols = inverse_kinematics(x, y, l1, l2)
        print(f"\nTarget: ({x}, {y})")

        if sols is None:
            print("  Unreachable")
            continue

        for i, (t1, t2) in enumerate(sols):
            x_fk, y_fk = forward_kinematics(t1, t2, l1, l2)
            print(f"  Solution {i+1}: θ1={t1:.2f}, θ2={t2:.2f} -> FK=({x_fk:.2f}, {y_fk:.2f})")
