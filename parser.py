# perfectpizza/parser.py

from html.parser import HTMLParser
from .dom import Node

class PizzaHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.root = Node("document", {})
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        node = Node(tag, attrs_dict, parent=self.stack[-1])
        self.stack[-1].add_child(node)
        self.stack.append(node)

    def handle_endtag(self, tag):
        if len(self.stack) > 1:
            self.stack.pop()

    def handle_data(self, data):
        stripped = data.strip()
        if stripped:
            self.stack[-1].add_child(stripped)

def parse(html: str) -> Node:
    parser = PizzaHTMLParser()
    parser.feed(html)
    return parser.root
# perfectpizza/parser.py (continued)

def find_all(node: Node, tag_name: str) -> List[Node]:
    result = []
    if node.tag == tag_name:
        result.append(node)
    for child in node.children:
        if isinstance(child, Node):
            result.extend(find_all(child, tag_name))
    return result
