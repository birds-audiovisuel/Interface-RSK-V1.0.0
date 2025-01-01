
def draw_field():
    """Renders the soccer field and returns the drawing as a string (SVG)."""
    svg_elements = []

    # Draw field boundaries
    svg_elements.append('<rect x="-1" y="-0.6" width="2" height="1.2" fill="none" stroke="white" stroke-width="0.02"/>')

    # Draw center circle
    svg_elements.append('<circle cx="0" cy="0" r="0.3" fill="none" stroke="black" stroke-width="0.02"/>')

    # Draw goals
    svg_elements.append('<rect x="-1" y="-0.4" width="0.4" height="0.8" fill="none" stroke="black" stroke-width="0.02"/>')
    svg_elements.append('<rect x="0.6" y="-0.4" width="0.4" height="0.8" fill="none" stroke="black" stroke-width="0.02"/>')

    # Draw additional static elements
    svg_elements.append('<line x1="-1" y1="-0.3" x2="-0.9" y2="-0.3" stroke="white" stroke-width="0.02"/>')
    svg_elements.append('<line x1="-1" y1="0.3" x2="-0.9" y2="0.3" stroke="white" stroke-width="0.02"/>')
    svg_elements.append('<line x1="1" y1="-0.3" x2="0.9" y2="-0.3" stroke="white" stroke-width="0.02"/>')
    svg_elements.append('<line x1="1" y1="0.3" x2="0.9" y2="0.3" stroke="white" stroke-width="0.02"/>')

    # Combine all SVG elements into a single SVG string
    svg_content = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="-1.1 -0.7 2.2 1.4" style="background-color: green;">' + ''.join(svg_elements) + '</svg>'
    return svg_content

def get_client_data():
    """Fetch the latest client data. Replace this with actual implementation."""
    # Example client data
    client = {
        'ball': [0, 0],
        'robot': {
            'green': {
                1: {'pose': [-0.5, 0, 0]},
                2: {'pose': [-0.5, 0.2, 0]}
            },
            'blue': {
                1: {'pose': [0.5, 0, 0]},
                2: {'pose': [0.5, 0.2, 0]}
            }
        }
    }
    return client

