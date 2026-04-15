# Chord Protocol Simulator

## 👩‍💻 Student Details
- Name: Mansha  
- Registration Number: 22MIC0162  

---

## 📌 Overview
This project simulates the Chord Peer-to-Peer Lookup Protocol using Python.

Chord is a Distributed Hash Table (DHT) that enables efficient key lookup in a decentralized peer-to-peer network. It organizes nodes in a circular ring and uses finger tables to perform fast lookups.

---

## ⚙️ Features
- Ring topology visualization  
- Finger table for each node  
- Key lookup simulation  
- Step-by-step routing animation  
- Hop count display  

---

## 🛠️ Technologies Used
- Python  
- SimPy  
- Streamlit  
- NetworkX  
- Matplotlib  

---

## 🧠 How It Works
- Nodes are arranged in a circular identifier space using consistent hashing.  
- Each node maintains a finger table containing references to other nodes.  
- During a lookup, the request is forwarded to the closest preceding node.  
- This reduces the number of hops required to locate a key.  
- The time complexity of lookup is **O(log N)**.  

---

## ▶️ How to Run

1. Install dependencies:
