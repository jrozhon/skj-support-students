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
    # 🕵️‍♀️ Lab 01: The Forensic Log Parser

    **Duration:** 90 Minutes

    **Focus:** String Manipulation, Dictionaries, Lists, Logic Flow

    **Context:** System Administration & Security Analysis

    ---

    ### 🎯 Objective
    In this session, you will build a set of tools to parse raw server logs. You will deal with messy text data from web servers, firewalls, and DHCP services to extract actionable intelligence.

    ### 📚 References
    *   [Python String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods) (split, strip, find)
    *   [Python Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
    *   [f-strings](https://realpython.com/python-f-strings/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 1: Web Traffic Analysis (Nginx Logs)

    **Scenario:** You have access logs from an Nginx web server. You need to identify which IP addresses are generating "Client Errors" (4xx status codes).

    **The Data:**
    Standard Nginx Combined Format looks like this:
    `192.168.1.15 - - [10/Oct/2023:13:55:36] "GET /admin HTTP/1.1" 403 1043`

    **Theory:**
    *   **`str.split()`**: Breaks a string into a list based on whitespace.
    *   **Indexing**: Accessing parts of a list (e.g., `parts[8]` is usually the status code).
    *   **Type Casting**: Converting string `"404"` to integer `404`.

    **Task:**
    1.  Complete `parse_nginx_line` to extract the **IP** and **Status Code**.
    2.  Complete `find_404_offenders` to return a list of IPs that triggered a 404 error.
    """)
    return


@app.cell
def _():
    # Raw Data Block - Do not modify
    nginx_logs = [
        '10.0.0.5 - - [12/Oct/2023:10:00:01] "GET /index.html HTTP/1.1" 200 512',
        '192.168.1.105 - - [12/Oct/2023:10:00:02] "GET /secret.txt HTTP/1.1" 404 124',
        '45.33.22.11 - - [12/Oct/2023:10:00:05] "POST /login HTTP/1.1" 401 0',
        '10.0.0.5 - - [12/Oct/2023:10:00:10] "GET /style.css HTTP/1.1" 200 1024',
        '172.16.0.55 - - [12/Oct/2023:10:00:15] "GET /missing.jpg HTTP/1.1" 404 124',
    ]
    return (nginx_logs,)


@app.cell
def _(nginx_logs):
    def parse_nginx_line(log_line):
        """
        Parses a single log line.
        Returns a tuple: (ip_address, status_code)
        """
        # TODO: Split the log line by whitespace into parts
        # TODO: Extract the IP address from the first element
        # TODO: Extract the status code from index 7 and convert it to an integer
        # TODO: Return a tuple of (ip, status)
        pass

    def find_404_offenders(logs):
        offenders = []
        # TODO: Iterate over each log line
        # TODO: Use parse_nginx_line to get the IP and status code
        # TODO: If the status code is 404, append the IP to the offenders list
        return offenders

    # Test
    offenders_found = find_404_offenders(nginx_logs)
    return (offenders_found,)


@app.cell
def _(mo, offenders_found):
    mo.md(f"""
    **Analysis Result:** The following IPs tried to access missing files: `{offenders_found}`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 2: Firewall Intrusion Detection (Nftables/Syslog)

    **Scenario:** Your firewall (nftables) logs dropped packets to syslog. You need to detect if someone is trying to brute-force SSH (Port 22).

    **The Data:**
    `Oct 12 10:00:01 server kernel: [123.45] IN=eth0 OUT= MAC=... SRC=192.168.1.55 DST=10.0.0.1 PROTO=TCP SPT=54321 DPT=22`

    **Theory:**
    *   **String Slicing/Searching**: `if "DPT=22" in line:` is a quick way to filter.
    *   **Parsing Key-Value pairs**: The log format is messy. You might need to iterate through parts to find the one starting with `SRC=`.

    **Task:**
    Complete `analyze_firewall_logs`. It should return a list of **Source IPs** (`SRC=...`) that were blocked while trying to access **Destination Port 22** (`DPT=22`).
    """)
    return


@app.cell
def _():
    firewall_logs = [
        "Oct 12 10:00:01 srv kernel: IN=eth0 SRC=1.2.3.4 DST=10.0.0.1 PROTO=TCP DPT=22",
        "Oct 12 10:00:02 srv kernel: IN=eth0 SRC=5.6.7.8 DST=10.0.0.1 PROTO=TCP DPT=80",
        "Oct 12 10:00:03 srv kernel: IN=eth0 SRC=1.2.3.4 DST=10.0.0.1 PROTO=TCP DPT=22",
        "Oct 12 10:00:04 srv kernel: IN=eth0 SRC=9.9.9.9 DST=10.0.0.1 PROTO=UDP DPT=53",
        "Oct 12 10:00:05 srv kernel: IN=eth0 SRC=11.22.33.44 DST=10.0.0.1 PROTO=TCP DPT=22"
    ]
    return (firewall_logs,)


@app.cell
def _(firewall_logs):
    def extract_src_ip(log_line):
        """
        Helper function to find 'SRC=x.x.x.x' in a string and return just the IP.
        """
        # TODO: Split the log line into parts
        # TODO: Iterate through parts and find the one starting with "SRC="
        # TODO: Strip the "SRC=" prefix and return just the IP address
        # TODO: Return None if no SRC= field is found
        pass

    def analyze_ssh_attempts(logs):
        attackers = []
        # TODO: Iterate over each log line
        # TODO: Check if the line contains "DPT=22"
        # TODO: If so, use extract_src_ip to get the source IP and append it to attackers
        return attackers

    ssh_attackers = analyze_ssh_attempts(firewall_logs)
    return (ssh_attackers,)


@app.cell
def _(mo, ssh_attackers):
    mo.md(f"""
    **Security Alert:** Detected SSH attempts from: `{ssh_attackers}`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 3: DHCP Lease Tracking (Dictionaries)

    **Scenario:** You are auditing a `dnsmasq` DHCP server. You want to know the current IP address assigned to specific MAC addresses.

    **The Data:**
    `Oct 12 14:00:00 dnsmasq-dhcp[123]: DHCPACK(eth0) 192.168.1.50 00:11:22:33:44:55 android-phone`

    **Theory:**
    *   **Dictionaries as State**: We can use a dictionary to store the *latest* known state. `leases[mac_address] = ip_address`.
    *   **Overwriting**: If a MAC gets a new IP, the dictionary automatically updates the value for that key.

    **Task:**
    Process the logs to build a `lease_db` dictionary where Keys are MAC addresses and Values are IP addresses.
    """)
    return


@app.cell
def _():
    dhcp_logs = [
        "dnsmasq-dhcp: DHCPACK(eth0) 192.168.1.10 00:11:22:33:44:55 workstation-01",
        "dnsmasq-dhcp: DHCPACK(eth0) 192.168.1.11 AA:BB:CC:DD:EE:FF printer-lobby",
        "dnsmasq-dhcp: DHCPACK(eth0) 192.168.1.12 00:11:22:33:44:55 workstation-01", # Re-assigned new IP
        "dnsmasq-dhcp: DHCPACK(eth0) 192.168.1.50 12:34:56:78:90:AB guest-iphone"
    ]
    return (dhcp_logs,)


@app.cell
def _(dhcp_logs):
    def build_lease_db(logs):
        leases = {} # Key: MAC, Value: IP
        # TODO: Iterate over each log line
        # TODO: Split the line into parts
        # TODO: Extract the IP address (index 2) and MAC address (index 3)
        # TODO: Store/overwrite the MAC -> IP mapping in the leases dictionary
        return leases

    current_leases = build_lease_db(dhcp_logs)
    return (current_leases,)


@app.cell
def _(current_leases, mo):
    mo.vstack([
        mo.md("**Current DHCP Leases:**"),
        mo.json(current_leases)
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 4: Advanced Logic - The "Noisy Neighbor" Detector

    **Scenario:** A single IP address might be spamming your server. You want to count how many times each IP appears in the logs and flag anyone who appears more than `threshold` times.

    **Theory:**
    *   **Counting with Dictionaries**: Iterate through items. If key exists, `count += 1`. If not, `count = 1`.
    *   **Filtering Dictionaries**: Creating a new list based on dictionary values.

    **Task:**
    1.  Count occurrences of every IP in the provided list.
    2.  Return a dictionary of IPs that exceeded the threshold.
    """)
    return


@app.function
def find_noisy_neighbors(ip_list, threshold):
    counts = {}

    # Step 1: Count them
    # TODO: Iterate over each IP in ip_list
    # TODO: If the IP is already in counts, increment its count by 1
    # TODO: Otherwise, initialize its count to 1

    # Step 2: Filter them
    banned_ips = {}
    # TODO: Iterate over counts.items()
    # TODO: If the count exceeds the threshold, add the IP and its count to banned_ips

    return banned_ips


@app.cell
def _(mo):
    # Simulated traffic stream
    traffic_stream = [
        "10.0.0.1", "10.0.0.2", "10.0.0.1", "10.0.0.5", 
        "10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.1"
    ]

    noisy = find_noisy_neighbors(traffic_stream, threshold=3)
    mo.vstack([
        mo.md(f"**Traffic Analysis:** Found {len(noisy)} noisy IPs."),
        mo.json(noisy)
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## 🚀 Final Challenge: The SysAdmin Dashboard

    **Task:** You are given a raw multi-line string containing a mix of system messages. You must parse it and produce a summary report.

    **Input:** A single long string with newlines (`
    `).
    **Output:** A dictionary with:
    *   `error_count`: Total number of lines containing "ERROR".
    *   `users`: A list of unique users who logged in (lines containing "Accepted password for...").
    *   `services`: A list of unique services mentioned (the text before the colon, e.g., `sshd`, `nginx`).

    **Hint:**
    1.  Use `raw_log.strip().split('
    ')` to get a list of lines.
    2.  Use `set()` to keep users and services unique.
    """)
    return


@app.cell
def _():
    raw_system_log = """
    sshd[123]: Accepted password for user root from 192.168.1.5
    nginx[456]: ERROR: Connection timed out
    sshd[124]: Accepted password for user alice from 10.0.0.2
    kernel: [1234.55] USB device disconnected
    nginx[456]: ERROR: Worker process died
    cron[789]: Starting daily backup
    sshd[125]: Accepted password for user root from 192.168.1.6
    """

    def generate_dashboard(raw_log):
        report = {
            "error_count": 0,
            "users": [],
            "services": []
        }

        unique_users = set()
        unique_services = set()

        # TODO: Strip the raw log and split it into individual lines

        # TODO: For each line (stripped of whitespace):
        #   1. Count Errors: If the line contains "ERROR", increment report["error_count"]
        #   2. Extract Service Name:
        #      - If the line contains "[", take everything before the first "[" as the service name
        #      - Otherwise if it contains ":", take everything before the first ":" as a fallback
        #      - Add the service name to unique_services
        #   3. Extract Users:
        #      - If the line contains "Accepted password for user", split the line
        #      - Find the word after "user" and add it to unique_users

        # TODO: Convert unique_users and unique_services sets to lists and store in report
        return report
    return generate_dashboard, raw_system_log


@app.cell
def _(generate_dashboard, mo, raw_system_log):
    dashboard = generate_dashboard(raw_system_log)

    mo.vstack([
        mo.md("### 📊 System Dashboard Generated"),
        mo.json(dashboard)
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

    ## Part 5: Subnet Membership Checker (The `ipaddress` Module)

    **Scenario:** Your company uses several VLANs. You need to classify IPs from logs into their respective subnets to determine which department generated the traffic.

    **The Data:**
    A list of IPs and a mapping of subnet → department name.

    **Theory:**
    *   **`ipaddress` module**: Python's standard library for working with IPs and networks.
    *   `ipaddress.ip_address("10.0.0.5")` creates an address object.
    *   `ipaddress.ip_network("10.0.0.0/24")` creates a network object.
    *   The `in` operator works: `ip_address("10.0.0.5") in ip_network("10.0.0.0/24")` → `True`.
    *   **Iterating over a dictionary**: `for subnet, name in subnets.items():`

    **Task:**
    1.  Complete `classify_ip(ip_str, subnet_map)` — it should return the department name for the given IP, or `"UNKNOWN"` if it doesn't match any subnet.
    2.  Complete `classify_all(ip_list, subnet_map)` — return a dictionary `{department: [list_of_ips]}`.
    """)
    return


@app.cell
def _():
    import ipaddress
    return (ipaddress,)


@app.cell
def _():
    # Data Block - Do not modify
    vlan_map = {
        "10.0.1.0/24": "Engineering",
        "10.0.2.0/24": "Marketing",
        "10.0.3.0/24": "Management",
        "192.168.100.0/24": "Guest-WiFi",
    }

    observed_ips = [
        "10.0.1.15", "10.0.2.200", "10.0.1.42", "192.168.100.5",
        "10.0.3.1", "8.8.8.8", "10.0.2.55", "192.168.100.99",
    ]
    return observed_ips, vlan_map


@app.cell
def _(ipaddress, observed_ips, vlan_map):
    def classify_ip(ip_str, subnet_map):
        """
        Given an IP string and a subnet_map {cidr_string: department_name},
        return the department name the IP belongs to, or "UNKNOWN".
        """
        # TODO: Create an ip_address object from ip_str
        # TODO: Iterate over subnet_map items (cidr, department)
        # TODO: Create an ip_network object from the CIDR string
        # TODO: Check if the address is in the network using the `in` operator
        # TODO: Return the matching department, or "UNKNOWN" if no match
        pass

    def classify_all(ip_list, subnet_map):
        """
        Returns a dict: {department_name: [ip1, ip2, ...]}
        """
        result = {}
        # TODO: Iterate over each IP in ip_list
        # TODO: Use classify_ip to determine the department
        # TODO: If the department key doesn't exist in result, create an empty list
        # TODO: Append the IP to the department's list
        return result

    department_traffic = classify_all(observed_ips, vlan_map)
    return (department_traffic,)


@app.cell
def _(department_traffic, mo):
    mo.vstack([
        mo.md("### 🏢 VLAN Traffic Classification"),
        mo.json(department_traffic)
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Part 6: Log Timeline Analysis (Timestamps & Sorting)

    **Scenario:** You suspect a brute-force attack happened in a short burst. You need to parse timestamps from auth logs, sort events chronologically, and detect if more than `N` failed logins happened within a given time window.

    **The Data:**
    Auth log lines with timestamps in `YYYY-MM-DD HH:MM:SS` format.

    **Theory:**
    *   **`datetime.strptime()`**: Parses a string into a `datetime` object using a format string.
    *   **`sorted()` with `key=`**: Sort complex objects by a specific attribute.
    *   **`timedelta`**: Represents a duration. `datetime_b - datetime_a` gives a `timedelta`.
    *   **List Comprehensions**: `[x for x in items if condition]` — a compact way to filter.

    **Task:**
    1.  Complete `parse_auth_line(line)` to return a tuple `(datetime_obj, ip, status)`.
    2.  Complete `detect_brute_force(logs, window_seconds, max_failures)` to return a list of IPs that had more than `max_failures` failed attempts within `window_seconds`.
    """)
    return


@app.cell
def _():
    from datetime import datetime, timedelta
    return datetime, timedelta


@app.cell
def _():
    # Data Block - Do not modify
    auth_logs = [
        "2023-10-12 10:00:01 FAILED login from 203.0.113.50",
        "2023-10-12 10:00:03 FAILED login from 203.0.113.50",
        "2023-10-12 10:00:04 OK login from 10.0.0.5",
        "2023-10-12 10:00:05 FAILED login from 203.0.113.50",
        "2023-10-12 10:00:06 FAILED login from 203.0.113.50",
        "2023-10-12 10:00:07 FAILED login from 203.0.113.50",
        "2023-10-12 10:00:30 FAILED login from 198.51.100.22",
        "2023-10-12 10:05:00 FAILED login from 198.51.100.22",
        "2023-10-12 10:00:08 OK login from 203.0.113.50",
    ]
    return (auth_logs,)


@app.cell
def _(auth_logs, datetime, timedelta):
    def parse_auth_line(line):
        """
        Parses: "2023-10-12 10:00:01 FAILED login from 203.0.113.50"
        Returns: (datetime_object, ip_string, status_string)
        status is "FAILED" or "OK"
        """
        # TODO: Split the line into parts
        # TODO: Combine parts[0] and parts[1] and parse into a datetime object
        #       using format "%Y-%m-%d %H:%M:%S"
        # TODO: Extract the status from parts[2] and the IP from parts[5]
        # TODO: Return (timestamp, ip, status)
        pass

    def detect_brute_force(logs, window_seconds=10, max_failures=3):
        """
        Detects IPs with more than max_failures FAILED logins within window_seconds.
        Returns a dict: {ip: number_of_failures_in_window}
        """
        # Step 1: Parse all lines and keep only FAILED attempts as (timestamp, ip) tuples
        failed_events = []
        # TODO: Use parse_auth_line on each log line, filter for FAILED status

        # Step 2: Sort failed_events by timestamp
        # TODO: Use .sort() with a key function on the timestamp

        # Step 3: Group timestamps by IP into a dict {ip: [list_of_timestamps]}
        ip_times = {}
        # TODO: Populate ip_times from failed_events

        # Step 4: For each IP, use a sliding window approach to find the maximum
        #         number of failures within window_seconds
        # TODO: For each IP's sorted timestamps, use two pointers (left/right)
        # TODO: Advance right pointer; shrink left while time difference > window
        # TODO: Track the max count seen for each IP
        # TODO: If max count > max_failures, add to flagged dict
        flagged = {}

        return flagged

    brute_force_ips = detect_brute_force(auth_logs, window_seconds=10, max_failures=3)
    return (brute_force_ips,)


@app.cell
def _(brute_force_ips):
    brute_force_ips
    return


@app.cell
def _(brute_force_ips, mo):
    if brute_force_ips:
        output = mo.md(f"### 🚨 Brute-Force Alert!\nThe following IPs exceeded the failure threshold:\n{brute_force_ips}")
    else:
        output = mo.md("### ✅ No brute-force patterns detected.")
    output
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Part 7: Port Scan Detector (Sets & Nested Dictionaries)

    **Scenario:** You want to detect horizontal port scans — when a single source IP probes many different destination ports on your server in a short time.

    **The Data:**
    Simplified connection log entries: `SRC_IP DST_PORT PROTO`

    **Theory:**
    *   **Sets for uniqueness**: `set.add(port)` — sets automatically deduplicate.
    *   **`len(set)`**: Tells you how many *unique* items were seen.
    *   **Nested Dictionaries**: `{ip: set_of_ports}` — each IP maps to a set of ports it touched.
    *   **Threshold logic**: If `len(ports) > scan_threshold`, flag it.

    **Task:**
    1.  Complete `build_port_profile(logs)` — returns `{src_ip: set(ports_touched)}`.
    2.  Complete `detect_scanners(profile, threshold)` — returns a dict of IPs that touched more unique ports than the threshold, along with the list of ports.
    """)
    return


@app.cell
def _():
    # Data Block - Do not modify
    connection_logs = [
        "10.0.0.5 80 TCP",
        "10.0.0.5 443 TCP",
        "203.0.113.10 22 TCP",
        "203.0.113.10 23 TCP",
        "203.0.113.10 25 TCP",
        "203.0.113.10 80 TCP",
        "203.0.113.10 443 TCP",
        "203.0.113.10 3306 TCP",
        "203.0.113.10 5432 TCP",
        "203.0.113.10 8080 TCP",
        "10.0.0.5 80 TCP",
        "172.16.0.1 53 UDP",
        "172.16.0.1 53 UDP",
        "203.0.113.10 8443 TCP",
        "203.0.113.10 9090 TCP",
    ]
    return (connection_logs,)


@app.cell
def _(connection_logs):
    def build_port_profile(logs):
        """
        Returns: {src_ip: set(destination_ports)}
        """
        profile = {}
        # TODO: Iterate over each log line
        # TODO: Split the line and extract src_ip (index 0) and dst_port (index 1, as int)
        # TODO: If the IP isn't in profile yet, initialize it with an empty set
        # TODO: Add the port to the IP's set
        return profile

    def detect_scanners(profile, threshold=5):
        """
        Returns: {ip: sorted_list_of_ports} for IPs that touched > threshold unique ports.
        """
        scanners = {}
        # TODO: Iterate over profile items (ip, ports)
        # TODO: If the number of unique ports exceeds the threshold,
        #       add the IP to scanners with a sorted list of its ports
        return scanners

    port_profile = build_port_profile(connection_logs)
    scanner_report = detect_scanners(port_profile, threshold=5)
    return (scanner_report,)


@app.cell
def _(mo, scanner_report):
    if scanner_report:
        _items = []
        for ip, ports in scanner_report.items():
            _items.append(mo.md(f"### 🔍 Port Scan Detected\n**Source:** `{ip}` scanned **{len(ports)}** unique ports: `{ports}`"))
        _output = mo.vstack(_items)
    else:
        _output = mo.md("### ✅ No port scan activity detected.")

    _output
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## Part 8: Configuration Drift Detector (Nested Dicts & Comparison)

    **Scenario:** You have two snapshots of a network device configuration (e.g., from a router or switch). You need to compare them and report what changed, what was added, and what was removed.

    **The Data:**
    Two configuration "files" represented as multi-line strings in `key = value` format (like simplified `.conf` files).

    **Theory:**
    *   **Parsing key-value configs**: Split each line on `=`, strip whitespace.
    *   **Set operations on dict keys**: `set(dict_a.keys()) - set(dict_b.keys())` gives keys only in `a`.
    *   **`dict_a.keys() & dict_b.keys()`**: Intersection — keys present in both.
    *   **Comparing values**: For shared keys, check if the value changed.

    **Task:**
    Complete `diff_configs(old_conf_str, new_conf_str)` that returns a dictionary:
    ```python
    {
        "added": {key: new_value, ...},
        "removed": {key: old_value, ...},
        "changed": {key: {"old": old_val, "new": new_val}, ...},
        "unchanged_count": int
    }
    ```
    """)
    return


@app.cell
def _():
    # Data Block - Do not modify
    config_old = """
    hostname = router-core-01
    interface_eth0 = 10.0.0.1/24
    interface_eth1 = 10.0.1.1/24
    dns_server = 8.8.8.8
    ntp_server = pool.ntp.org
    enable_ipv6 = no
    max_routes = 10000
    """

    config_new = """
    hostname = router-core-01
    interface_eth0 = 10.0.0.1/24
    interface_eth1 = 10.0.1.254/24
    dns_server = 1.1.1.1
    ntp_server = pool.ntp.org
    enable_ipv6 = yes
    firewall_policy = strict
    """
    return config_new, config_old


@app.cell
def _(config_new, config_old):
    def parse_config(conf_str):
        """
        Parses a key=value config string into a dictionary.
        Ignores blank lines.
        """
        result = {}
        # TODO: Strip the config string and split by newlines
        # TODO: For each non-empty line containing "=":
        #       Split on "=" (max 1 split), strip whitespace from key and value
        #       Store in result dict
        return result

    def diff_configs(old_str, new_str):
        """
        Compares two config strings and returns a diff report.
        """
        old = parse_config(old_str)
        new = parse_config(new_str)

        # TODO: Create sets of old and new keys
        # TODO: Find added keys (in new but not old), removed keys (in old but not new),
        #       and common keys (in both) using set operations

        report = {
            "added": {},
            "removed": {},
            "changed": {},
            "unchanged_count": 0,
        }

        # TODO: Populate report["added"] with {key: new_value} for each added key
        # TODO: Populate report["removed"] with {key: old_value} for each removed key
        # TODO: For each common key, compare old and new values:
        #       - If different, add to report["changed"] as {key: {"old": ..., "new": ...}}
        #       - If same, increment report["unchanged_count"]

        return report

    config_diff = diff_configs(config_old, config_new)
    return (config_diff,)


@app.cell
def _(config_diff, mo):
    mo.vstack([
        mo.md(f"""
    ### ⚙️ Configuration Drift Report

    | Category | Count |
    |----|----|
    | Added    | {len(config_diff['added'])} |
    | Removed  | {len(config_diff['removed'])} |
    | Changed  | {len(config_diff['changed'])} |
    | Unchanged| {config_diff['unchanged_count']} |
    """),
        mo.json(config_diff)
    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## 🏆 Part 9: Boss Level — Automated Incident Report Generator

    **Scenario:** You are the on-call engineer. An alert fired at 3 AM. You have logs from multiple sources (web server, firewall, auth). You need to **correlate** them and produce a structured incident report automatically.

    **This task combines everything you've learned:**
    *   String parsing (Parts 1–3)
    *   Counting & thresholds (Part 4)
    *   IP classification (Part 5)
    *   Timestamp analysis (Part 6)
    *   Port profiling (Part 7)
    *   Diff / comparison logic (Part 8)

    **Task:**
    Given the three log sources below, produce an `incident_report` dictionary with:

    ```python
    {
        "summary": "Automated Incident Report — <timestamp>",
        "top_offender_ip": "<​​the IP with the most suspicious activity>",
        "offender_department": "<​​department from VLAN map, or UNKNOWN>",
        "web_404s": [list of paths that got 404],
        "ssh_failed_attempts": int,
        "ports_scanned": [sorted list of ports],
        "severity": "CRITICAL" | "HIGH" | "MEDIUM" | "LOW",
    }
    ```

    **Severity rules:**
    *   **CRITICAL**: Port scan detected AND brute-force SSH AND web 404s from the same IP.
    *   **HIGH**: Any two of the above from the same IP.
    *   **MEDIUM**: Any one of the above.
    *   **LOW**: No suspicious activity detected.

    **Hints:**
    *   Reuse your functions from earlier parts!
    *   Build helper sets: `ips_with_404`, `ips_with_ssh_fail`, `ips_with_scan`.
    *   Find the intersection to determine the top offender.
    """)
    return


@app.cell
def _():
    # Data Block - Do not modify
    incident_web_logs = [
        '203.0.113.10 - - [12/Oct/2023:03:00:01] "GET /index.html HTTP/1.1" 200 512',
        '203.0.113.10 - - [12/Oct/2023:03:00:02] "GET /admin HTTP/1.1" 404 124',
        '203.0.113.10 - - [12/Oct/2023:03:00:03] "GET /wp-login.php HTTP/1.1" 404 124',
        '203.0.113.10 - - [12/Oct/2023:03:00:04] "GET /.env HTTP/1.1" 404 0',
        '203.0.113.10 - - [12/Oct/2023:03:00:05] "GET /phpmyadmin HTTP/1.1" 404 0',
        '10.0.1.15 - - [12/Oct/2023:03:00:06] "GET /index.html HTTP/1.1" 200 512',
    ]

    incident_fw_logs = [
        "Oct 12 03:00:10 srv kernel: IN=eth0 SRC=203.0.113.10 DST=10.0.0.1 PROTO=TCP DPT=22",
        "Oct 12 03:00:11 srv kernel: IN=eth0 SRC=203.0.113.10 DST=10.0.0.1 PROTO=TCP DPT=23",
        "Oct 12 03:00:12 srv kernel: IN=eth0 SRC=203.0.113.10 DST=10.0.0.1 PROTO=TCP DPT=3306",
        "Oct 12 03:00:13 srv kernel: IN=eth0 SRC=203.0.113.10 DST=10.0.0.1 PROTO=TCP DPT=5432",
        "Oct 12 03:00:14 srv kernel: IN=eth0 SRC=203.0.113.10 DST=10.0.0.1 PROTO=TCP DPT=8080",
        "Oct 12 03:00:15 srv kernel: IN=eth0 SRC=203.0.113.10 DST=10.0.0.1 PROTO=TCP DPT=9090",
        "Oct 12 03:00:16 srv kernel: IN=eth0 SRC=10.0.1.15 DST=10.0.0.1 PROTO=TCP DPT=80",
    ]

    incident_auth_logs = [
        "2023-10-12 03:00:20 FAILED login from 203.0.113.10",
        "2023-10-12 03:00:21 FAILED login from 203.0.113.10",
        "2023-10-12 03:00:22 FAILED login from 203.0.113.10",
        "2023-10-12 03:00:23 FAILED login from 203.0.113.10",
        "2023-10-12 03:00:24 FAILED login from 203.0.113.10",
        "2023-10-12 03:00:30 OK login from 10.0.1.15",
    ]

    incident_vlan_map = {
        "10.0.1.0/24": "Engineering",
        "10.0.2.0/24": "Marketing",
        "10.0.3.0/24": "Management",
        "192.168.100.0/24": "Guest-WiFi",
    }
    return (
        incident_auth_logs,
        incident_fw_logs,
        incident_vlan_map,
        incident_web_logs,
    )


@app.cell
def _(
    datetime,
    incident_auth_logs,
    incident_fw_logs,
    incident_vlan_map,
    incident_web_logs,
    ipaddress,
):
    def generate_incident_report(web_logs, fw_logs, auth_logs, vlan_map):
        """
        Correlates multiple log sources and generates an incident report.
        """
        # --- Step 1: Analyze web logs for 404s ---
        ip_404_paths = {}  # {ip: [path1, path2, ...]}
        # TODO: For each web log line, split into parts, extract IP (index 0) and status (index 8)
        # TODO: If status is 404, extract the requested path (index 6)
        # TODO: Build a dict mapping each IP to its list of 404 paths

        # --- Step 2: Analyze firewall logs for port scanning ---
        ip_ports = {}  # {ip: set(ports)}
        # TODO: For each firewall log line, find the SRC= and DPT= fields
        # TODO: Build a dict mapping each source IP to the set of destination ports it touched

        # --- Step 3: Analyze auth logs for brute-force ---
        ip_fail_count = {}  # {ip: count}
        # TODO: For each auth log line, extract status and IP
        # TODO: Count FAILED attempts per IP

        # --- Step 4: Build indicator sets ---
        # TODO: ips_with_404 = set of IPs that have any 404 paths
        # TODO: ips_with_scan = set of IPs that probed more than 5 unique ports
        # TODO: ips_with_brute = set of IPs with more than 3 failed login attempts

        # --- Step 5: Find the top offender ---
        # TODO: Union all suspicious IP sets
        # TODO: Score each IP by how many indicator sets it appears in (0-3)
        # TODO: The IP with the highest score is the top offender

        # --- Step 6: Classify the top offender's department ---
        # TODO: Use ipaddress module to check the top offender IP against vlan_map
        # TODO: Return the matching department name, or "UNKNOWN"

        # --- Step 7: Determine severity ---
        # TODO: CRITICAL if score >= 3, HIGH if 2, MEDIUM if 1, LOW if 0

        # --- Step 8: Build the report ---
        report = {
            "summary": f"Automated Incident Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "top_offender_ip": None,       # TODO: fill in
            "offender_department": None,    # TODO: fill in
            "web_404s": [],                 # TODO: fill in from ip_404_paths for top offender
            "ssh_failed_attempts": 0,       # TODO: fill in from ip_fail_count for top offender
            "ports_scanned": [],            # TODO: fill in from ip_ports for top offender (sorted)
            "severity": "LOW",              # TODO: fill in based on score
        }

        return report

    incident_report = generate_incident_report(
        incident_web_logs, incident_fw_logs, incident_auth_logs, incident_vlan_map
    )
    return (incident_report,)


@app.cell
def _(incident_report, mo):
    severity_emoji = {
        "CRITICAL": "‼️",
        "HIGH": "⚠️",
        "MEDIUM": "⏳",
        "LOW": "✅",
    }

    sev = incident_report["severity"]
    emoji = severity_emoji.get(sev, "⚪")

    mo.vstack([
        mo.md(f"""
        ### {emoji} Incident Report — Severity: **{sev}**
    
        | Field | Value |
        |----|----|
        | Top Offender | `{incident_report['top_offender_ip']}` |
        | Department | {incident_report['offender_department']} |
        | SSH Failed Attempts | {incident_report['ssh_failed_attempts']} |
        | Ports Scanned | {len(incident_report['ports_scanned'])} |
        | Web 404 Probes | {len(incident_report['web_404s'])} |
    
        **404 Paths Probed:** `{incident_report['web_404s']}`
    
        **Ports Scanned:** `{incident_report['ports_scanned']}`
        """),
        mo.json(incident_report)
    ])
    return


if __name__ == "__main__":
    app.run()
