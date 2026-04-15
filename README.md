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

2. Run the application:

3. Open the browser (if not opened automatically):
 
4. Use the interface:
- Select number of nodes  
- Choose a node  
- Enter a key  
- Click **Run Lookup** to see routing  

---

## 📊 Output
- Interactive ring visualization  
- Finger table display  
- Animated lookup path showing hop-by-hop routing  
- Number of hops taken for each lookup  

---

## 🎥 Demo Video
(Add your video link here)

---

## 📎 GitHub Repository
(Add your GitHub repository link here)

---

## 📌 Conclusion
This project demonstrates how the Chord protocol enables efficient and scalable distributed key lookups. By using finger tables and structured routing, the system achieves logarithmic lookup time, making it suitable for large peer-to-peer systems.
