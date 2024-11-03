import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.widgets import Button

# Function to handle button click events
def on_and_button_click(event):
    print("AND Gate clicked")

def on_or_button_click(event):
    print("OR Gate clicked")

def on_not_button_click(event):
    print("NOT Gate clicked")

# Create a figure and axes
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Interactive Logical Gates')

def draw_and_gate(ax):
    """Draw an AND gate."""
    ax.add_patch(patches.Polygon(((0, 0), (0.4, 0.3), (0.4, -0.3)), closed=True, edgecolor='black', facecolor='lightgrey'))
    ax.add_patch(patches.Circle((0.4, 0), 0.3, edgecolor='black', facecolor='lightgrey'))
    ax.plot([0.4, 0.8], [0.3, 0.3], color='black')
    ax.plot([0.4, 0.8], [-0.3, -0.3], color='black')
    ax.plot([0.8, 1.0], [0.3, 0.3], color='black')
    ax.plot([0.8, 1.0], [-0.3, -0.3], color='black')
    ax.text(0.6, 0.35, 'AND', fontsize=12)

def draw_or_gate(ax):
    """Draw an OR gate."""
    ax.add_patch(patches.Polygon(((0, 0.3), (0.4, 0.3), (0.4, -0.3), (0, -0.3)), closed=True, edgecolor='black', facecolor='lightgrey'))
    ax.add_patch(patches.Circle((0.4, 0), 0.3, edgecolor='black', facecolor='lightgrey'))
    ax.plot([0.4, 0.8], [0.3, 0.3], color='black')
    ax.plot([0.4, 0.8], [-0.3, -0.3], color='black')
    ax.plot([0.8, 1.0], [0.3, 0.3], color='black')
    ax.plot([0.8, 1.0], [-0.3, -0.3], color='black')
    ax.text(0.6, 0.35, 'OR', fontsize=12)

def draw_not_gate(ax):
    """Draw a NOT gate."""
    ax.add_patch(patches.Polygon(((0, 0.3), (0.4, 0.3), (0.4, -0.3), (0, -0.3)), closed=True, edgecolor='black', facecolor='lightgrey'))
    ax.add_patch(patches.Circle((0.4, 0), 0.1, edgecolor='black', facecolor='lightgrey'))
    ax.plot([0.4, 0.6], [0.3, 0.3], color='black')
    ax.plot([0.4, 0.6], [-0.3, -0.3], color='black')
    ax.plot([0.6, 0.8], [0.3, 0.3], color='black')
    ax.plot([0.6, 0.8], [-0.3, -0.3], color='black')
    ax.text(0.3, 0.35, 'NOT', fontsize=12)

# Draw gates
draw_and_gate(axs[0])
axs[0].set_title('AND Gate')
axs[0].set_xlim(-0.2, 1.2)
axs[0].set_ylim(-0.5, 0.5)
axs[0].set_aspect('equal')
axs[0].axis('off')

draw_or_gate(axs[1])
axs[1].set_title('OR Gate')
axs[1].set_xlim(-0.2, 1.2)
axs[1].set_ylim(-0.5, 0.5)
axs[1].set_aspect('equal')
axs[1].axis('off')

draw_not_gate(axs[2])
axs[2].set_title('NOT Gate')
axs[2].set_xlim(-0.2, 1.2)
axs[2].set_ylim(-0.5, 0.5)
axs[2].set_aspect('equal')
axs[2].axis('off')

# Add buttons for interaction
ax_button_and = plt.axes([0.1, 0.05, 0.1, 0.075])
ax_button_or = plt.axes([0.4, 0.05, 0.1, 0.075])
ax_button_not = plt.axes([0.7, 0.05, 0.1, 0.075])

button_and = Button(ax_button_and, 'AND Gate')
button_or = Button(ax_button_or, 'OR Gate')
button_not = Button(ax_button_not, 'NOT Gate')

button_and.on_clicked(on_and_button_click)
button_or.on_clicked(on_or_button_click)
button_not.on_clicked(on_not_button_click)

plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.show()
