import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from chord import *

st.title("Chord Protocol Simulator")

# Input
n = st.slider("Number of Nodes", 3, 10, 5)
m = 4

node_ids = sorted(set([i*2 for i in range(n)]))

nodes = create_ring(node_ids, m)
build_finger_tables(nodes, m)

# Draw ring
G = nx.DiGraph()

for node in nodes:
    G.add_edge(node.id, node.successor.id)

pos = nx.circular_layout(G)

fig, ax = plt.subplots()
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", ax=ax)

st.pyplot(fig)

# Select node
selected_node = st.selectbox("Select Node", [node.id for node in nodes])

# Show finger table
node_obj = next(n for n in nodes if n.id == selected_node)

st.subheader("Finger Table")

finger_data = []
for i, finger in enumerate(node_obj.finger):
    finger_data.append((i, finger.id))

st.table(finger_data)

# Lookup
key = st.number_input("Enter Key", 0, 15)

if st.button("Run Lookup"):
    start = node_obj
    path = lookup(start, key)
    st.write("Lookup Path:", path)