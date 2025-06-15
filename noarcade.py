
"""
noarcade.py

A simple text-based implementation of Conway's Game of Life.
This script allows users to input starting cell coordinates and then simulate
the evolution of the cell population based on the rules of the game.
"""

class Cell:
    """
    Represents a single cell in the Game of Life.

    Attributes:
        x (int): The x-coordinate of the cell.
        y (int): The y-coordinate of the cell.
        neighbours (int): The number of live neighbours this cell has.
                          This is calculated during each step of the simulation.
    """
    def __init__(self,x,y):
        """
        Initializes a Cell object.

        Args:
            x (int): The x-coordinate of the cell.
            y (int): The y-coordinate of the cell.
        """
        self.x = x
        self.y = y
        self.neighbours = 0 # Initialized to 0, calculated each generation

class Game:
    """
    Manages the Game of Life simulation.

    This class handles the game state, including the list of live cells,
    the game field representation, and the simulation logic like evolving
    to the next generation and displaying the field.
    """
    def __init__(self):
        """
        Initializes the Game simulation.

        Sets up empty lists for cells and the field, initializes coordinate boundaries,
        prompts the user for initial cell coordinates, initializes these cells,
        calculates the initial field boundaries, and creates the initial field.
        """
        self.cells = [] # List to store all live Cell objects
        self.field = [] # 2D list representing the game field (grid)
        self.xmin, self.xmax, self.ymin, self.ymax = 0, 0, 0, 0 # Boundaries of live cells

        coordinates = self._create_cell_list_from_input()
        self._initialize_cells(coordinates)

        # Calculate initial boundaries only if there are live cells
        if self.cells:
            self.xmin = min(c.x for c in self.cells)
            self.xmax = max(c.x for c in self.cells)
            self.ymin = min(c.y for c in self.cells)
            self.ymax = max(c.y for c in self.cells)

        self._make_field() # Create the initial field representation

    def _create_cell_list_from_input(self):
        """
        Prompts the user for initial cell coordinates and returns them as a list of integers.

        Handles input validation for integer conversion and correct pairing of coordinates.
        Allows input like "1,2 3,4" or "1 2 3 4".
        Returns:
            list[int]: A flat list of integers representing coordinates, e.g., [x1, y1, x2, y2].
                       Returns an empty list if the user provides no input.
        """
        while True:
            a = input('Enter starting coordinates x,y for each cell separated by space (e.g., 1,2 3,4 or 0 0 0 1 1 1): ')
            c = a.split() # Split input string by spaces
            processed_coords = []

            if not c: # User entered nothing or only whitespace
                return [] # Assume "no cells" is valid if input is empty

            try:
                for item_str in c:
                    # Handle comma-separated pairs like "1,2"
                    if ',' in item_str:
                        parts = item_str.split(',')
                        if len(parts) == 2:
                            processed_coords.append(int(parts[0].strip()))
                            processed_coords.append(int(parts[1].strip()))
                        else: # Incorrect comma format like "1,2,3" or "1,"
                            raise ValueError("Coordinates should be in x,y format or single numbers forming pairs.")
                    elif item_str.strip(): # Handle space-separated single numbers
                        processed_coords.append(int(item_str.strip()))
                    # If item_str is empty or only whitespace after split (e.g. multiple spaces between numbers), it's ignored

            except ValueError as e:
                # Custom message for our specific format error, generic for int conversion
                if "Coordinates should be" in str(e):
                    print(f"Invalid input: {e}")
                else:
                    print("Invalid input: All coordinates must be valid integers.")
                print("Please try again.")
                continue # Ask for input again

            # Check if the total number of processed coordinates is even
            if len(processed_coords) % 2 != 0:
                print("Invalid input: Coordinates must be provided in x,y pairs. An odd number of values was entered.")
                print("Please try again.")
                continue

            return processed_coords # Return the validated list of coordinate integers

    def _initialize_cells(self, coordinates):
        """
        Initializes Cell objects from a list of coordinates and adds them to self.cells.

        Args:
            coordinates (list[int]): A flat list of integers (e.g., [x1, y1, x2, y2]).
        """
        i = 0
        while i < len(coordinates):
            # Create Cell objects from pairs of coordinates
            self.cells.append(Cell(coordinates[i], coordinates[i+1]))
            i += 2

    def _make_field(self):
        """
        Creates or updates the 2D grid representation (self.field) of the game.

        The field is sized to encompass all live cells with a 1-cell border around them.
        Live cells are placed onto this grid. Empty spots are initialized to 0.
        The field uses relative indexing based on self.xmin and self.ymin.
        """
        if not self.cells:  # Handle case with no initial or no live cells
            self.field = []
            return

        # Create a 2D list for the field. Dimensions are calculated based on min/max
        # coordinates of live cells, with a padding of 1 cell on each side (+3 total).
        # Row (y) dimension: self.ymax - self.ymin + 3
        # Column (x) dimension: self.xmax - self.xmin + 3
        self.field = [[0]*(self.xmax-self.xmin+3) for _ in range (self.ymax-self.ymin+3)]

        # Place Cell objects onto the field grid
        for cell_obj in self.cells:
            # Convert absolute cell coordinates to relative field coordinates
            # y_field = cell_obj.y - self.ymin + 1 (border)
            # x_field = cell_obj.x - self.xmin + 1 (border)
            self.field[cell_obj.y-self.ymin+1][cell_obj.x-self.xmin+1] = cell_obj

    def _modify(self, field_y, field_x):
        """
        Increments the neighbor count at a specific coordinate on the game field.

        If the specified coordinate on `self.field` contains a `Cell` object,
        its `neighbours` attribute is incremented. If it contains an integer
        (representing an empty spot), that integer value is incremented.
        This method directly modifies `self.field` or `Cell.neighbours`.

        Args:
            field_y (int): The y-coordinate on the `self.field` grid (relative index).
            field_x (int): The x-coordinate on the `self.field` grid (relative index).
        """
        # Check boundaries to ensure we are trying to modify a valid spot on the field
        if 0 <= field_y < len(self.field) and 0 <= field_x < len(self.field[0]):
            target = self.field[field_y][field_x]
            if isinstance(target, Cell): # If it's a live cell
                target.neighbours += 1 # Increment its own neighbour count
            elif isinstance(target, int): # If it's an empty spot (represented by an int)
                self.field[field_y][field_x] += 1 # Increment the count for this empty spot
            # No return needed as self.field (or cell.neighbours) is modified in place

    def _calculate_neighbor_counts(self):
        """
        Calculates and updates neighbor counts for all cells and relevant empty spots.

        Iterates through each live cell in `self.cells`. For each live cell,
        it increments the neighbor count for the cell itself and its 8 surrounding
        neighbors on `self.field` using the `_modify` method.
        This means `Cell.neighbours` will store its own count + true neighbors,
        and empty spots on `self.field` (integers) will store their true neighbor count.
        """
        if not self.field: return # Skip if field is not initialized (e.g. no cells)

        for cell in self.cells:
            # Convert absolute cell coordinates to relative field coordinates
            # The +1 accounts for the border around the live cell area in the field
            field_cell_y = cell.y - self.ymin + 1
            field_cell_x = cell.x - self.xmin + 1

            # Iterate over the 3x3 grid centered on the current live cell
            # This includes the cell itself and its 8 neighbours.
            for dy in [-1, 0, 1]:      # Delta y (row offset)
                for dx in [-1, 0, 1]:  # Delta x (column offset)
                    # Call _modify for the cell and each of its 8 neighbours
                    self._modify(field_cell_y + dy, field_cell_x + dx)


    def _apply_rules_and_identify_changes(self):
        """
        Applies Conway's Game of Life rules to identify cells that die and new cells that are born.

        Iterates over `self.field`.
        - For existing `Cell` objects:
            - Checks `cell.neighbours`. A cell survives if `cell.neighbours` is 3 or 4
              (meaning 2 or 3 true neighbors, because `_calculate_neighbor_counts` also
              increments the cell's own `neighbours` attribute).
            - Cells not meeting survival criteria are added to `cells_to_die`.
            - `cell.neighbours` is reset to 0 for the next generation.
        - For integer spots (empty):
            - If the integer value is 3 (meaning 3 true neighbors), new cell coordinates
              are added to `coords_for_new_cells`.

        Returns:
            tuple: A tuple containing two lists: `(cells_to_die, coords_for_new_cells)`.
                   `cells_to_die` contains `Cell` objects.
                   `coords_for_new_cells` contains `(x, y)` tuples for new cells.
        """
        cells_to_die = []
        coords_for_new_cells = []

        if not self.field: return cells_to_die, coords_for_new_cells # Should not happen if evolve checks first

        # Iterate over each spot in the game field
        for y_idx, row in enumerate(self.field):
            for x_idx, item in enumerate(row):
                if isinstance(item, Cell): # If the spot contains a live cell
                    # Game of Life rules for survival:
                    # `item.neighbours` includes the cell itself.
                    # Survives with 2 or 3 actual neighbours (so item.neighbours will be 3 or 4).
                    if not (item.neighbours == 3 or item.neighbours == 4):
                        cells_to_die.append(item)
                    item.neighbours = 0  # Reset for the next generation's count

                elif isinstance(item, int): # If the spot is empty (contains an integer)
                    # Game of Life rules for birth:
                    # An empty spot with exactly 3 neighbours becomes a live cell.
                    # The integer `item` here directly represents the number of true neighbours.
                    if item == 3:
                        # Convert relative field coordinates back to absolute world coordinates
                        abs_x = x_idx + self.xmin - 1 # -1 to adjust for the border
                        abs_y = y_idx + self.ymin - 1 # -1 to adjust for the border
                        coords_for_new_cells.append((abs_x, abs_y))
        return cells_to_die, coords_for_new_cells

    def _update_cell_list(self, cells_to_die, coords_for_new_cells):
        """
        Updates `self.cells` by removing dead cells and adding newly born cells.

        Args:
            cells_to_die (list[Cell]): A list of `Cell` objects to remove.
            coords_for_new_cells (list[tuple[int, int]]): A list of (x,y) coordinates for new cells.
        """
        # Remove dead cells from the main list of live cells
        for cell_to_remove in cells_to_die:
            # Ensure the cell is still in the list before trying to remove
            # (could be relevant in more complex scenarios, good practice)
            if cell_to_remove in self.cells:
                self.cells.remove(cell_to_remove)

        # Add newly born cells to the main list
        for x, y in coords_for_new_cells:
            self.cells.append(Cell(x, y)) # Create new Cell objects

    def evolve(self):
        """
        Evolves the game state to the next generation.

        This method orchestrates the steps:
        1. Handles the case of no live cells (returns early).
        2. Calculates neighbor counts for all cells and relevant empty spots.
        3. Applies Game of Life rules to determine cells that die and new cells that are born.
        4. Updates the list of live cells (`self.cells`).
        5. If live cells remain, recalculates coordinate boundaries and rebuilds `self.field`.
        6. If all cells die, resets the field and boundaries.
        """
        # If there are no live cells, there's nothing to evolve.
        if not self.cells:
            self.field = [] # Ensure field is empty
            self.xmin, self.xmax, self.ymin, self.ymax = 0, 0, 0, 0 # Reset boundaries
            return

        # Step 1: Calculate neighbor counts. This modifies `Cell.neighbours` and integer
        # values on `self.field` representing counts for empty spots.
        self._calculate_neighbor_counts()

        # Step 2: Apply rules based on counts and identify cells to die and new cell coordinates.
        # Also resets `Cell.neighbours` to 0 for all live cells.
        cells_to_die, coords_for_new_cells = self._apply_rules_and_identify_changes()

        # Step 3: Update the master list of live cells (`self.cells`).
        self._update_cell_list(cells_to_die, coords_for_new_cells)

        # Step 4: Recalculate boundaries and rebuild the field representation
        # if there are still live cells.
        if self.cells:
            self.xmin = min(c.x for c in self.cells)
            self.xmax = max(c.x for c in self.cells)
            self.ymin = min(c.y for c in self.cells)
            self.ymax = max(c.y for c in self.cells)
            self._make_field()  # Rebuild self.field with new cells and new dimensions
        else:
            # All cells died in this generation
            self.field = [] # Clear the field
            self.xmin, self.xmax, self.ymin, self.ymax = 0, 0, 0, 0 # Reset boundaries

    def display_field(self):
        """
        Prints the current state of the game field to the console.

        'C' represents a live cell.
        Integers represent the number of live neighbors for an empty spot
        (this is a transient state during calculation, usually 0 for truly empty spots
        in the final display of a stable or intermediate generation).
        """
        if not self.field:
            print("Field is empty.") # Message if there are no cells or field isn't made
            return

        # Iterate through each row and then each item in the row to print
        for i in range(len(self.field)):
            for t in range(len(self.field[0])):
                if isinstance(self.field[i][t],Cell):
                    print("C", end=" ") # Print 'C' for a live Cell object
                else:
                    print(self.field[i][t], end=" ") # Print the integer value for an empty spot
            print(" ") # Newline after each row

# Main simulation logic
if __name__ == "__main__":
    # Create a Game instance. This will also prompt for initial cell input.
    game = Game()

    # Check if any cells were actually initialized.
    # _create_cell_list_from_input returns [] if user enters nothing,
    # which means game.cells will be empty.
    if not game.cells:
        print("No initial cells provided or input was empty. Simulation will not start.")
        exit() # Exit the script if no cells to simulate

    print("\nInitial field:")
    game.display_field() # Display the starting state of the game

    # Main simulation loop
    while True:
        command = input("Press 'c' to continue simulation, 'q' to quit: ").strip().lower()

        if command == "q":
            print("Life simulation is over.")
            break # Exit the loop, ending the simulation
        elif command == "c":
            game.evolve() # Evolve the game to the next generation

            # Check if all cells have died
            if not game.cells:
                print("\nAll cells have died. Simulation ended.")
                game.display_field() # Display the final empty field
                break # Exit the loop

            print("\nNext generation:")
            game.display_field() # Display the new state
        else:
            # Handle invalid commands
            print("Invalid command. Please enter 'c' or 'q'.")
            continue # Ask for input again

