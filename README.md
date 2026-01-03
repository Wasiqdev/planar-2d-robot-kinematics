# Planar 2-DOF Robot Kinematics

This repository contains an analytical and computational study of a
planar two-degree-of-freedom (2-DOF) robotic manipulator. The project
focuses on forward and inverse kinematics, workspace analysis, and
Jacobian-based singularity analysis.

## Overview
The manipulator is modeled as a planar system with two revolute joints.
Forward kinematics map joint angles to Cartesian end-effector position,
while inverse kinematics are solved analytically using geometric
principles and explicit reachability conditions. The Jacobian matrix is
derived to analyze instantaneous motion and singular configurations.

## Contents
- `src/fk.py` — Forward kinematics implementation
- `src/ik.py` — Analytical inverse kinematics with reachability checks
- `src/jacobian.py` — Jacobian matrix computation
- `src/visualize.py` — Arm visualization and workspace plotting
- `report.pdf` — Full technical report describing the model and results

## Key Concepts
- Planar robot kinematics
- Multiple inverse kinematics solutions (elbow-up / elbow-down)
- Workspace geometry and reachability
- Jacobian singularities and loss of degrees of freedom

## Notes
This project emphasizes mathematical modeling and physical
interpretation rather than control or dynamics. It is intended as a
foundational study in robotics and machine intelligence.
