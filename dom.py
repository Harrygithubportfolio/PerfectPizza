# perfectpizza/dom.py

from typing import Optional, List, Dict, Union

class Node:
    def __init__(self, tag: str, attrs: Dict[str, str], parent: Optional['Node'] = None):
        self.tag = tag
        self.attrs = attrs
        self.parent = parent
        self.children: List[Union['Node', str]] = []  # Can contain nested Nodes or text

    def add_child(self, child: Union['Node', str]):
        self.children.append(child)

    def __repr__(self):
        return f"<{self.tag} {' '.join(f'{k}={v}' for k,v in self.attrs.items())}>"

    def text(self) -> str:
        return "".join(c.text() if isinstance(c, Node) else c for c in self.children)
