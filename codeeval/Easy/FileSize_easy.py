# https://www.codeeval.com/open_challenges/26/
# File Size

# CHALLENGE DESCRIPTION:

# Print the size of a file in bytes.
import sys
import os 

file_size = os.path.getsize(sys.argv[1])
print(file_size)