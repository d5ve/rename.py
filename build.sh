#!/bin/bash

# Create README from rename.py

/usr/bin/pydoc ./rename.py | /usr/bin/grep -v 'Help on module rename:' > README
