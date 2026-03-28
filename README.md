
📔 Mini-Diary (v0)
A Constraint-Driven CLI Architecture for Persistent Logging
📖 Overview
Mini-Diary is a high-performance Command-Line Interface (CLI) tool specifically engineered to demonstrate that complex software logic—such as data persistence and unique ID tracking—can be achieved under extreme programming limitations.

Developed as part of the Software Engineering curriculum at Samsun University, this project serves as a technical proof-of-concept for high-efficiency file I/O operations without relying on modern data structures.

🚀 Key Features & Innovation (v0)
🛠️ Constraint-Driven Logic
The core architecture is strictly built upon a "Zero-Collection" policy. This system successfully manages persistent data WITHOUT using:

❌ Iterative Loops (for, while)

❌ Structured Collections (list, dict, set)

📁 Hidden Persistence Engine
The application implements an automated environment setup by creating a concealed .minidiary directory. This ensures that the database remains isolated from the main workspace, maintaining a clean and professional file structure.

⚡ Smart ID Synchronization
The system features a Newline-Scanning (\n) algorithm. By analyzing the raw file stream in real-time, it calculates the next unique Entry ID on-the-fly. This ensures data integrity and absolute ID consistency without consuming excessive memory.

📝 Instant Append Protocol
Utilizing optimized file-stream append modes, the tool ensures that every new entry is committed directly to the diary.dat file, preserving the full historical record while maintaining millisecond-level execution speeds.
