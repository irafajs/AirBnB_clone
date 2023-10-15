#!/usr/bin/python3
"""
Shebang to create a PY script
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
