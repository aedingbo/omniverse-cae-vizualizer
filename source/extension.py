import os
import csv
import math
import omni.ext
import omni.ui as ui
import carb

# USD / Omniverse stage helpers
import omni.usd
from pxr import UsdGeom, Gf, Sdf

# ------------------------------
# Utility functions
# ------------------------------
def _normalize(values):
    if not values:
        return []
    vmin, vmax = min(values), max(values)
    if math.isclose(vmin, vmax):
        return [0.5 for _ in values]
    return [(v - vmin) / (vmax - vmin) for v in values]

def _color_from_norm(t):
    """Map [0,1] to RGB: blue->green->red."""
    t = max(0.0, min(1.0, float(t)))
    if t < 0.5:
        tt = t / 0.5
        return (0.0, tt, 1.0 - tt)
    else:
        tt = (t - 0.5) / 0.5
        return (tt, 1.0 - tt, 0.0)

def _read_csv_values(path, column="value"):
    vals = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if column not in reader.fieldnames:
            raise ValueError(f"CSV missing '{column}' column.")
        for row in reader:
            try:
                vals.append(float(row[column]))
            except Exception:
                continue
    return vals

# ------------------------------
# Build cubes in the scene
# ------------------------------
def _make_colored_cubes(stage, values, size=1.0, gap=0.2):
    root = UsdGeom.Xform.Define(stage, Sdf.Path("/World/Vis"))
    norms = _normalize(values)
    x = 0.0
    for i, t in enumerate(norms):
        path = Sdf.Path(f"/World/Vis/Cube_{i}")
        cube = UsdGeom.Cube.Define(stage, path)
        cube.CreateSizeAttr(size)
        xform = UsdGeom.Xformable(cube)
        xform.AddTranslateOp().Set(Gf.Vec3d(x, 0.0, 0.0))
        r, g, b = _color_from_norm(t)
        cube.CreateDisplayColorAttr([Gf.Vec3f(r, g, b)])
        x += size + gap

# ------------------------------
# Extension class
# ------------------------------
class CaeDataVisualizerExt(omni.ext.IExt):
    def on_startup(self, ext_id):
        carb.log_info(f"[CAE Visualizer] Startup: {ext_id}")

        # Default CSV path
        this_dir = os.path.dirname(os.path.dirname(__file__))
        self._default_csv = os.path.join(this_dir, "data", "sample_results.csv")

        # UI window
        self._window = ui.Window("CAE Visualizer", width=360, height=200)
        with self._window.frame:
            with ui.VStack(spacing=8, height=0):
                ui.Label("CSV → Colored Cubes", style={"color": 0xFFE0E0E0})
                with ui.HStack(spacing=6):
                    ui.Label("CSV Path:", width=60)
                    self._path_field = ui.StringField()
                    self._path_field.model.set_value(self._default_csv)
                    ui.Button("Load CSV", clicked_fn=self._on_click_load)

    def _on_click_load(self):
        try:
            path = self._path_field.model.get_value_as_string()
            values = _read_csv_values(path)
            stage = omni.usd.get_context().get_stage()
            if not stage:
                omni.usd.get_context().new_stage()
                stage = omni.usd.get_context().get_stage()
            # Clear previous
            if stage.GetPrimAtPath("/World/Vis"):
                stage.RemovePrim("/World/Vis")
            _make_colored_cubes(stage, values)
            carb.log_info(f"[CAE Visualizer] Loaded {len(values)} values from {path}")
        except Exception as e:
            carb.log_error(f"[CAE Visualizer] Error: {e}")

    def on_shutdown(self):
        carb.log_info("[CAE Visualizer] Shutdown")
        self._window = None