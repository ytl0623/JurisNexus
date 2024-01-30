import networkx as nx
from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,
                          ColumnDataSource, OpenURL, TapTool, Bezier, Rect, Text, Arc, Ellipse)
from bokeh.plotting import from_networkx, figure, output_file, show

# Prepare Data
G = nx.Graph()
G.add_edge(1, 3)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(1, 6)
G.add_edge(2, 7)
G.add_edge(4, 8)
G.add_edge(5, 9)
G.add_edge(3, 10)

# explicitly set positions
pos = {1: (0, 0), 2: (0, 0.3), 3: (2, 0.15), 4: (4, 0.3), 5: (4, 0), 6: (-1, 0), 7: (-1, 0.3), 8: (5, 0.3), 9: (5, 0), 10: (4, 0.15)}

# set urls as node attributes
urls = {
    1: "https://google.com",
    2: "https://facebook.com",
    3: "https://www.instagram.com/",
    4: "https://www.youtube.com/",
    5: "https://tw.yahoo.com/"
}

nx.set_node_attributes(G, urls, "URL")

# Show with Bokeh
p = figure(width=1400, height=700,
           x_range=Range1d(-2, 6), y_range=Range1d(-0.2, 0.5),
           tools="tap",
           x_axis_location =None,  # Hide the x-axis
           y_axis_location =None,  # Hide the y-axis
           )

# Configure node hover tool and add tools
node_hover_tool = HoverTool(tooltips=[("URL", "@URL")])
p.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

# Configure tap tool
url = "@URL"
taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

graph_renderer = from_networkx(G, pos, scale=1.0, center=(0, 0))

graph_renderer.node_renderer.glyph = Ellipse(width=0.5, height=0.05, fill_color="white",
                                           line_color = "black", line_width = 1)
                                           
graph_renderer.edge_renderer.glyph = MultiLine(line_color="black", line_alpha=1,
                                               line_width=1)

p.renderers.append(graph_renderer)

output_file("0913.html")
show(p)