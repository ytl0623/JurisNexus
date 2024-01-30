import networkx as nx
from bokeh.io import output_file, show
from bokeh.models import (BoxZoomTool, Circle, HoverTool,
                          MultiLine, Plot, Range1d, ResetTool,
                          ColumnDataSource, OpenURL, TapTool)
from bokeh.plotting import from_networkx, figure, output_file, show


# Prepare Data
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 5)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)

# explicitly set positions
pos = {1: (0, 0), 2: (-1, 0.3), 3: (2, 0.17), 4: (4, 0.255), 5: (5, 0.03)}

# set urls as node attributes
urls = {
    1: "https://stackoverflow.com/questions/69456723/networkx-add-hyperlink-to-each-node",
    2: "https://facebook.com",
    3: "https://google.com",
    4: "Test",
    5: "Test"

}
nx.set_node_attributes(G, urls, "URL")

# Show with Bokeh
p = figure(width=400, height=400,
           x_range=Range1d(-2, 6), y_range=Range1d(-0.2, 0.5),
           tools="tap", title="Click the URL")

# Configure node hover tool and add tools
node_hover_tool = HoverTool(tooltips=[("URL", "@URL")])
p.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

# Configure tap tool
url = "@URL"
taptool = p.select(type=TapTool)
taptool.callback = OpenURL(url=url)

graph_renderer = from_networkx(G, pos, scale=0.5, center=(0, 0))

graph_renderer.node_renderer.glyph = Circle(size=15, fill_color="white",
                                            line_color="black", line_width=1)
graph_renderer.edge_renderer.glyph = MultiLine(line_color="black", line_alpha=1,
                                               line_width=1)
p.renderers.append(graph_renderer)

output_file("interactive_graphs.html")
show(p)