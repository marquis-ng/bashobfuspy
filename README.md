# bashobfuspy
Bash obfuscator written in Python

## Introduction
Obfuscate Bash scripts (and Shell scripts) using `eval` and variables.

## Installation
```bash
git clone https://github.com/marquis-ng/bashobfuspy
cd bashobfuspy
pip install .
# pip install .[full] # install completion module too
```

## Usage
### From command line
```bash
bashobfuspy --help # help
bashobfuspy infile.sh # read from infile.sh and output to stdout
bashobfuspy --outfile outfile.sh # read from stdin and output to outfile.sh
bashobfuspy -c 3 # set chunk size to 3
bashobfuspy -n # do not randomize variable order
```

### From Python
```python
import bashobfuspy
# bashobfuspy.obfuscate(content, chunk_size=4, rand=True)
bashobfuspy.obfuscate("apt update; apt upgrade") # obfuscate string
bashobfuspy.obfuscate("find /etc =type f", chunk_size=5) # set chunk size to 5
bashobfuspy.obfuscate("echo 'python is awesome!'", rand=False) # do not randomize variable order
```

## Note
This program can only *obfuscate* Bash scripts, not encrypting them. They can be easily deobfuscated by programmers who are familiar with Bash. So, do **NOT** store any sensitive information or passwords inside.
