#!/usr/bin/python3
"""initialize"""

from models.engine.file_storage import FileStorage


"""retrive stotage"""
storage = FileStorage()
storage.reload()
