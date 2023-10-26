"""Expected values for the tests are collected in this file.

For each test file, there should be a dictionary with the name of the test file. Inside
this dictionary, there should be a dictionary with the name of the test function/class,
containing the expected values for the test named according to what they are compared
to.

"""
import numpy as np

# test_mpsa.py
_grad_bound_known = np.array(
    [
        [0.10416667, 0.0, 0.0, 0.0, 0.0, -0.02083333, 0.0, 0.0],
        [0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.10416667, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.02083333],
        [0.0, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.10416667, 0.0, 0.0, 0.02083333, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.10416667, 0.0, 0.0, 0.0, 0.0, -0.02083333],
        [0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0],
        [-0.02083333, 0.0, 0.0, 0.0, 0.0, 0.10416667, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.25, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.02083333, 0.0, 0.0, 0.10416667, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0],
        [0.02083333, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.10416667],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.25, 0.0],
        [0.0, 0.0, -0.02083333, 0.0, 0.0, 0.0, 0.0, 0.10416667],
    ]
)
_grad_cell = np.array(
    [
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
        [1.0, 0.0],
        [0.0, 1.0],
    ]
)
test_mpsa = {
    "MpsaReconstructBoundaryDisplacement": {
        "test_cart_2d": {
            "grad_bound_known": _grad_bound_known,
            "grad_cell_known": _grad_cell,
        },
    }
}
# test_mpfa.py
_grad_bound = np.array(
    [
        [-0.25, 0.0, 0.0, 0.0],
        [0.0, -0.25, 0.0, 0.0],
        [0.0, 0.0, -0.25, 0.0],
        [0.0, 0.0, 0.0, -0.25],
    ]
)
_D_g = np.array(
    [
        [-1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, -1.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, -1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
    ]
)
test_mpfa = {
    "TestMpfaPressureReconstructionMatrices": {
        "test_cart_2d": {
            "grad_bound": _grad_bound,
            "D_g": _D_g,
        },
    }
}
_D_g = np.array(
    [
        [-1 / 6, -1 / 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0],
        [0, 0, -1 / 6, -1 / 3, 0, 0, 0, 0, 0, 0, 0, 0.0],
        [0, 0, 0, 0, 0, 0, -1 / 3, -1 / 6, 0, 0, 0, 0.0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1 / 3, -1 / 6, 0, 0.0],
        [-1 / 12, 1 / 12, 0, 0, 0, 0, 1 / 12, -1 / 12, 0, 0, 0, 0],
        [0, 0, 0, 0, -1 / 12, 1 / 12, 0, 0, 0, 0, 1 / 12, -1 / 12],
        [0, 0, 1 / 3, 1 / 6, 0, 0, 0, 0, 0, 0, 0, 0.0],
        [0, 0, 0, 0, 1 / 3, 1 / 6, 0, 0, 0, 0, 0, 0.0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1 / 6, 1 / 3, 0, 0.0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1 / 6, 1 / 3],
    ]
)

_CC = np.array(
    [
        [1, 0.0],
        [1, 0.0],
        [0, 1.0],
        [0, 1.0],
        [0.5, 0.5],
        [0.5, 0.5],
        [1, 0.0],
        [1, 0.0],
        [0, 1.0],
        [0, 1.0],
    ]
)
test_mpfa["TestMpfaPressureReconstructionMatrices"]["test_simplex_2d"] = {
    "D_g": _D_g,
    "CC": _CC,
}


_D_g = np.array(
    [
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    ]
)

_CC = np.array(
    [
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
        [1],
    ]
)
test_mpfa["TestMpfaPressureReconstructionMatrices"]["test_cart_3d"] = {
    "D_g": _D_g,
    "CC": _CC,
}

## test_tags.py
test_tags = {}

_known_faces_2d_simplex = np.array(
    [
        True,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)

_known_nodes_2d_simplex = np.array(
    [
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        True,
        True,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)

test_tags["func_2d_simplex"] = {
    "known_faces": _known_faces_2d_simplex,
    "known_nodes": _known_nodes_2d_simplex,
}

_known_faces_2d_cartesian = np.array(
    [
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)
_known_nodes_2d_cartesian = np.array(
    [
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)

test_tags["func_2d_cartesian"] = {
    "known_faces": _known_faces_2d_cartesian,
    "known_nodes": _known_nodes_2d_cartesian,
}

_known_faces_3d_simplex = np.array(
    [
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
        True,
        False,
        True,
        True,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        False,
        False,
        True,
        False,
        True,
        True,
        False,
        True,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        True,
        False,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        False,
        False,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        False,
        False,
        True,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)
_known_nodes_3d_simplex = np.array(
    [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)

test_tags["func_3d_simplex"] = {
    "known_faces": _known_faces_3d_simplex,
    "known_nodes": _known_nodes_3d_simplex,
}

_known_faces_3d_cartesian = np.array(
    [
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)
_known_nodes_3d_cartesian = np.array(
    [
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
        True,
    ],
    dtype=bool,
)
test_tags["func_3d_cartesian"] = {
    "known_faces": _known_faces_3d_cartesian,
    "known_nodes": _known_nodes_3d_cartesian,
}

# test_grid.py
test_grid = {}
_x = np.array(
    [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2]
)
_y = np.array(
    [0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2, 0, 0, 0, 1, 1, 1, 2, 2, 2]
)
_z = np.array(
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
)
test_grid["test_geometry_3d_unperturbed"] = {"x": _x, "y": _y, "z": _z}

_face_centers = np.array(
    [
        [
            0.33333333,
            0.33333333,
            0.0,
            0.66666667,
            0.33333333,
            0.33333333,
            1.0,
            0.66666667,
            0.66666667,
            0.33333333,
            0.66666667,
            0.33333333,
            0.0,
            0.66666667,
            1.0,
            0.66666667,
            0.33333333,
            0.66666667,
        ],
        [
            0.33333333,
            0.0,
            0.33333333,
            0.66666667,
            0.33333333,
            0.66666667,
            0.33333333,
            0.66666667,
            0.0,
            0.33333333,
            0.33333333,
            1.0,
            0.66666667,
            0.66666667,
            0.66666667,
            1.0,
            0.33333333,
            0.66666667,
        ],
        [
            0.0,
            0.33333333,
            0.33333333,
            0.0,
            0.33333333,
            0.33333333,
            0.33333333,
            0.33333333,
            0.66666667,
            0.66666667,
            0.66666667,
            0.33333333,
            0.66666667,
            0.66666667,
            0.66666667,
            0.66666667,
            1.0,
            1.0,
        ],
    ]
)
test_grid["test_geometry_tetrahedral_grid"] = {"face_centers": _face_centers}


# test_meshing.py
test_meshing = {
    "test_fracture_and_boundary_face_tags_2d_domain_x_intersection": {
        "fracture_tags": np.array(
            [
                False,
                True,
                False,
                False,  # first row
                False,
                True,
                False,
                False,  # Second row
                False,
                False,
                False,
                False,  # third row
                False,
                False,
                False,  # Bottom column
                True,
                True,
                False,  # Second column
                False,
                False,
                False,  # Third column
                False,
                False,
                False,  # Top column
                True,
                True,
                True,
                True,
            ]
        ),
        "domain_boundary_tags": np.array(
            [
                True,
                False,
                False,
                True,  # first row
                True,
                False,
                False,
                True,  # Second row
                True,
                False,
                False,
                True,  # third row
                True,
                True,
                True,  # Bottom column
                False,
                False,
                False,  # Second column
                False,
                False,
                False,  # Third column
                True,
                True,
                True,  # Top column
                False,
                False,
                False,
                False,
            ]
        ),
    }
}


# test_fvutils.py
_neu_inds = np.array(
    [
        30,
        31,
        36,
        37,
        38,
        39,
        44,
        45,
        46,
        47,
        52,
        53,
        24,
        66,
        25,
        67,
        26,
        27,
        28,
        68,
        29,
        69,
    ]
)
_dir_inds = np.array(
    [
        0,
        1,
        6,
        7,
        8,
        9,
        14,
        15,
        16,
        17,
        22,
        23,
        24,
        54,
        25,
        55,
        26,
        56,
        27,
        57,
        28,
        58,
        29,
        59,
        72,
        73,
    ]
)
test_fvutils = {"test_bound_exclusion": {"neu_inds": _neu_inds, "dir_inds": _dir_inds}}
