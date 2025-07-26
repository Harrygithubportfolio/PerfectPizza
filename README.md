# 🍕 PerfectPizza

**PerfectPizza** is a blazing-fast, functional, and extensible HTML parser written in Python. It is designed as a modern alternative to BeautifulSoup, focused on performance, functional purity, and clean DOM traversal. Built from the ground up using only standard libraries (for now), it lays the foundation for high-speed, intelligent web scraping and HTML processing.

---

## 🎯 Project Goal

To create a minimal, powerful HTML parser and DOM traversal tool with:

- Functional, immutable operations
- Tree-based parsing of malformed or valid HTML
- Pure functions for transformation and querying
- Future extensibility: CSS4 selectors, XPath, JS-rendered HTML, AI-assisted parsing

PerfectPizza emphasizes **clarity, performance, and composability**.

---

## 🏗️ Project Structure

PerfectPizza/
├── perfectpizza/
│ ├── init.py # Module initializer
│ ├── dom.py # DOM node representation and utilities
│ ├── parser.py # HTML parser and functional traversal
├── test/
│ └── test_parser.py # Unit tests for parser
├── example.py # Example usage script
└── README.md # Documentation (this file)

yaml
Copy
Edit

---

## 🔧 Core Concepts

### 1. **DOM Representation (`Node`)**
HTML is parsed into a custom tree of `Node` objects that represent tags. Each node contains:

- `tag`: Tag name (`div`, `p`, `h1`, etc.)
- `attrs`: Dictionary of HTML attributes (`{"class": "title"}`)
- `children`: A list of either strings (text nodes) or other `Node` objects
- `parent`: Link to the parent node (optional)

### 2. **Parsing**
HTML is parsed using Python's built-in `html.parser.HTMLParser`. It builds a tree of `Node` objects that mirror the nested structure of the HTML document.

### 3. **Functional Traversal**
You query the tree using pure functions like `find_all(node, tag_name)`, which returns all descendant tags with that name. No mutation of state occurs—this is a read-only, functional API.

---

## 🚀 Getting Started

### 1. Clone the repo or copy files

```bash
git clone https://github.com/yourusername/PerfectPizza.git
cd PerfectPizza
Or create the structure manually with:

bash
Copy
Edit
PerfectPizza/
    perfectpizza/
    test/
    example.py
    README.md
2. Run the example
bash
Copy
Edit
python example.py
This parses a sample HTML snippet and prints its structure + extracted <h1> text.

3. Run tests
bash
Copy
Edit
python -m unittest discover test
🧪 Example Usage
Here’s what using PerfectPizza looks like:

python
Copy
Edit
from perfectpizza.parser import parse, find_all

html = """
<html>
  <body>
    <h1 class="title">PerfectPizza Parser</h1>
    <p>Hello, world!</p>
  </body>
</html>
"""

doc = parse(html)

# Find all <h1> tags
headings = find_all(doc, "h1")
for h in headings:
    print("Heading Text:", h.text())
📦 Current Features (MVP – Phase 1)
Feature	Description
✅ Custom HTML DOM	Custom Node tree structure for representing HTML
✅ HTML parsing	Parses raw HTML into Node trees
✅ Tree navigation	Access and traverse children and parents
✅ Functional querying	find_all(node, tag) returns all matching tags
✅ Immutability by default	Tree is read-only unless explicitly transformed
✅ Unit testing	Tested using Python’s unittest module

🧩 Coming Soon (Future Phases)
These features are planned and designed:

Feature	Planned Description
🔜 Full CSS4 Selector Support	Use .select(dom, "div > h1.title") queries
🔜 HTML Output (to_html)	Export clean HTML from a Node tree
🔜 Functional Mutations	replace_attr(), remove_tags(), etc.
🔜 JavaScript Rendering	Parse JS-rendered pages using Playwright or Pyppeteer
🔜 Fuzzy Matching	Semantic tag matching (e.g. "price", "headline")
🔜 Plugin System	Optional AI helpers, validators, and output transformers
🔜 Pandas Integration	Convert tables into usable pandas.DataFrames

🧠 Design Philosophy
Functional: All operations are stateless and predictable. No side effects.

Fast: Designed to scale from simple scripts to large-scale crawlers.

Composable: Functions can be combined easily for complex workflows.

Hackable: Clear code structure for extension and custom use cases.

🧪 Example Test Case
python
Copy
Edit
from perfectpizza.parser import parse, find_all

def test_parsing():
    html = "<div><p>Hello</p><p>World</p></div>"
    doc = parse(html)
    paragraphs = find_all(doc, "p")
    assert paragraphs[0].text() == "Hello"
    assert paragraphs[1].text() == "World"
🧠 FAQ
Q: Is this a replacement for BeautifulSoup?
A: Not yet—but it aims to be faster, more modern, and fully functional. It’s an educational and performance-driven reimagining of HTML parsing.

Q: Does it support malformed HTML?
A: Yes. The built-in html.parser is fault-tolerant. Future versions may swap this for faster, stricter engines.

Q: Why “PerfectPizza”?
A: Because it’s a delicious slice of Python: fast, clean, satisfying, and infinitely customizable. 🍕

👥 Credits & Contributions
Created by Harry Graham
Open to contributions once Phase 2 is in progress!

📜 License
MIT License – use freely and with extra cheese.

🧭 Roadmap Summary
 Phase 1: DOM + Parser

 Phase 2: CSS Selectors + Mutation

 Phase 3: JS-Rendered HTML Support

 Phase 4: AI Plugins + Table Extraction

 Phase 5: Docs, Packaging, PyPI, Demos

Built with Python, logic, and love. 🍕

yaml
Copy
Edit

---
