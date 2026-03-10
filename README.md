# Santa Compressor (Huffman Coding)

A Python implementation of lossless data compression using Huffman Coding algorithms. 

![Santa Compressor Terminal Demo]([Insert Image/Result Here])

## Overview

This repository demonstrates fundamental Computer Science algorithm implementation. By utilizing variable-length prefix coding (Huffman Trees), this program efficiently encodes and decodes text files, significantly reducing storage footprint for redundant characters without any loss of data.

## Contents
- `encode.py`: Parses the input text, generates the frequency dictionary, builds the Huffman Tree, and serializes the compressed `.huf` binary output.
- `decode.py`: Deserializes the `.huf` binary along with its tree metadata to perfectly reconstruct the original text.
- `input.txt` & `encoded.huf`: Sample input payloads and their corresponding compressed outputs.

## Usage

**To Compress (Encode):**
```bash
python encode.py input.txt
```
*This will generate `encoded.huf` containing the compressed binary.*

**To Decompress (Decode):**
```bash
python decode.py encoded.huf
```
*This will reconstruct the exact content of the original dataset.*
