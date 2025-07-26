# example.py

from perfectpizza.parser import parse

html = """
<html>
  <body>
    <h1 class="title">PerfectPizza Parser</h1>
    <p>Hello, world!</p>
  </body>
</html>
"""

doc = parse(html)

def print_dom(node, indent=0):
    spacer = "  " * indent
    if isinstance(node, str):
        print(spacer + repr(node))
        return
    print(f"{spacer}<{node.tag}>")
    for child in node.children:
        print_dom(child, indent + 1)

print_dom(doc)
