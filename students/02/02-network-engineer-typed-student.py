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
    # 📡 Lab 02: The Network Engineer's Toolkit

    **Duration:** 90 Minutes

    **Focus:** Functions, String Manipulation, File I/O, `*args` / `**kwargs`, List Comprehensions, Generators

    **Context:** Telecommunications & Computer Networks

    ---

    ### 🎯 Objective
    In this session, you will build a collection of utility functions used by network engineers daily — from formatting protocol messages and reading configuration files, to filtering network inventory data. You will practice writing clean, reusable functions and working with files.

    ### 📚 References
    *   [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
    *   [Python File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
    *   [*args and **kwargs](https://realpython.com/python-kwargs-and-args/)
    *   [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
    *   [Generators](https://docs.python.org/3/howto/functional.html#generators)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 1: Protocol Message Framing (Basic Functions & String Ops)

    **Scenario:** In many network protocols (e.g., HDLC, PPP), data frames are delimited by special flag characters. You need to build a simple framing utility that wraps payload strings with delimiter characters — similar to how a data-link layer frames a packet.

    **Theory:**
    *   **Functions**: Encapsulate reusable logic. `def function_name(parameters): ...`
    *   **String concatenation**: `"!" + payload + "!"` wraps a string.
    *   **Calling functions from functions**: Good design means small, composable functions.

    **Task:**
    1.  Complete `frame_payload(payload)` — returns the input string wrapped with leading and closing `~` characters (the HDLC flag byte representation).
    2.  Complete `frame_all_payloads(payload_list)` — takes a list of payload strings and returns a new list where each payload is framed. **Use `frame_payload` inside this function** to keep things modular.
    """)
    return


@app.cell
def _():
    # Data Block - Do not modify
    raw_payloads = [
        "HELLO-PEER",
        "ACK-0x01",
        "DATA:192.168.1.1>10.0.0.1:ICMP-ECHO",
        "FIN-SESSION",
    ]
    return (raw_payloads,)


@app.cell
def _(raw_payloads):
    from typing import Generator

    def frame_payload(payload: str) -> str:
        """
        Returns input string wrapped with leading and closing '~' character (HDLC flag).

        Expected behavior:
          - Prepend '~' and append '~' to the payload string.
          - Example: "HELLO-PEER" -> "~HELLO-PEER~"

        Hint: Use string concatenation.
        """
        # TODO: Implement this function
        ...

    def frame_all_payloads(payload_list: list[str]) -> list[str]:
        """
        Returns a list of framed payload strings.

        Expected behavior:
          - Iterate over payload_list and apply frame_payload() to each element.
          - Return the resulting list.
          - Use a list comprehension for a concise solution.

        Hint: Call frame_payload() for each payload in the list.
        """
        # TODO: Implement this function
        ...

    # Test
    framed = frame_all_payloads(raw_payloads)
    framed
    return Generator, framed


@app.cell
def _(framed, mo):
    mo.md(f"""
    **Framed Payloads:** `{framed}`

    Each payload is now delimited with `~` flags, ready for transmission on the data-link layer.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 2: Network Banner Printer (`*args` & String Joining)

    **Scenario:** When you connect to a network device via SSH or Telnet, it often displays a "Message of the Day" (MOTD) banner. You need a utility function that takes any number of text segments and prints them as a formatted banner with a border.

    **Theory:**
    *   **`*args`**: Allows a function to accept any number of positional arguments. Inside the function, `args` is a tuple.
    *   **`" ".join(iterable)`**: Joins elements of an iterable into a single string separated by spaces.
    *   **`len(string)`**: Returns the length of a string — useful for creating matching-width borders.

    **Task:**
    Complete `motd_banner(*args)` — it should:
    1.  Join all arguments into a single string separated by spaces.
    2.  Print a line of `=` characters matching the length of the joined string.
    3.  Print the joined string.
    4.  Print the `=` border again.
    5.  **Return** the joined string (for testing purposes).

    Example:
    ```
    motd_banner("Unauthorized", "access", "prohibited!")
    ```
    Output:
    ```
    ====
    Unauthorized access prohibited!
    ====
    ```
    """)
    return


@app.cell
def _():
    def motd_banner(*args: str) -> str:
        """
        Prints a formatted MOTD banner from any number of string arguments.
        Returns the joined message string.

        Expected behavior:
          1. Join all args into a single string separated by spaces using " ".join().
          2. Create a border string of '=' characters with the same length as the message.
          3. Print: border, then message, then border (three print() calls).
          4. Return the joined message string.
        """
        # TODO: Implement this function
        ...

    # Test
    result = motd_banner("WARNING:", "This", "is", "a", "restricted", "network", "device.")
    return (result,)


@app.cell
def _(mo, result):
    mo.md(f"""
    **Banner message:** `{result}`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 3: Reading Network Inventory Files (File I/O)

    **Scenario:** Your network operations center (NOC) keeps a plain-text inventory file listing all managed devices — one device per line. You need functions to read this file so you can process the data programmatically.

    **The Data (`devices.txt`):**
    ```
    switch-core-01,10.0.0.1,Cisco,Catalyst 9300
    router-edge-01,10.0.1.1,Juniper,MX204
    ap-floor3-01,10.0.2.10,Ubiquiti,U6-Pro
    firewall-main,10.0.0.254,Palo Alto,PA-450
    switch-access-02,10.0.0.2,Cisco,Catalyst 9200
    ```

    **Theory:**
    *   **Classic file access**: `f = open(filename)` → `f.read()` → `f.close()`. Must handle `FileNotFoundError`.
    *   **`with` statement**: `with open(filename) as f:` — automatically closes the file, even on errors. This is the **preferred** Pythonic way.
    *   **`try / except / finally`**: Exception handling to gracefully deal with missing files.

    **Task:**
    1.  Complete `read_inventory(filename)` using **classic** `open/close` with `try/except/finally`.
    2.  Complete `read_inventory_with(filename)` using the **`with` statement**.
    3.  Both should return the file content as a string, or an error message `"Unable to open file: <filename>"` if the file doesn't exist.
    """)
    return


@app.cell
def _():
    # First, let's create the sample data file for this exercise
    _device_data = """switch-core-01,10.0.0.1,Cisco,Catalyst 9300
    router-edge-01,10.0.1.1,Juniper,MX204
    ap-floor3-01,10.0.2.10,Ubiquiti,U6-Pro
    firewall-main,10.0.0.254,Palo Alto,PA-450
    switch-access-02,10.0.0.2,Cisco,Catalyst 9200
    switch-distro-01,10.0.0.3,Cisco,Catalyst 9500
    router-branch-01,10.0.3.1,MikroTik,CCR2004
    ap-floor1-01,10.0.2.11,Ubiquiti,U6-LR
    ap-floor2-01,10.0.2.12,Ubiquiti,U6-Pro"""

    with open("devices.txt", "w") as f:
        f.write(_device_data)

    print("✅ devices.txt created successfully.")
    return


@app.cell
def _():
    def read_inventory(filename: str) -> str:
        """
        Returns content of a file as a string.
        Uses classic file access with try/except/finally.

        Expected behavior:
          1. Initialize a variable `f` to None and `lines` to the error message
             "Unable to open file: <filename>" (use .format() or f-string).
          2. In a try block: open the file with open(filename, "r"), assign to f,
             then read all content with f.read() into lines.
          3. In an except block: catch FileNotFoundError — lines already has the error message,
             so just pass.
          4. In a finally block: if f is not None, close it with f.close(), then return lines.
        """
        # TODO: Implement this function
        ...

    def read_inventory_with(filename: str) -> str:
        """
        Returns content of a file as a string.
        Uses the with statement for automatic resource management.

        Expected behavior:
          1. Initialize `lines` to the error message "Unable to open file: <filename>".
          2. In a try block: use `with open(filename, "r") as f:` and read content with f.read().
          3. In an except block: catch FileNotFoundError — just pass.
          4. In a finally block: return lines.

        Note: The with statement automatically closes the file — no need for manual f.close().
        """
        # TODO: Implement this function
        ...

    # Test with existing file
    content_classic = read_inventory("devices.txt")
    content_with = read_inventory_with("devices.txt")

    # Test with non-existing file
    content_missing = read_inventory("nonexistent.txt")

    print("=== Classic read ===")
    print(content_classic)
    print("\n=== With-statement read ===")
    print(content_with)
    print("\n=== Missing file ===")
    print(content_missing)
    return


@app.cell
def _(mo):
    mo.md("""
    **Key takeaway:** Both approaches produce the same result, but the `with` statement is cleaner and safer — it guarantees the file handle is closed even if an exception occurs mid-read. In production network scripts, **always prefer `with`**.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 4: Filtering Network Devices (`**kwargs` & List Comprehensions)

    **Scenario:** Your NOC inventory file also contains bandwidth capacity (in Mbps) for each device's uplink. You need a flexible filtering function that can select devices based on bandwidth thresholds — useful for capacity planning and upgrade decisions.

    **The Data (`device_bandwidth.txt`):**
    ```
    switch-core-01,10000
    router-edge-01,40000
    ap-floor3-01,1000
    firewall-main,10000
    switch-access-02,1000
    switch-distro-01,25000
    router-branch-01,2500
    ap-floor1-01,1000
    ap-floor2-01,1000
    ```

    **Theory:**
    *   **`**kwargs`**: Allows a function to accept any number of keyword arguments. Inside the function, `kwargs` is a dictionary.
    *   **Checking for keys**: `if 'gt' in kwargs:` — test if a keyword was provided.
    *   **List comprehension**: `[x for x in items if condition]` — compact filtering.
    *   **Unpacking**: `name, bw = line.split(",")` — assign multiple variables from a split.

    **Task:**
    1.  Complete `filter_devices(filename, **kwargs)` that reads the file and filters devices by bandwidth:
        *   `gt=value` → only devices with bandwidth **greater than** `value`
        *   `lt=value` → only devices with bandwidth **less than** `value`
        *   Both can be specified simultaneously.
        *   If neither is specified, return an empty list.
    2.  Use **list comprehension** for the filtering step.
    3.  Use **unpacking** when parsing each line.
    """)
    return


@app.cell
def _():
    # Create the bandwidth data file
    _bw_data = """switch-core-01,10000
    router-edge-01,40000
    ap-floor3-01,1000
    firewall-main,10000
    switch-access-02,1000
    switch-distro-01,25000
    router-branch-01,2500
    ap-floor1-01,1000
    ap-floor2-01,1000"""

    with open("device_bandwidth.txt", "w") as g:
        g.write(_bw_data)

    print("✅ device_bandwidth.txt created successfully.")
    return


@app.cell
def _():
    def filter_devices(filename: str, **kwargs: int) -> list[tuple[str, int]]:
        """
        Returns a list of (device_name, bandwidth) tuples that match the given criteria.
        Keyword arguments:
          gt: only devices with bandwidth greater than this value
          lt: only devices with bandwidth less than this value
        If no keyword arguments are given, returns an empty list.

        Expected behavior:
          1. If kwargs is empty, return [].
          2. Read the file using `with open(...)`. If FileNotFoundError, return [].
          3. Parse each line by splitting on ',' and unpacking into name and bw.
             Strip whitespace and convert bw to int. Collect into a list of (name, bw) tuples.
          4. If 'gt' is in kwargs, filter the list using a list comprehension to keep
             only tuples where bw > kwargs["gt"].
          5. If 'lt' is in kwargs, filter the list using a list comprehension to keep
             only tuples where bw < kwargs["lt"].
          6. Return the filtered list.
        """
        # TODO: Implement this function
        ...

    # Tests
    print("=== Devices with bandwidth > 10 Gbps (10000 Mbps) ===")
    high_bw = filter_devices("device_bandwidth.txt", gt=10000)
    for name, bw in high_bw:
        print(f"  {name}: {bw} Mbps")

    print("\n=== Devices with bandwidth < 2000 Mbps ===")
    low_bw = filter_devices("device_bandwidth.txt", lt=2000)
    for name, bw in low_bw:
        print(f"  {name}: {bw} Mbps")

    print("\n=== Devices between 2000 and 30000 Mbps ===")
    mid_bw = filter_devices("device_bandwidth.txt", gt=2000, lt=30000)
    for name, bw in mid_bw:
        print(f"  {name}: {bw} Mbps")

    print("\n=== No filter (should be empty) ===")
    no_filter = filter_devices("device_bandwidth.txt")
    print(f"  Result: {no_filter}")
    return (filter_devices,)


@app.cell
def _(filter_devices, mo):
    _high = filter_devices("device_bandwidth.txt", gt=10000)
    _low = filter_devices("device_bandwidth.txt", lt=2000)

    mo.vstack([
        mo.md(f"**High-bandwidth devices (>10 Gbps):** {len(_high)} found"),
        mo.md(f"**Low-bandwidth devices (<2 Gbps):** {len(_low)} found — candidates for upgrade 🔧"),
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 5: Generator-Based Log Streaming (Generators & `yield`)

    **Scenario:** In a real telecom NOC, log files can be enormous — gigabytes of syslog data. Loading everything into memory at once is impractical. Instead, you use **generators** to process logs line-by-line, yielding only the entries you care about.

    **Theory:**
    *   **Generator function**: A function that uses `yield` instead of `return`. It produces values one at a time, on demand.
    *   **Lazy evaluation**: The generator doesn't compute the next value until you ask for it (e.g., with `next()` or a `for` loop).
    *   **Memory efficiency**: Only one line is in memory at a time — critical for large-scale network monitoring.

    **Task:**
    1.  Reimplement the device filter from Part 4 as a **generator** function `filter_devices_gen(filename, **kwargs)`.
    2.  Instead of building a list and returning it, **`yield`** each matching device one at a time.
    3.  Demonstrate that you can iterate over the generator with a `for` loop.
    """)
    return


@app.cell
def _(Generator):
    def filter_devices_gen(filename: str, **kwargs: int) -> Generator[tuple[str, int], None, None]:
        """
        Generator version of filter_devices.
        Yields (device_name, bandwidth) tuples one at a time.

        Expected behavior:
          1. If kwargs is empty, return immediately (use bare `return`).
          2. Open the file with `with open(...)` inside a try block.
          3. Iterate over lines in the file. For each line:
             a. Strip whitespace. Skip empty lines with `continue`.
             b. Split on ',' and unpack into name and bw. Strip and convert bw to int.
             c. If 'gt' is in kwargs and bw <= kwargs["gt"], skip this line (continue).
             d. If 'lt' is in kwargs and bw >= kwargs["lt"], skip this line (continue).
             e. If the line passed all filters, `yield (name, bw)`.
          4. Catch FileNotFoundError and return.

        Key difference from filter_devices: use `yield` instead of appending to a list.
        This makes the function a generator — it produces values lazily, one at a time.
        """
        # TODO: Implement this function
        ...

    # Demonstrate generator usage
    print("=== Streaming high-bandwidth devices (generator) ===")
    gen = filter_devices_gen("device_bandwidth.txt", gt=5000)
    print(f"Generator object: {gen}")
    print(f"Type: {type(gen)}")
    print()

    for device_name, bandwidth in gen:
        print(f"  📡 {device_name}: {bandwidth} Mbps")

    print("\n=== Generator is now exhausted — no more values ===")
    remaining = list(filter_devices_gen("device_bandwidth.txt", gt=5000))
    # But creating a new generator works fine:
    print(f"  Fresh generator produces: {len(remaining)} items")
    return


@app.cell
def _(mo):
    mo.md("""
    **Key insight:** The generator reads the file line-by-line and yields matches immediately. For a 10 GB log file, memory usage stays constant — only one line is processed at a time. This is how real network monitoring tools (like `tcpdump` piped through Python) work.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## 🚀 Final Challenge: The Telecom Inventory Auditor

    **Scenario:** You are a network engineer preparing for a quarterly audit. You have the device inventory file and the bandwidth file. You need to produce a comprehensive audit report that:

    1.  Reads both files.
    2.  Merges the data by device name.
    3.  Classifies each device into a **tier** based on bandwidth.
    4.  Identifies devices that need attention (low bandwidth APs, unknown vendors, etc.).
    5.  Produces a formatted summary report.

    **Tier Classification:**
    *   **Backbone** (>= 25000 Mbps)
    *   **Distribution** (>= 5000 Mbps and < 25000 Mbps)
    *   **Access** (>= 1000 Mbps and < 5000 Mbps)
    *   **Legacy** (< 1000 Mbps)

    **This task combines everything from this lab:**
    *   Functions & modularity (Part 1)
    *   `*args` for flexible output (Part 2)
    *   File I/O with `with` (Part 3)
    *   `**kwargs` filtering (Part 4)
    *   Generator thinking (Part 5)

    **Task:**
    Complete `generate_audit_report()` that returns a dictionary:
    ```python
    {
        "total_devices": int,
        "tier_summary": {"Backbone": int, "Distribution": int, "Access": int, "Legacy": int},
        "devices_by_vendor": {"Cisco": [names], "Juniper": [names], ...},
        "upgrade_candidates": [list of device names with bandwidth < 2000],
        "missing_bandwidth_data": [devices in inventory but not in bandwidth file],
    }
    ```
    """)
    return


@app.cell
def _():
    from typing import Any

    def parse_inventory_file(filename: str) -> dict[str, dict[str, str]]:
        """
        Reads devices.txt and returns a dict: {device_name: {"ip": ..., "vendor": ..., "model": ...}}

        Expected behavior:
          1. Initialize an empty dict `devices`.
          2. Open the file with `with open(...)`. Catch FileNotFoundError and print an error.
          3. For each line: strip whitespace, skip empty lines, split on ','.
          4. Use parts[0] as the device name (key). Store a dict with keys
             "ip" (parts[1]), "vendor" (parts[2]), "model" (parts[3]) — all stripped.
          5. Return the devices dict.
        """
        # TODO: Implement this function
        ...

    def parse_bandwidth_file(filename: str) -> dict[str, int]:
        """
        Reads device_bandwidth.txt and returns a dict: {device_name: bandwidth_mbps}

        Expected behavior:
          1. Initialize an empty dict `bandwidths`.
          2. Open the file with `with open(...)`. Catch FileNotFoundError and print an error.
          3. For each line: strip whitespace, skip empty lines, split on ',' and unpack
             into name and bw. Strip both, convert bw to int.
          4. Store bandwidths[name] = bw.
          5. Return the bandwidths dict.
        """
        # TODO: Implement this function
        ...

    def classify_tier(bandwidth_mbps: int) -> str:
        """
        Returns the tier name based on bandwidth.

        Expected behavior:
          - >= 25000 -> "Backbone"
          - >= 5000 and < 25000 -> "Distribution"
          - >= 1000 and < 5000 -> "Access"
          - < 1000 -> "Legacy"

        Use if/elif/else chain.
        """
        # TODO: Implement this function
        ...

    def generate_audit_report(
        inventory_file: str = "devices.txt",
        bandwidth_file: str = "device_bandwidth.txt",
    ) -> dict[str, Any]:
        """
        Generates a comprehensive network audit report.

        Expected behavior:
          1. Call parse_inventory_file() and parse_bandwidth_file() to read both files.
          2. Initialize the report dict with keys:
             - "total_devices": len(inventory)
             - "tier_summary": {"Backbone": 0, "Distribution": 0, "Access": 0, "Legacy": 0}
             - "devices_by_vendor": {}
             - "upgrade_candidates": []
             - "missing_bandwidth_data": []
          3. For each device in inventory:
             a. Group by vendor: add device name to report["devices_by_vendor"][vendor] list.
             b. If device has bandwidth data:
                - Classify its tier with classify_tier() and increment the tier count.
                - If bandwidth < 2000, add to upgrade_candidates.
             c. If device has NO bandwidth data, add to missing_bandwidth_data.
          4. Return the report dict.
        """
        # TODO: Implement this function
        ...

    audit = generate_audit_report()
    return Any, audit


@app.cell
def _(audit, mo):
    _tier = audit["tier_summary"]
    _vendors = audit["devices_by_vendor"]
    _vendor_rows = "\n".join(
        [f"    | {v} | {len(devs)} | {', '.join(devs)} |" for v, devs in _vendors.items()]
    )

    mo.vstack([
        mo.md(f"""
    ### 📊 Quarterly Network Audit Report

    **Total managed devices:** {audit["total_devices"]}

    #### Tier Summary
    | Tier | Count |
    |----|----|
    | 🔴 Backbone (≥25 Gbps) | {_tier["Backbone"]} |
    | 🟠 Distribution (≥5 Gbps) | {_tier["Distribution"]} |
    | 🟢 Access (≥1 Gbps) | {_tier["Access"]} |
    | ⚪ Legacy (<1 Gbps) | {_tier["Legacy"]} |

    #### Vendor Distribution
    | Vendor | Count | Devices |
    |----|----|----|
    {_vendor_rows}

    #### ⚠️ Upgrade Candidates (bandwidth < 2 Gbps)
    {', '.join(audit['upgrade_candidates']) if audit['upgrade_candidates'] else 'None — all devices meet minimum bandwidth.'}

    #### ❓ Missing Bandwidth Data
    {', '.join(audit['missing_bandwidth_data']) if audit['missing_bandwidth_data'] else 'None — all devices have bandwidth records.'}
        """),
        mo.json(audit)
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Want More?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Part 6: Packet Header Parser (String Slicing & Hex)

    **Scenario:** You intercepted a simplified representation of an IPv4 packet header as a hex string. You need to extract key fields: version, header length, TTL, protocol, source IP, and destination IP.

    **The Data:**
    A simplified hex string representing selected IPv4 header fields:
    `"45 00 00 3c 40 11 c0a80101 c0a80102"`

    Format: `VERSION_IHL TOS TOTAL_LEN TTL PROTO SRC_IP DST_IP`

    **Theory:**
    *   **Hex to int**: `int("45", 16)` → `69`. The high nibble (`4`) is the version, the low nibble (`5`) is the IHL.
    *   **Bitwise operations**: `value >> 4` shifts right by 4 bits (extracts high nibble). `value & 0x0F` masks the low nibble.
    *   **IP from hex**: `"c0a80101"` → split into 2-char chunks → convert each to int → join with dots → `"192.168.1.1"`.

    **Task:**
    Complete `parse_ipv4_header(header_str)` that returns a dictionary with the parsed fields.
    """)
    return


@app.cell
def _():
    # Data Block - Do not modify
    sample_headers = [
        "45 00 00 3c 40 06 c0a80101 0a00001",
        "45 00 00 28 80 11 0a0a0a01 c0a80201",
        "46 00 01 00 01 01 7f00001 7f00001",
    ]
    return (sample_headers,)


@app.cell
def _(sample_headers):
    def hex_to_ip(hex_str: str) -> str:
        """
        Converts an 8-character hex string to dotted-decimal IP.
        Example: "c0a80101" -> "192.168.1.1"

        Expected behavior:
          1. Split the hex string into 4 chunks of 2 characters each (indices 0:2, 2:4, 4:6, 6:8).
          2. Convert each 2-char hex chunk to an integer with int(chunk, 16).
          3. Convert each integer to a string.
          4. Join the four strings with '.' and return.

        Hint: Use a list comprehension with range(0, 8, 2) for slicing.
        """
        # TODO: Implement this function
        ...

    def protocol_name(proto_num: int) -> str:
        """
        Maps common protocol numbers to names.

        Expected behavior:
          - Create a dict mapping: {1: "ICMP", 6: "TCP", 17: "UDP"}
          - Return the name for the given number, or "OTHER(<number>)" if not found.

        Hint: Use dict.get() with a default value.
        """
        # TODO: Implement this function
        ...

    def parse_ipv4_header(header_str: str) -> dict[str, int | str]:
        """
        Parses a simplified IPv4 header hex string.
        Returns a dict with: version, ihl, ttl, protocol, src_ip, dst_ip

        Expected behavior:
          1. Split header_str on spaces into parts.
          2. Parse the first byte (parts[0]) as hex int:
             - version = first_byte >> 4 (high nibble)
             - ihl = first_byte & 0x0F (low nibble)
          3. TTL = int(parts[3], 16)
          4. Protocol = int(parts[5], 16), then map with protocol_name().
          5. Source IP = hex_to_ip(parts[6])
          6. Destination IP = hex_to_ip(parts[7])
          7. Return dict with keys: "version", "ihl", "ttl", "protocol", "src_ip", "dst_ip".
        """
        # TODO: Implement this function
        ...

    parsed_headers = [parse_ipv4_header(h) for h in sample_headers]
    for i, ph in enumerate(parsed_headers):
        print(f"Packet {i+1}: {ph}")
    return (parsed_headers,)


@app.cell
def _(mo, parsed_headers):
    _rows = "\n".join([
        f"| {i+1} | IPv{p['version']} | {p['ihl']} | {p['ttl']} | {p['protocol']} | `{p['src_ip']}` | `{p['dst_ip']}` |"
        for i, p in enumerate(parsed_headers)
    ])

    mo.md(f"""
    ### 📦 Parsed IPv4 Headers

    | # | Version | IHL | TTL | Protocol | Source IP | Destination IP |
    |---|----|----|----|----|----|---|
    {_rows}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Part 7: Routing Table Analyzer (Nested Data & Longest Prefix Match)

    **Scenario:** You have a simplified routing table and need to determine which next-hop a packet should be forwarded to, based on the **longest prefix match** algorithm — the fundamental forwarding decision in IP routing.

    **The Data:**
    A routing table as a list of tuples: `(network_cidr, next_hop_ip, interface)`

    **Theory:**
    *   **`ipaddress` module**: `ip_address()` and `ip_network()` for proper IP handling.
    *   **Longest Prefix Match**: When multiple routes match a destination, the one with the longest subnet mask (most specific) wins.
    *   **`network.prefixlen`**: The prefix length (e.g., `/24` → 24). Higher = more specific.

    **Task:**
    1.  Complete `longest_prefix_match(dest_ip, routing_table)` — returns the best matching route (the one with the longest prefix) or a default message.
    2.  Complete `trace_routes(destinations, routing_table)` — returns a list of `(destination, matched_route)` tuples.
    """)
    return


@app.cell
def _():
    import ipaddress as ipaddr
    return (ipaddr,)


@app.cell
def _():
    # Data Block - Do not modify
    routing_table = [
        ("10.0.0.0/8", "172.16.0.1", "eth0"),
        ("10.0.1.0/24", "172.16.0.2", "eth1"),
        ("10.0.1.128/25", "172.16.0.3", "eth2"),
        ("192.168.0.0/16", "172.16.0.4", "eth3"),
        ("0.0.0.0/0", "172.16.0.254", "eth0"),  # Default route
    ]

    test_destinations = [
        "10.0.1.200",   # Should match /25 (most specific)
        "10.0.1.50",    # Should match /24
        "10.0.5.5",     # Should match /8
        "192.168.1.1",  # Should match /16
        "8.8.8.8",      # Should match default route
    ]
    return routing_table, test_destinations


@app.cell
def _(ipaddr, routing_table, test_destinations):
    def longest_prefix_match(
        dest_ip_str: str,
        rtable: list[tuple[str, str, str]],
    ) -> tuple[str, str, str, int] | None:
        """
        Finds the best (longest prefix) matching route for a destination IP.
        Returns: (network, next_hop, interface, prefix_length) or None

        Expected behavior:
          1. Convert dest_ip_str to an ip_address object using ipaddr.ip_address().
          2. Initialize best_match = None and best_prefix_len = -1.
          3. For each (network_cidr, next_hop, interface) in rtable:
             a. Convert network_cidr to an ip_network object using ipaddr.ip_network().
             b. Check if dest is in the network (`dest in network`).
             c. If it matches AND network.prefixlen > best_prefix_len:
                - Update best_match to (network_cidr, next_hop, interface, network.prefixlen).
                - Update best_prefix_len.
          4. Return best_match (could be None if nothing matched).
        """
        # TODO: Implement this function
        ...

    def trace_routes(
        destinations: list[str],
        rtable: list[tuple[str, str, str]],
    ) -> list[tuple[str, tuple[str, str, str, int] | None]]:
        """
        For each destination IP, find the best matching route.
        Returns: [(dest_ip, match_result), ...]

        Expected behavior:
          1. Initialize an empty results list.
          2. For each dest in destinations:
             a. Call longest_prefix_match(dest, rtable).
             b. Append (dest, match_result) to results.
          3. Return results.
        """
        # TODO: Implement this function
        ...

    def print_route_results(
        route_results: list[tuple[str, tuple[str, str, str, int] | None]],
    ) -> None:
        for dest, match in route_results:
            if match:
                net, nh, iface, plen = match
                print(f"{dest} -> via {nh} ({iface}), matched {net} [/{plen}]")
            else:
                print(f"{dest} -> NO ROUTE")

    route_results = trace_routes(test_destinations, routing_table)
    print_route_results(route_results)
    return (route_results,)


@app.cell
def _(mo, route_results):
    _rows = []
    for dest, match in route_results:
        if match:
            net, nh, iface, plen = match
            _rows.append(f"| `{dest}` | `{net}` | `{nh}` | `{iface}` |")
        else:
            _rows.append(f"| `{dest}` | NO MATCH | — | — |")

    mo.md(f"""
    ### 🗺️ Routing Decision Table

    | Destination | Matched Route | Next Hop | Interface |
    |----|----|----|----|
    {chr(10).join(_rows)}

    The longest prefix match ensures the most specific route is always preferred — just like a real router's forwarding engine.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## 🏆 Part 8: Boss Level — Network Topology Discovery Report

    **Scenario:** You are building an automated network discovery tool. You have three data sources:
    1.  **Device inventory** (devices.txt) — device names, IPs, vendors, models.
    2.  **Bandwidth data** (device_bandwidth.txt) — uplink capacity per device.
    3.  **Link data** — which devices are connected to which (adjacency information).

    You must correlate all three sources and produce a topology report.

    **This task combines everything:**
    *   Functions & modularity (Parts 1–2)
    *   File I/O (Part 3)
    *   Filtering with `**kwargs` (Part 4)
    *   Generator thinking (Part 5)
    *   Data parsing (Part 6)
    *   Routing/network logic (Part 7)

    **Task:**
    Produce a `topology_report` dictionary:
    ```python
    {
        "total_devices": int,
        "total_links": int,
        "most_connected_device": {"name": str, "connections": int},
        "bottleneck_links": [{"from": str, "to": str, "bandwidth": int}],
        "isolated_devices": [str],  # devices with no links
        "vendor_summary": {"Cisco": int, ...},
    }
    ```

    A **bottleneck link** is any link where the minimum bandwidth of the two endpoints is below 5000 Mbps.
    """)
    return


@app.cell
def _():
    # Data Block - Do not modify
    # Adjacency list: (device_a, device_b)
    link_data = [
        ("switch-core-01", "switch-distro-01"),
        ("switch-core-01", "router-edge-01"),
        ("switch-core-01", "firewall-main"),
        ("switch-distro-01", "switch-access-02"),
        ("switch-distro-01", "ap-floor1-01"),
        ("switch-distro-01", "ap-floor2-01"),
        ("switch-distro-01", "ap-floor3-01"),
        ("router-edge-01", "router-branch-01"),
    ]
    return (link_data,)


@app.cell
def _(Any, link_data):
    def build_topology_report(
        inventory_file: str,
        bandwidth_file: str,
        links: list[tuple[str, str]],
    ) -> dict[str, Any]:
        """
        Correlates device inventory, bandwidth data, and link information
        to produce a comprehensive topology report.

        Expected behavior:
          Step 1: Read inventory file.
            - Open inventory_file, parse each line into (name, {ip, vendor, model}).
            - Store in a dict: inventory[name] = {"ip": ..., "vendor": ..., "model": ...}
            - If file not found, return {"error": "Missing file: <filename>"}.

          Step 2: Read bandwidth file.
            - Open bandwidth_file, parse each line into (name, bandwidth_int).
            - Store in a dict: bandwidths[name] = bw
            - If file not found, return {"error": "Missing file: <filename>"}.

          Step 3: Build adjacency count.
            - For each (dev_a, dev_b) in links, increment connection_count for both devices.
            - Use dict.get(key, 0) + 1 pattern.

          Step 4: Find most connected device.
            - Use max() on connection_count with key=connection_count.get.
            - Store as {"name": ..., "connections": int}.

          Step 5: Find bottleneck links.
            - For each link (dev_a, dev_b), get bandwidth of both endpoints from bandwidths dict
              (default 0 if missing).
            - If min(bw_a, bw_b) < 5000, add {"from": dev_a, "to": dev_b, "bandwidth": min_bw}
              to the bottleneck list.

          Step 6: Find isolated devices.
            - Build a set of all devices that appear in any link.
            - Any device in inventory but NOT in that set is isolated.
            - Use a list comprehension.

          Step 7: Vendor summary.
            - Count devices per vendor from inventory.
            - Use dict.get(key, 0) + 1 pattern.

          Return dict with keys: total_devices, total_links, most_connected_device,
          bottleneck_links, isolated_devices, vendor_summary.
        """
        # TODO: Implement this function
        ...

    topology_report = build_topology_report("devices.txt", "device_bandwidth.txt", link_data)
    return (topology_report,)


@app.cell
def _(mo, topology_report):
    _mc = topology_report["most_connected_device"]
    _bn = topology_report["bottleneck_links"]
    _iso = topology_report["isolated_devices"]
    _vs = topology_report["vendor_summary"]

    _bn_rows = "\n".join([
        f"| `{b['from']}` | `{b['to']}` | {b['bandwidth']} Mbps |"
        for b in _bn
    ]) if _bn else "| — | — | No bottlenecks detected |"

    _vs_rows = "\n".join([
        f"| {v} | {c} |" for v, c in _vs.items()
    ])

    mo.vstack([
        mo.md(f"""
    ### 🌐 Network Topology Discovery Report

    | Metric | Value |
    |----|----|
    | Total Devices | {topology_report['total_devices']} |
    | Total Links | {topology_report['total_links']} |
    | Most Connected | `{_mc['name']}` ({_mc['connections']} links) |
    | Isolated Devices | {len(_iso)} |

    #### 🔴 Bottleneck Links (< 5 Gbps)
    | From | To | Min Bandwidth |
    |----|----|---|
    {_bn_rows}

    #### 🏭 Vendor Distribution
    | Vendor | Device Count |
    |----|----|
    {_vs_rows}

    #### 🏝️ Isolated Devices (no links)
    {', '.join(_iso) if _iso else 'None — all devices are connected.'}
        """),
        mo.json(topology_report)
    ])
    return


if __name__ == "__main__":
    app.run()
