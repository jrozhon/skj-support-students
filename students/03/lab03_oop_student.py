import marimo

__generated_with = "0.18.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 🖧 Lab 03: Object-Oriented Network Engineering

    **Duration:** 90 Minutes

    **Focus:** Classes, Constructors, Magic Methods, Operator Overloading, Iterators, Design Patterns, Immutability

    **Context:** Network Engineering & System Administration

    ---

    ### 🎯 Objective
    In this lab you will model real network infrastructure using Python classes.
    You will build IP address objects, implement a network switch simulator,
    create an event-driven alert system (Observer pattern), a logging decorator,
    and a network simulation automaton — all using OOP principles that mirror
    how production network management software is built.

    ### 📚 References
    *   [Python Classes](https://docs.python.org/3/tutorial/classes.html)
    *   [Magic Methods Cheatsheet](https://rszalski.github.io/magicmethods)
    *   [Observer Pattern](https://refactoring.guru/design-patterns/observer)
    *   [Decorator Pattern](https://refactoring.guru/design-patterns/decorator)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 1: IPv4 Address Object (Constructor, `__str__`, `__eq__`, Indexing)

    **Scenario:** Every network device has at least one IP address. Instead of
    passing raw strings around, professional tools wrap addresses in objects that
    support comparison, formatting, and octet-level access.

    **Theory:**
    *   **`__init__`** — constructor, stores instance attributes.
    *   **`__str__`** — human-readable string form (`print()`, `str()`).
    *   **`__eq__`** — equality via `==`.
    *   **`__getitem__` / `__setitem__`** — bracket indexing (`obj[i]`).

    **Task — implement the `IPv4Address` class:**
    1.  Constructor takes four integer octets (default `0`). Store them in a list attribute `octets`.
    2.  `__str__` returns dotted-decimal notation, e.g. `"192.168.1.1"`.
    3.  `__eq__` returns `True` when all octets match; `False` (not `ValueError`) for non-`IPv4Address` operands.
    4.  `__getitem__(i)` / `__setitem__(i, val)` — access individual octets. Raise `IndexError` if `i > 3`.
    5.  `__iter__` — yields each octet so you can `for o in addr`.

    ```
    addr = IPv4Address(192, 168, 1, 1)
    str(addr)          # "192.168.1.1"
    addr[0]            # 192
    addr[3] = 254      # addr is now 192.168.1.254
    addr == IPv4Address(192, 168, 1, 254)  # True
    list(addr)         # [192, 168, 1, 254]
    ```
    """)
    return


@app.cell
def _():
    class IPv4Address:
        """Models a single IPv4 address with octet-level access.

        Implement:
        - __init__(o1=0, o2=0, o3=0, o4=0): store octets in a list
        - __str__: return dotted-decimal "o1.o2.o3.o4"
        - __eq__: compare octets; return False for non-IPv4Address
        - __getitem__(i): return octet at index i; IndexError if i > 3
        - __setitem__(i, val): set octet at index i; IndexError if i > 3
        - __iter__: yield each octet
        """
        pass

    # ── Tests (do not modify) ──
    addr1 = IPv4Address(10, 0, 0, 1)
    addr2 = IPv4Address(10, 0, 0, 1)
    addr3 = IPv4Address(192, 168, 1, 1)

    print(f"addr1 = {addr1}")
    print(f"addr1 == addr2 → {addr1 == addr2}")
    print(f"addr1 == addr3 → {addr1 == addr3}")
    print(f"addr3[0] = {addr3[0]}, addr3[3] = {addr3[3]}")

    addr3[3] = 254
    print(f"After addr3[3] = 254 → {addr3}")

    print(f"Iterating addr1: {list(addr1)}")

    try:
        _ = addr1[5]
    except IndexError as e:
        print(f"IndexError caught: {e}")

    print(f"addr1 == 'string' → {addr1 == 'string'}")
    return addr1, addr3


@app.cell
def _(addr1, addr3, mo):
    mo.md(f"""
    **Results:**\n\n
    - `addr1` = `{addr1}` — default gateway of the management VLAN
    - `addr3` (modified) = `{addr3}` — broadcast-adjacent address
    - Iteration works: `{list(addr1)}`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 2: Subnet Calculator (Operator Overloading: `+`, `-`, `==`)

    **Scenario:** Network engineers constantly calculate subnet boundaries.
    Model a `Subnet` that stores a network address and a prefix length, and
    supports arithmetic to shift the network ID up or down.

    **Theory:**
    *   **`__add__`** / **`__sub__`** — implement `+` and `-` operators.
    *   Both must return a **new** object (immutability of operands).
    *   Raise `ValueError` if the right operand is not an `int`.

    **Task — implement the `Subnet` class:**
    1.  Constructor takes `network` (str like `"192.168.1.0"`) and `prefix` (int, default `24`).
    2.  `__str__` returns CIDR notation, e.g. `"192.168.1.0/24"`.
    3.  `__eq__` compares both network string and prefix.
    4.  `subnet + n` → returns a new `Subnet` whose third octet is incremented by `n`.
    5.  `subnet - n` → same but decremented.
    6.  Raise `ValueError` if `n` is not an `int`.

    ```
    s = Subnet("10.0.1.0", 24)
    str(s)         # "10.0.1.0/24"
    s + 1          # Subnet("10.0.2.0", 24)
    s - 1          # Subnet("10.0.0.0", 24)
    ```
    """)
    return


@app.cell
def _():
    class Subnet:
        """Models an IPv4 subnet with CIDR prefix and arithmetic shifting.

        Implement:
        - __init__(network="0.0.0.0", prefix=24): store network and prefix
        - __str__: return "network/prefix"
        - __eq__: compare network and prefix; False for non-Subnet
        - __add__(n): return new Subnet with third octet incremented by n; ValueError if n not int
        - __sub__(n): return new Subnet with third octet decremented by n; ValueError if n not int
        """
        pass

    # ── Tests (do not modify) ──
    s1 = Subnet("10.0.1.0", 24)
    s2 = s1 + 1
    s3 = s1 - 1

    print(f"s1 = {s1}")
    print(f"s1 + 1 = {s2}")
    print(f"s1 - 1 = {s3}")
    print(f"s1 == Subnet('10.0.1.0', 24) → {s1 == Subnet('10.0.1.0', 24)}")
    print(f"s1 == s2 → {s1 == s2}")
    print(f"s1 == 42 → {s1 == 42}")

    try:
        _ = s1 + "oops"
    except ValueError as e:
        print(f"ValueError caught: {e}")
    return s1, s2, s3


@app.cell
def _(mo, s1, s2, s3):
    _s1_str = str(s1)
    _s2_str = str(s2)
    _s3_str = str(s3)
    mo.md(
        f"**Subnet arithmetic:**\n\n"
        f"| Expression | Result |\n"
        f"|---|---|\n"
        f"| `s1` | `{_s1_str}` |\n"
        f"| `s1 + 1` | `{_s2_str}` |\n"
        f"| `s1 - 1` | `{_s3_str}` |\n"
        f"\nThis is how IPAM (IP Address Management) tools iterate over address blocks."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 3: Network Alert Bus (Observer Design Pattern)

    **Scenario:** In a NOC (Network Operations Center), monitoring systems fire
    alerts when thresholds are breached — high CPU, link down, etc. Multiple
    dashboards and pagers **subscribe** to these alerts. When an alert fires,
    every subscriber is notified.

    **Theory:**
    *   **Observer pattern**: A subject maintains a list of observers and notifies
        them automatically of state changes.
    *   `subscribe(fn)` → adds `fn` to the list, returns an *unsubscribe* callable.
    *   `notify(*args, **kwargs)` → calls every subscriber with the given arguments.

    **Task — implement `AlertBus`:**
    1.  `subscribe(callback)` — appends `callback` to an internal list; returns a function that, when called, removes that callback.
    2.  `notify(*args, **kwargs)` — calls every subscribed callback with the given arguments.
    3.  The returned unsubscribe function must actually remove the callback so it is no longer notified.

    ```python
    bus = AlertBus()
    log = []
    unsub = bus.subscribe(lambda msg: log.append(msg))
    bus.notify("LINK DOWN on eth0")
    unsub()
    bus.notify("CPU HIGH on core-sw-01")
    # log == ["LINK DOWN on eth0"]  — second alert was NOT received
    ```
    """)
    return


@app.cell
def _():
    class AlertBus:
        """Observer-pattern alert distribution for NOC monitoring.

        Implement:
        - __init__: initialize empty subscriber list
        - subscribe(callback): add callback, return an unsubscribe function
        - notify(*args, **kwargs): call all subscribers with given arguments
        """
        pass

    # ── Tests (do not modify) ──
    bus = AlertBus()
    noc_log = []
    pager_log = []

    unsub_noc = bus.subscribe(lambda msg, **kw: noc_log.append(f"[NOC] {msg}"))
    unsub_pager = bus.subscribe(lambda msg, **kw: pager_log.append(f"[PAGER] {msg}"))

    bus.notify("LINK DOWN on ge-0/0/1")
    bus.notify("CPU 95% on core-sw-01")

    unsub_pager()
    bus.notify("MEMORY LOW on fw-main")

    print(f"NOC log:   {noc_log}")
    print(f"Pager log: {pager_log}")
    print(f"Pager missed last alert: {'MEMORY LOW' not in str(pager_log)}")
    return noc_log, pager_log


@app.cell
def _(mo, noc_log, pager_log):
    mo.md(f"""
    **Alert Distribution Results:**\n\n
    - NOC dashboard received **{len(noc_log)}** alerts (all of them)
    - Pager received **{len(pager_log)}** alerts (unsubscribed before the third)

    This is exactly how SNMP trap receivers and syslog forwarders work in production NOCs.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 4: Syslog Severity Decorator (Decorator Design Pattern)

    **Scenario:** Syslog messages have severity levels (0=Emergency … 7=Debug).
    You have a base `LogWriter` that writes plain text. You need a `SeverityDecorator`
    that **wraps** a `LogWriter` and prepends a severity tag to every message —
    without modifying the original class.

    **Theory:**
    *   **Decorator pattern**: Wraps an object to add behaviour. The wrapper has
        the **same interface** as the wrapped object.
    *   The decorator stores a reference to the wrapped object and delegates to it.
    *   `write(msg)` on the decorator transforms `msg`, then calls `self._wrapped.write(...)`.

    **Task:**
    1.  `LogWriter` (provided) — has `write(msg)` that appends to an internal list, and `messages()` that returns the list.
    2.  Implement `SeverityDecorator(wrapped, severity)`:
        *   `write(msg)` → calls `wrapped.write(f"<{severity}> {msg}")`
        *   `messages()` → delegates to `wrapped.messages()`
    3.  Implement `UpperCaseDecorator(wrapped)`:
        *   `write(msg)` → calls `wrapped.write(msg.upper())`
        *   `messages()` → delegates to `wrapped.messages()`
    4.  Decorators can be **stacked**: `UpperCaseDecorator(SeverityDecorator(writer, 3))`.

    ```python
    w = LogWriter()
    d = SeverityDecorator(w, 4)  # severity 4 = Warning
    d.write("Interface flapping on ge-0/0/2")
    d.messages()  # ["<4> Interface flapping on ge-0/0/2"]
    ```
    """)
    return


@app.cell
def _():
    class LogWriter:
        """Base log writer — stores messages in a list. (PROVIDED — do not modify)"""
        def __init__(self):
            self._log = []

        def write(self, msg: str):
            self._log.append(msg)

        def messages(self) -> list[str]:
            return list(self._log)

    class SeverityDecorator:
        """Prepends syslog severity tag to every message.

        Implement:
        - __init__(wrapped, severity): store wrapped writer and severity level
        - write(msg): prepend "<severity> " and delegate to wrapped.write()
        - messages(): delegate to wrapped.messages()
        """
        pass

    class UpperCaseDecorator:
        """Converts every message to uppercase before writing.

        Implement:
        - __init__(wrapped): store wrapped writer
        - write(msg): convert to uppercase and delegate to wrapped.write()
        - messages(): delegate to wrapped.messages()
        """
        pass

    # ── Tests (do not modify) ──
    writer = LogWriter()
    sev = SeverityDecorator(writer, 4)
    sev.write("Interface flapping on ge-0/0/2")
    sev.write("BGP peer 10.0.0.2 down")
    print(f"Severity-tagged: {sev.messages()}")

    writer2 = LogWriter()
    stacked = UpperCaseDecorator(SeverityDecorator(writer2, 1))
    stacked.write("Power supply failure in chassis 0")
    print(f"Stacked (upper+severity): {stacked.messages()}")
    return sev, stacked


@app.cell
def _(mo, sev, stacked):
    _sev_msgs = sev.messages()
    _stacked_msgs = stacked.messages()
    _sev_rows = "\n".join([f"| {i+1} | `{m}` |" for i, m in enumerate(_sev_msgs)])
    _stacked_rows = "\n".join([f"| {i+1} | `{m}` |" for i, m in enumerate(_stacked_msgs)])
    mo.md(
        f"**Severity-tagged messages:**\n\n"
        f"| # | Message |\n"
        f"|---|---|\n"
        f"{_sev_rows}\n\n"
        f"**Stacked decorators (Severity + UpperCase):**\n\n"
        f"| # | Message |\n"
        f"|---|---|\n"
        f"{_stacked_rows}\n\n"
        f"Decorators let you compose logging pipelines without modifying the base writer — "
        f"just like rsyslog filter chains."
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 5: Network Worm Propagation Simulator (Immutable State, `__repr__`)

    **Scenario:** Model a simplified network worm / broadcast storm spreading
    across a row of switches. Each switch is either **infected** (`1`) or
    **clean** (`0`). At each tick, a switch becomes infected if it has
    **exactly one** infected neighbour (mimicking a targeted lateral movement);
    otherwise it becomes/stays clean.

    **Theory:**
    *   **Immutability**: `step()` returns a **new** `NetworkSim` object — the
        original is never modified. This makes it safe to keep history.
    *   **`__repr__`** — unambiguous developer representation.
    *   **`__str__`** — visual representation using `█` (infected) and `·` (clean).

    **Task — implement `NetworkSim`:**
    1.  Constructor takes a `list[int]` of 0s and 1s (the switch row).
    2.  `__str__` → `"█··█·"` style string.
    3.  `__repr__` → `"NetworkSim([1,0,0,1,0])"`.
    4.  `step()` → returns a **new** `NetworkSim` with the next generation.
        *   Rule: a cell becomes `1` if **exactly one** of its neighbours is `1`; else `0`.
        *   Edges wrap around (toroidal).
    5.  `count_infected()` → number of `1`s.
    6.  `is_clean()` → `True` if all cells are `0`.

    ```python
    sim = NetworkSim([0, 0, 1, 0, 0])
    str(sim)            # "··█··"
    sim2 = sim.step()
    str(sim2)           # "·█·█·"
    sim2.count_infected()  # 2
    ```
    """)
    return


@app.cell
def _():
    import time
    return (time,)


@app.cell
def _():
    class NetworkSim:
        """Cellular automaton simulating worm propagation across switches.

        Implement:
        - __init__(state: list[int]): store a copy of the state list
        - __str__: "█" for infected (1), "·" for clean (0)
        - __repr__: "NetworkSim([1, 0, ...])"
        - step(): return NEW NetworkSim; cell=1 if exactly one neighbour is 1, else 0; wrap edges
        - count_infected(): return sum of 1s
        - is_clean(): return True if all 0s
        """
        pass

    # ── Tests (do not modify) ──
    sim = NetworkSim([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    print(f"Initial: {sim}  repr: {repr(sim)}")

    for tick in range(6):
        print(f"Tick {tick}: {sim}  infected={sim.count_infected()}")
        sim = sim.step()

    print(f"Clean? {sim.is_clean()}")
    return (NetworkSim,)


@app.cell
def _(NetworkSim, mo):
    _sim = NetworkSim([0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
    _history = [str(_sim)]
    for _ in range(8):
        _sim = _sim.step()
        _history.append(str(_sim))
    _rows = "\n".join([f"| {i} | `{h}` | {h.count('█')} |" for i, h in enumerate(_history)])
    mo.md(
        f"**Worm propagation over 8 ticks:**\n\n"
        f"| Tick | State | Infected |\n"
        f"|---|---|---|\n"
        f"{_rows}\n\n"
        f"The worm oscillates — just like a real broadcast storm that flaps between switch ports."
    )
    return


@app.cell
def _(NetworkSim, time):
    def run_simulation(sim: NetworkSim, steps: int):
        """Render the propagation simulation for n steps."""
        for i in range(steps):
            print(f"── Tick {i} ──")
            print(sim)
            sim = sim.step()
            time.sleep(0.3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## 🚀 Final Challenge: Data Center Rack Monitor

    **Scenario:** Combine everything into a `DataCenterRack` class that models
    a physical server rack in your data center.

    **Requirements:**
    1.  Constructor takes `rack_id` (str), `location` (str), and `capacity` (int, default 42 — standard rack units).
    2.  Internal list `servers` stores server name strings.
    3.  `add_server(name)` — adds a server; raises `OverflowError` if at capacity.
    4.  `remove_server(name)` — removes a server; raises `ValueError` if not found.
    5.  `__len__` → number of servers currently installed.
    6.  `__contains__(name)` → supports `"web-01" in rack`.
    7.  `__str__` → `"Rack <rack_id> @ <location> [<used>/<capacity>]"`.
    8.  `__iter__` → iterate over installed servers.
    9.  `__eq__` → two racks are equal if same `rack_id`.
    10. `utilization()` → returns float percentage of used capacity.

    ```python
    rack = DataCenterRack("R-101", "Building A, Row 3", 4)
    rack.add_server("web-01")
    rack.add_server("db-01")
    len(rack)           # 2
    "web-01" in rack    # True
    rack.utilization()  # 50.0
    str(rack)           # "Rack R-101 @ Building A, Row 3 [2/4]"
    ```
    """)
    return


@app.cell
def _():
    class DataCenterRack:
        """
        Models a physical server rack with OOP best practices.

        Implement ALL of the following:
        - __init__(rack_id, location, capacity=42): store attributes + empty servers list
        - add_server(name): append to servers, raise OverflowError if full
        - remove_server(name): remove from servers, raise ValueError if not found
        - utilization(): return (used / capacity) * 100 as float
        - __len__: return number of servers
        - __contains__(name): return whether name is in servers
        - __str__: "Rack <rack_id> @ <location> [<used>/<capacity>]"
        - __iter__: yield each server name
        - __eq__: compare by rack_id only, False for non-DataCenterRack
        """
        pass

    # ── Tests (do not modify) ──
    rack = DataCenterRack("R-101", "Building A, Row 3", 4)
    rack.add_server("web-01")
    rack.add_server("web-02")
    rack.add_server("db-01")

    print(f"Rack: {rack}")
    print(f"Servers installed: {len(rack)}")
    print(f"'web-01' in rack → {'web-01' in rack}")
    print(f"'mail-01' in rack → {'mail-01' in rack}")
    print(f"Utilization: {rack.utilization():.1f}%")
    print(f"Iterating: {list(rack)}")

    rack.add_server("cache-01")
    print(f"\nAfter adding cache-01: {rack}")

    try:
        rack.add_server("overflow-01")
    except OverflowError as e:
        print(f"OverflowError: {e}")

    rack.remove_server("web-02")
    print(f"After removing web-02: {rack}")

    try:
        rack.remove_server("ghost-01")
    except ValueError as e:
        print(f"ValueError: {e}")

    rack2 = DataCenterRack("R-101", "Different Location")
    print(f"\nrack == rack2 (same ID) → {rack == rack2}")
    print(f"rack == 'string' → {rack == 'string'}")
    return (rack,)


@app.cell
def _(mo, rack):
    _servers = list(rack)
    _rows = "\n".join([f"| {i+1} | `{s}` |" for i, s in enumerate(_servers)])
    mo.md(
        f"### 🏗️ Data Center Rack Report\n\n"
        f"**{rack}**\n\n"
        f"| # | Server |\n"
        f"|---|---|\n"
        f"{_rows}\n\n"
        f"**Utilization:** {rack.utilization():.1f}%\n\n"
        f"This class could be extended with power monitoring, temperature sensors, "
        f"and SNMP integration — the foundation of any DCIM (Data Center Infrastructure "
        f"Management) system."
    )
    return


if __name__ == "__main__":
    app.run()
