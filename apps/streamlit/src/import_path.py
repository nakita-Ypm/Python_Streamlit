import sys
import os


def import_path(path):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    import_path = os.path.abspath(os.path.join(current_dir, path))
    sys.path.append(import_path)
