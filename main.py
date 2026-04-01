import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from datalog.nrdatalog2sql import main

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py datalog.dl tbox_name.txt")
        sys.exit(1)
    main(sys.argv)
