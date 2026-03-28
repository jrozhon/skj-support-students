import marimo

__generated_with = "0.21.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import xml.etree.ElementTree as ET

    return ET, mo


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # 📄 Lab: XML Processing with Python

    **Duration:** 90 Minutes

    **Focus:** XML Structure, `xml.etree.ElementTree`, Parsing, Creating, Modifying, Searching, and Writing XML

    **Context:** Student Grade Management System

    ---

    ### 🎯 Objective
    In this lab you will learn how to work with XML data in Python using the built-in
    `xml.etree.ElementTree` module. You will parse existing XML, create new elements,
    modify content, search the tree, and write results back to a file — skills used
    in configuration management, data exchange, and web services every day.

    ### 📚 References
    *   [Python xml.etree.ElementTree docs](https://docs.python.org/3/library/xml.etree.elementtree.html)
    *   [W3Schools XML Tutorial](https://www.w3schools.com/xml/)
    *   [Real Python — Working With XML](https://realpython.com/python-xml-parser/)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 0: What is XML and Why Does It Matter?

    **XML** (eXtensible Markup Language) is a text-based format for storing and
    transporting structured data. Unlike HTML (which is about *displaying* data),
    XML is about *describing* data.

    ### Key Concepts

    | Term | Meaning | Example |
    |---|---|---|
    | **Element** | A node in the tree, delimited by tags | `<student>...</student>` |
    | **Tag** | The name of an element | `student`, `task` |
    | **Attribute** | Key-value metadata on an opening tag | `id="xnovak01"` |
    | **Text** | Character content inside an element | `<points>10</points>` |
    | **Root** | The single top-level element | `<students>` |
    | **Child / Parent** | Hierarchical relationship between elements | `<task>` is a child of `<student>` |

    ### Anatomy of an XML Document

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>   ← XML declaration (optional)
    <students>                    ← root element
        <student id="xnovak01">              ← element with an attribute
            <task id="task1">               ← child element
                <points>8</points>          ← leaf element with text content
            </task>
        </student>
    </students>
    ```

    ### Rules
    - Every document has **exactly one root** element.
    - Tags are **case-sensitive** (`<Student>` ≠ `<student>`).
    - Every opening tag must have a **matching closing tag** (or be self-closing: `<br/>`).
    - Attribute values must be **quoted**.
    - Special characters must be **escaped**: `&amp;` `&lt;` `&gt;` `&quot;` `&apos;`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 1: Parsing XML with `ElementTree`

    Python's standard library ships with `xml.etree.ElementTree` (often imported as `ET`).
    It represents an XML document as a **tree of `Element` objects**.

    ### Two ways to parse

    ```python
    import xml.etree.ElementTree as ET

    # From a file
    tree = ET.parse("grades.xml")
    root = tree.getroot()

    # From a string (useful for testing / network responses)
    root = ET.fromstring(xml_string)
    ```

    ### Useful `Element` attributes and methods

    | Member | What it gives you |
    |---|---|
    | `element.tag` | The tag name (`"student"`) |
    | `element.text` | Text content between tags |
    | `element.attrib` | Dict of all attributes |
    | `element.get("id")` | Value of attribute `id` (or `None`) |
    | `element.set("id", "x")` | Set / overwrite an attribute |
    | `list(element)` | Direct children as a list |
    | `element.find("tag")` | First child with that tag (or `None`) |
    | `element.findall("tag")` | All children with that tag |
    | `element.iter("tag")` | All descendants with that tag (recursive) |
    | `element.append(child)` | Add a child element |
    | `element.remove(child)` | Remove a child element |
    """)
    return


@app.cell
def _(ET):
    # ── Sample XML we will use throughout the tutorial ──
    SAMPLE_XML = """<?xml version="1.0"?>
    <students>
        <student id="xnovak01">
            <task id="task1"><points>8</points></task>
            <task id="task2"><points>5</points></task>
        </student>
        <student id="xsmith02">
            <task id="task1"><points>10</points></task>
        </student>
    </students>
    """

    # TODO: Parse SAMPLE_XML from the string above into a root element
    root = None  # TODO: use ET.fromstring(...)

    # TODO: Print the root tag, root attributes, and a list of direct children tags
    return SAMPLE_XML, root


@app.cell
def _(root):
    # TODO: Access the first student element using index access
    first_student = None  # TODO: root[0]
    # TODO: Print the first student's id attribute and tag

    # TODO: Iterate over all students using findall() and for each one
    #       print their id and how many tasks they have
    return (first_student,)


@app.cell
def _(root):
    def _():
        # TODO: Iterate over all students, and for each student iterate over
        #       all tasks. For each task, read the points text and print:
        #       "  <student_id> / <task_id> → <points> pts"
        pass

    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔍 XPath-lite: `find` vs `findall` vs `iter`

    `ElementTree` supports a **subset of XPath** expressions:

    ```python
    # Direct child named "student"
    root.find("student")

    # All direct children named "student"
    root.findall("student")

    # All <task> elements anywhere in the tree (recursive)
    root.iter("task")

    # Student whose id attribute equals "xnovak01"
    root.find("student[@id='xnovak01']")

    # All tasks of a specific student
    root.findall("student[@id='xnovak01']/task")
    ```
    """)
    return


@app.cell
def _(ET, SAMPLE_XML):
    root2 = ET.fromstring(SAMPLE_XML)

    # TODO: Use an XPath attribute predicate to find the student with id "xnovak01"
    #       and print their id
    target = None  # TODO: root2.find(...)

    # TODO: Use iter() to iterate over ALL tasks in the document (across all students)
    #       and for each task print its id and points text
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 2: Creating XML Programmatically

    You can build an XML tree from scratch using `ET.Element` and `ET.SubElement`.

    ```python
    import xml.etree.ElementTree as ET

    # Create the root element
    root = ET.Element("students")

    # Create a child element and attach it
    student = ET.SubElement(root, "student")
    student.set("id", "xnovak01")

    # Create a grandchild
    task = ET.SubElement(student, "task")
    task.set("id", "task1")

    points = ET.SubElement(task, "points")
    points.text = "8"          # set text content
    ```

    ### `ET.Element` vs `ET.SubElement`

    | | `ET.Element(tag)` | `ET.SubElement(parent, tag)` |
    |---|---|---|
    | Creates element | ✅ | ✅ |
    | Attaches to parent | ❌ (you must `parent.append(el)`) | ✅ automatically |

    ### Pretty-printing (Python ≥ 3.9)

    ```python
    ET.indent(root)                    # adds newlines & spaces in-place
    print(ET.tostring(root, encoding="unicode"))
    ```
    """)
    return


@app.cell
def _(ET):
    # TODO: Build a fresh XML tree from scratch with the following structure:
    #
    #   <students>
    #       <student id="xbrown03">
    #           <task id="task1"><points>7</points></task>
    #       </student>
    #       <student id="xwhite04">
    #           <task id="task1"><points>9</points></task>
    #       </student>
    #   </students>
    #
    # Requirements:
    #   - Create the root element using ET.Element()
    #   - Add xbrown03 and their task using ET.SubElement()
    #   - Add xwhite04 using ET.Element() + root.append() (not SubElement)
    #   - Add xwhite04's task using ET.SubElement()
    #   - Pretty-print the result using ET.indent() and ET.tostring()

    new_root = None  # TODO: ET.Element("students")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 3: Modifying an Existing XML Tree

    Once you have a tree in memory you can:

    - **Change text**: `element.text = "new value"`
    - **Change / add attribute**: `element.set("key", "value")`
    - **Add a child**: `parent.append(new_child)` or `ET.SubElement(parent, tag)`
    - **Remove a child**: `parent.remove(child)` — you need a reference to the *parent*

    > ⚠️ `remove()` takes the **child element object**, not a tag name or index.
    > You must first find the child, then call `parent.remove(child)`.

    ### Typical pattern for safe removal

    ```python
    for student in root.findall("student"):
        if student.get("id") == "xnovak01":
            root.remove(student)   # root is the parent
            break
    ```
    """)
    return


@app.cell
def _(ET, SAMPLE_XML):
    def _():
        mod_root = ET.fromstring(SAMPLE_XML)

        # TODO 1: Find the <points> element for xnovak01 / task2 using an XPath path,
        #         print its current value, change it to 9, then print the new value

        # TODO 2: Find the student xsmith02, add a new task "task2" with points 6
        #         using ET.SubElement(), then print all task ids for xsmith02

        # TODO 3: Remove the student xnovak01 from mod_root entirely.
        #         Hint: iterate with findall(), check the id, then call mod_root.remove()

        # TODO 4: Print the remaining student ids, then pretty-print the final XML
        #         using ET.indent() and ET.tostring()

        return mod_root

    mod_root = _()
    return (mod_root,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 4: Writing XML to a File

    After modifying the tree, persist it with `ElementTree.write()`.

    ```python
    tree = ET.ElementTree(root)          # wrap root in a Tree object
    tree.write(
        "output.xml",
        encoding="unicode",              # "unicode" → str output (no BOM)
        xml_declaration=True             # adds <?xml version='1.0' ...?>
    )
    ```

    Or write to a string for inspection / network transmission:

    ```python
    xml_str = ET.tostring(root, encoding="unicode", xml_declaration=True)
    ```

    ### Round-trip pattern (parse → modify → save)

    ```python
    tree = ET.parse("grades.xml")        # parse from file
    root = tree.getroot()

    # ... make changes to root ...

    ET.indent(root)                    # optional: pretty-print
    tree.write("grades.xml", encoding="unicode", xml_declaration=True)
    ```
    """)
    return


@app.cell
def _(ET, mod_root):
    # TODO: Wrap mod_root in an ET.ElementTree and write it to "grades_output.xml"
    #       Use encoding="unicode" and xml_declaration=True
    #       Print a confirmation message after writing

    # TODO: Verify the file was written correctly by re-parsing it with ET.parse()
    #       and printing the ids of all students found in the re-parsed tree
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 5: Error Handling & Defensive Patterns

    Real-world XML processing requires guarding against:

    | Situation | What to check |
    |---|---|
    | Element not found | `find()` returns `None` — always check before accessing `.text` |
    | Duplicate entries | Search before inserting |
    | Malformed XML | Wrap `ET.parse()` / `ET.fromstring()` in `try/except ET.ParseError` |
    | Missing attribute | Use `element.get("id", default)` instead of `element.attrib["id"]` |

    ### Pattern: check-before-insert

    ```python
    def create_student(root, student_id):
        existing = root.find(f"student[@id='{student_id}']")
        if existing is not None:
            raise Exception("student already exists")
        student = ET.SubElement(root, "student")
        student.set("id", student_id)
    ```

    ### Pattern: safe text access

    ```python
    pts_el = task.find("points")
    points = int(pts_el.text) if pts_el is not None else 0
    ```

    ### Pattern: parse error handling

    ```python
    try:
        root = ET.fromstring(bad_xml)
    except ET.ParseError as e:
        print(f"XML is malformed: {e}")
    ```
    """)
    return


@app.cell
def _(ET):
    # Demonstrate defensive patterns

    safe_xml = "<students><student id='xa01'><task id='t1'><points>5</points></task></student></students>"
    safe_root = ET.fromstring(safe_xml)

    # TODO 1: Use find() to search for a student with id "nobody" and print the result
    #         (it should be None)

    # TODO 2: Find the first student element and demonstrate:
    #         - safe access of an existing attribute ("id")
    #         - safe access of a missing attribute ("grade") with a default value of "N/A"

    # TODO 3: Try to parse the malformed string "<unclosed>" and catch ET.ParseError,
    #         printing the error message

    # TODO 4: Implement safe_add_student(root, sid) that:
    #         - raises Exception("student already exists") if the student is already present
    #         - otherwise adds the student and returns the new element
    #         Then call it once successfully (id "xb02") and once to trigger the duplicate
    #         error (id "xa01"), printing results each time

    def safe_add_student(root, sid):
        # TODO: implement
        pass

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Part 6: Putting It All Together — Grade Manager

    Now implement all five functions from `tasks.py` yourself.
    Each function operates on an `xml_root` element representing the `<students>` tree.

    The XML structure:

    ```xml
    <students>
        <student id="xnovak01">
            <task id="task1">
                <points>8</points>
            </task>
        </student>
    </students>
    ```

    Use the patterns from Parts 1–5:
    - XPath predicate `[@id='...']` to locate elements
    - `parent.remove(child)` for deletion (you need the parent reference!)
    - `iter()` to walk the whole tree for cross-student operations
    """)
    return


@app.cell
def _(ET):
    def create_student(xml_root, student_id):
        """Add a new <student id="..."> element. Raises if already exists."""
        # TODO: Check if a student with student_id already exists; if so raise Exception("student already exists")
        # TODO: Create a new <student> subelement and set its "id" attribute
        pass


    def remove_student(xml_root, student_id):
        """Remove the <student> with the given id."""
        # TODO: Find the student element with the matching id
        # TODO: If found, remove it from xml_root
        pass


    def set_task_points(xml_root, student_id, task_id, points):
        """Overwrite the <points> text for a specific student/task pair."""
        # TODO: Build an XPath path to reach the <points> element for the given
        #       student_id and task_id (e.g. "student[@id='...']/task[@id='...']/points")
        # TODO: If the element exists, set its .text to str(points)
        pass


    def create_task(xml_root, student_id, task_id, points):
        """Add a new <task> under a student. Raises if task already exists."""
        # TODO: Find the student; raise Exception("student not found") if missing
        # TODO: Check if the task already exists; raise Exception("task already exists") if so
        # TODO: Create a <task> subelement with the given task_id
        # TODO: Create a <points> subelement inside the task and set its text to str(points)
        pass


    def remove_task(xml_root, task_id):
        """Remove every <task id='task_id'> across ALL students."""
        # TODO: Iterate over all students with findall()
        # TODO: For each student, find all tasks matching task_id and remove them
        pass


    print("Functions defined — now test them below!")
    return (
        create_student,
        create_task,
        remove_student,
        remove_task,
        set_task_points,
    )


@app.cell
def _(
    ET,
    create_student,
    create_task,
    remove_student,
    remove_task,
    set_task_points,
):
    # ── Test your implementations here ──

    demo_xml = "<students/>"
    demo_root = ET.fromstring(demo_xml)

    # 1. create_student
    create_student(demo_root, "xnovak01")
    create_student(demo_root, "xsmith02")
    print("After create_student x2:", [s.get("id") for s in demo_root.findall("student")])

    # 2. Duplicate guard
    try:
        create_student(demo_root, "xnovak01")
    except Exception as e:
        print(f"Duplicate student → {e}")

    # 3. create_task
    create_task(demo_root, "xnovak01", "task1", 8)
    create_task(demo_root, "xnovak01", "task2", 5)
    create_task(demo_root, "xsmith02", "task1", 10)
    print("xnovak01 tasks:", [t.get("id") for t in demo_root.findall("student[@id='xnovak01']/task")])

    # 4. Duplicate task guard
    try:
        create_task(demo_root, "xnovak01", "task1", 99)
    except Exception as e:
        print(f"Duplicate task    → {e}")

    # 5. set_task_points
    set_task_points(demo_root, "xnovak01", "task2", 9)
    pts = demo_root.find("student[@id='xnovak01']/task[@id='task2']/points").text
    print(f"xnovak01/task2 after set_task_points → {pts}")

    # 6. remove_task (across all students)
    remove_task(demo_root, "task1")
    print("After remove_task('task1'):")
    for s in demo_root.findall("student"):
        print(f"  {s.get('id')}: {[t.get('id') for t in s.findall('task')]}")

    # 7. remove_student
    remove_student(demo_root, "xsmith02")
    print("After remove_student('xsmith02'):", [s.get("id") for s in demo_root.findall("student")])

    ET.indent(demo_root)
    print("\nFinal XML state:")
    print(ET.tostring(demo_root, encoding="unicode"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ---

    ## 🚀 Final Challenge: Grade Report Generator

    **Scenario:** You are given an XML file with student grades. Write a function
    `grade_report(xml_root)` that returns a **summary dict** with the following
    structure:

    ```python
    {
        "xnovak01": {"tasks": ["task1", "task2"], "total": 17, "average": 8.5},
        "xsmith02": {"tasks": ["task1"],           "total": 10, "average": 10.0},
    }
    ```

    **Requirements:**
    1. Iterate over all `<student>` elements.
    2. For each student collect all task IDs and their points.
    3. Compute `total` (sum of points) and `average` (mean, rounded to 1 decimal).
    4. Return the dict — do **not** print inside the function.
    5. Handle the edge case where a student has **no tasks** (average = 0.0).

    **Bonus:** Add a `top_student(report)` function that returns the student id
    with the highest average.
    """)
    return


@app.cell
def _(ET):
    def grade_report(xml_root):
        """Build a summary dict for all students."""
        # TODO: Create an empty report dict
        # TODO: Iterate over all <student> elements
        #       For each student:
        #         - get their id
        #         - iterate over their <task> elements, collecting task ids and summing points
        #           (use safe text access: int(pts_el.text) if pts_el is not None else 0)
        #         - compute average (round to 1 decimal); handle the no-tasks edge case
        #         - store {"tasks": [...], "total": ..., "average": ...} in the report dict
        # TODO: Return the report
        pass


    def top_student(report):
        """Return the student id with the highest average."""
        # TODO: Return None if report is empty
        # TODO: Use max() with a key function to find the student with the highest average
        pass


    # ── Test ──
    challenge_xml = """<students>
        <student id="xnovak01">
            <task id="task1"><points>8</points></task>
            <task id="task2"><points>9</points></task>
        </student>
        <student id="xsmith02">
            <task id="task1"><points>10</points></task>
        </student>
        <student id="xempty03">
        </student>
    </students>"""

    challenge_root = ET.fromstring(challenge_xml)
    report = grade_report(challenge_root)

    if report:
        for student_id, data in report.items():
            print(f"{student_id}: tasks={data['tasks']}, total={data['total']}, avg={data['average']}")
        print(f"\nTop student: {top_student(report)}")
    else:
        print("grade_report() returned nothing yet — implement it above!")
    return report, top_student


@app.cell
def _(mo, report, top_student):
    if report:
        _rows = "\n".join(
            f"| `{student_id}` | {', '.join(f'`{t}`' for t in d['tasks']) or '—'} | {d['total']} | {d['average']} |"
            for student_id, d in report.items()
        )
        mo.md(
            f"### 📊 Grade Report\n\n"
            f"| Student | Tasks | Total pts | Average |\n"
            f"|---|---|---|---|\n"
            f"{_rows}\n\n"
            f"🏆 **Top student:** `{top_student(report)}`\n\n"
            f"This pattern — parse XML, aggregate data, produce a report — is the backbone "
            f"of countless real systems: CI/CD test result parsers (JUnit XML), "
            f"Maven/Gradle build reports, SCORM e-learning packages, and RSS/Atom feeds."
        )
    else:
        mo.md("*Implement `grade_report()` above to see the report here.*")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
