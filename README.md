Omniverse CAE Visualizer: A Kit-CAE Integration Proof-of-Concept

Overview

This project is a proof-of-concept demonstrating a core integration pattern for connecting external engineering data with NVIDIA's Omniverse platform. It exemplifies a workflow that a customer or ISV (Independent Software Vendor) would use to bring their own CAE simulation results into a collaborative, real-time 3D environment.

Key Accomplishments
- Omniverse Kit SDK Extension Development: Built a custom extension from the ground up, showcasing a fundamental skill for integrating with Omniverse-based applications.
- Workflow Integration: Establishes a data bridge between external CAE results (stored in a CSV) and the Omniverse USD (Universal Scene Description) stage. This is a direct parallel to how engineering software is integrated with the platform.
- Engineering Data-to-3D Mapping: Visually maps scalar CAE values (e.g., stress, displacement) to 3D geometry properties (color, size) within the USD scene.
- Custom UI Development: Leverages the omni.ui library to create a custom user interface, providing an intuitive way for engineers to trigger the data ingestion workflow.

Technical Details
The extension is built using Python within the Omniverse Kit SDK. Key components include:
- ext.toml: Defines the extension's metadata and dependencies, managing its lifecycle within the Omniverse ecosystem.
- extension.py: Contains the core logic, including the IExt interface methods (on_startup, on_shutdown).
- USD Scene Manipulation: Uses the pxr.UsdGeom API to programmatically create and manipulate 3D geometry (cubes) on the stage based on the input data.
- Data Parsing: Employs standard Python libraries to read and process the CSV input file, demonstrating proficiency in data engineering.

Project Structure 
omniverse-cae-visualizer/
├── README.md
├── ext.toml                # Extension metadata
├── data/
│   └── sample_results.csv   # Example CAE results
└── source/
    ├── __init__.py
    └── extension.py         # Extension logic


