Omniverse CAE Visualizer

Overview

This project demonstrates how to integrate CAE (Computer-Aided Engineering) data with the NVIDIA Omniverse Kit SDK by developing a lightweight extension. The extension is designed to read a CSV file of CAE-style results and represent them in a 3D scene as geometry (cubes). The focus of this project is not on building a production-ready application but on showing how Omniverse extensions can connect external engineering data into an Omniverse workflow.

Features

- Omniverse extension built with the Kit SDK.
- Parses CAE results from a CSV file.
- Generates a row of 3D cubes with color and size scaled to simulation values.
- Custom extension panel to trigger CSV-to-USD visualization.
- Demonstrates how engineering data can be mapped to 3D scene geometry.
- Lightweight demo designed to illustrate integration with Omniverse.

Project Structure 

omniverse-cae-visualizer/
├── README.md
├── ext.toml                # Extension metadata
├── data/
│   └── sample_results.csv   # Example CAE results
└── source/
    ├── __init__.py
    └── extension.py         # Extension logic


