from graphviz import Digraph

# Create a new directed graph
mindmap = Digraph("Recycling Collaboration Platform", format="png")
mindmap.attr(rankdir="TB", size="8,5")

# Core node
mindmap.node("Core", "Recycling Collaboration Platform", shape="ellipse", color="blue", style="filled", fontcolor="white")

# Major branches
branches = {
    "Behaviour": ["Works on phone and PC/laptop", "Runs in web browser", "Only authorised users edit data"],
    "Users' Needs": ["View recycling & reuse resource maps", "Post and search second-hand items", "Participate in community recycling projects", "Track regional rankings"],
    "Gamification": ["Earn points for activities", "Upload photos as proof", "Regional leaderboards"],
    "Data Features": ["View historical recycling rates", "Visualize reuse activity statistics", "Analyze trends by region"],
    "External Integration": ["Newsfeed on recycling policies", "API for external environmental data"],
}

# Add branches and subnodes
for branch, subnodes in branches.items():
    mindmap.node(branch, branch, shape="box", style="filled", color="lightblue")
    mindmap.edge("Core", branch)
    for subnode in subnodes:
        mindmap.node(subnode, subnode, shape="box", style="filled", color="lightyellow")
        mindmap.edge(branch, subnode)

# Save and render the mindmap
mindmap.render("Recycling_Collaboration_Mindmap", cleanup=True)
