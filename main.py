#!/usr/bin/env python3
"""
Main entry point for the application
"""

import sys
from utils import greet
from config import VERSION

def main():
    print(f"Starting application version {VERSION}")
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(greet(name))
    else:
        print("Hello, World!")

if __name__ == "__main__":
    main()
