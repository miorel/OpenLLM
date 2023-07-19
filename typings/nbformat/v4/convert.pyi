from typing import Any

from _typeshed import Incomplete
from nbformat import v3 as v3
from nbformat import validator as validator

from .nbbase import NotebookNode as NotebookNode
from .nbbase import nbformat as nbformat
from .nbbase import nbformat_minor as nbformat_minor
from .nbbase import random_cell_id as random_cell_id

def upgrade(nb: NotebookNode, from_version: Incomplete | None = ..., from_minor: Incomplete | None = ...) -> Any: ...
def upgrade_cell(cell: NotebookNode) -> Any: ...
def downgrade_cell(cell: NotebookNode) -> Any: ...
def to_mime_key(d: Any) -> Any: ...
def from_mime_key(d: Any) -> Any: ...
def upgrade_output(output: Any) -> Any: ...
def downgrade_output(output: Any) -> Any: ...
def upgrade_outputs(outputs: Any) -> Any: ...
def downgrade_outputs(outputs: Any) -> Any: ...
def downgrade(nb: NotebookNode) -> Any: ...