# Interactive Logical Gates with Matplotlib

This Python code creates an interactive GUI using `matplotlib` to display three logical gates: AND, OR, and NOT. Each gate is drawn in a separate subplot, and buttons below the gates allow user interaction.

## Code Breakdown

1. **Import Statements**
   - `matplotlib.pyplot` and `matplotlib.patches` for drawing the gates.
   - `Button` from `matplotlib.widgets` for adding clickable buttons.

2. **Event Handler Functions**
   - `on_and_button_click`, `on_or_button_click`, and `on_not_button_click` print messages when the respective gate button is clicked.

3. **Drawing Logical Gates**
   - Each gate (AND, OR, NOT) has its own function (`draw_and_gate`, `draw_or_gate`, `draw_not_gate`).
   - Gates are drawn using `Polygon` and `Circle` patches and basic shapes to represent each gate accurately.

4. **Creating the Figure and Subplots**
   - The code creates a `figure` with three subplots for the AND, OR, and NOT gates.
   - Each gate is drawn and labeled in a separate subplot, with specific axis settings to remove the default grid and ensure the gates fit nicely.

5. **Adding Buttons**
   - Three buttons (`AND Gate`, `OR Gate`, `NOT Gate`) are positioned below the gates.
   - The `on_clicked` method links each button to its respective event handler function, allowing interactions.

6. **Display**
   - The `plt.tight_layout(rect=[0, 0.1, 1, 1])` call ensures that the layout is properly aligned within the display area.
   - `plt.show()` starts the event loop, displaying the figure and buttons.

When run, this code will display a figure with three logical gates and allow users to click on each gate's button, which triggers the respective event handler, printing messages to the console.
