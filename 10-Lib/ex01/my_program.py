#!/usr/bin/env python3
import sys

sys.path.append('./local_lib')

from path import Path

p = Path("/path/to/file")
print(f"Path: {p}")
print(f"Is this path a file? {p.is_file()}")
print(f"Is this path a directory? {p.is_dir()}")