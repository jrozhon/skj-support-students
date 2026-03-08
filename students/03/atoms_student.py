import marimo

__generated_with = "0.13.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # Atoms Playground 🟢🟡

        ## Task 1 (2 points)
        - Fill in the `Atom` class initializer (`pos`, `vel`, `rad`, `color`).
        - Implement `to_tuple` to return `(x, y, radius, color)`.
        - Implement `random_atom` in `ExampleWorld` to generate a random green atom.
        - Implement `generate_atoms` to create the initial list of atoms.
        - Implement `apply_speed` to move atoms and bounce off walls.

        ## Task 2 (2 points)
        - Create `FallDownAtom` inheriting from `Atom` with class variables `g` and `damping`.
        - Override `apply_speed` to add gravity and damping on ground bounce.
        - Implement `random_falldown_atom` in `ExampleWorld`.

        ## Task 3 (1 point)
        - Implement `add_atom` and `add_falldown_atom` triggered by button clicks.
        """
    )
    return


@app.cell
def _():
    import random
    return (random,)


@app.cell
def _():
    class Atom:

        def __init__(self, pos: tuple[int, int], vel: tuple[int, int], rad: int, col: str):
            """
            Initializer of Atom class

            :param pos: tuple (x, y) position
            :param vel: tuple (vx, vy) velocity
            :param rad: radius
            :param col: color of displayed circle
            """
            pass

        def to_tuple(self) -> tuple[int, int, int, str]:
            """
            Returns tuple representing an atom.

            Example: pos = (10, 12), rad = 15, color = 'green' -> (10, 12, 15, 'green')
            """
            pass

        def apply_speed(self, size_x: int, size_y: int):
            """
            Applies velocity `vel` to atom's position `pos`.
            Check boundary collisions and reverse direction when hitting edges.
            Clamp the position back to the boundary to prevent the atom from escaping.

            :param size_x: width of the world space
            :param size_y: height of the world space
            """
            pass

    return (Atom,)


@app.cell
def _(Atom):
    class FallDownAtom(Atom):
        """
        Class to represent atoms that are pulled by gravity.

        Set gravity factor g to ~3.0
        Set damping factor to ~0.7

        Override apply_speed to:
        - Add g to vertical velocity each tick
        - On hitting the ground (bottom edge), clamp position and damp both vx and vy by multiplying with damping
        - Clamp position on all boundary hits to prevent atoms from escaping
        """

        g = 3.0
        damping = 0.7

        pass

    return (FallDownAtom,)


@app.cell
def _(Atom, FallDownAtom, random):
    class ExampleWorld:

        def __init__(self, size_x: int, size_y: int, no_atoms: int, no_falldown_atoms: int):
            self.width = size_x
            self.height = size_y
            self.atoms: list[Atom | FallDownAtom] = []
            # TODO: call generate_atoms here

        def generate_atoms(self, no_atoms: int, no_falldown_atoms: int) -> list[Atom | FallDownAtom]:
            """
            Generates no_atoms Atom instances and no_falldown_atoms FallDownAtom instances.
            Returns list of all atom instances.
            """
            pass

        def random_atom(self) -> Atom:
            """
            Generates one Atom at random position with random velocity, random radius, green color.
            """
            pass

        def random_falldown_atom(self) -> FallDownAtom:
            """
            Generates one FallDownAtom at random position with random velocity, random radius, yellow color.
            """
            pass

        def add_atom(self, pos_x: int, pos_y: int):
            """
            Adds a new Atom at the given position with random velocity and radius.
            """
            pass

        def add_falldown_atom(self, pos_x: int, pos_y: int):
            """
            Adds a new FallDownAtom at the given position with random velocity and radius.
            """
            pass

        def tick(self) -> list[tuple[int, int, int, str]]:
            """
            Moves all atoms and returns list of tuples for rendering.
            """
            # TODO: call apply_speed on each atom and return list of to_tuple results
            return [(120, 60, 15, "#43B02A"), (240, 300, 10, "#FFB81C")]

    return (ExampleWorld,)


@app.cell
def _():
    # Configuration
    SIZE_X, SIZE_Y = 700, 400
    NO_ATOMS = 5
    NO_FALLDOWN_ATOMS = 5
    return NO_ATOMS, NO_FALLDOWN_ATOMS, SIZE_X, SIZE_Y


@app.cell
def _(ExampleWorld, NO_ATOMS, NO_FALLDOWN_ATOMS, SIZE_X, SIZE_Y, mo):
    # Create world instance (stored in mo.state so buttons can mutate it)
    get_world, set_world = mo.state(
        ExampleWorld(SIZE_X, SIZE_Y, NO_ATOMS, NO_FALLDOWN_ATOMS)
    )

    # Buttons use on_click to add atoms via mo.state
    add_atom_btn = mo.ui.button(
        label="Add Atom (green)",
        kind="success",
        on_click=lambda _: set_world(
            lambda w: (w.add_atom(random.randint(20, SIZE_X - 20), random.randint(20, SIZE_Y - 20)), w)[1]
        ),
    )
    add_falldown_btn = mo.ui.button(
        label="Add FallDown Atom (yellow)",
        kind="warn",
        on_click=lambda _: set_world(
            lambda w: (w.add_falldown_atom(random.randint(20, SIZE_X - 20), random.randint(20, SIZE_Y - 20)), w)[1]
        ),
    )

    # Dropdown to control atom count
    atom_count_dropdown = mo.ui.dropdown(
        options={"3": 3, "5": 5, "10": 10, "20": 20, "50": 50},
        value="5",
        label="Initial atoms per type",
    )
    return add_atom_btn, add_falldown_btn, atom_count_dropdown, get_world, set_world


@app.cell
def _(ExampleWorld, SIZE_X, SIZE_Y, atom_count_dropdown, mo, set_world):
    # Reset world when dropdown changes
    reset_btn = mo.ui.button(
        label="Reset",
        kind="danger",
        on_click=lambda _: set_world(
            ExampleWorld(SIZE_X, SIZE_Y, int(atom_count_dropdown.value), int(atom_count_dropdown.value))
        ),
    )
    return (reset_btn,)


@app.cell
def _(mo):
    # Animation refresh timer
    refresh = mo.ui.refresh(default_interval="100ms")
    return (refresh,)


@app.cell
def _(SIZE_X, SIZE_Y, add_atom_btn, add_falldown_btn, atom_count_dropdown, get_world, mo, refresh, reset_btn):
    # Trigger refresh to get new frame
    _ = refresh.value

    world = get_world()
    atoms_data = world.tick()

    # Build SVG canvas
    svg_elements = []
    for atom in atoms_data:
        x, y, rad, color = atom
        svg_elements.append(
            f'<circle cx="{x}" cy="{y}" r="{rad}" fill="{color}" opacity="0.85"/>'
        )

    circles_svg = "\n".join(svg_elements)

    canvas = mo.Html(f"""
    <svg width="{SIZE_X}" height="{SIZE_Y}" style="background-color: white; border-radius: 8px; border: 2px solid #00A499;">
        {circles_svg}
    </svg>
    """)

    controls = mo.vstack([
        refresh,
        mo.md(f"**Atoms: {len(atoms_data)}**"),
        add_atom_btn,
        add_falldown_btn,
        atom_count_dropdown,
        reset_btn,
    ], align="start", gap=0.5)

    mo.hstack([canvas, controls], justify="start", align="start", gap=1)
    return


if __name__ == "__main__":
    app.run()
