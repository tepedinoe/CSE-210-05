import constants

class Actor:
    """A visible, moveable thing that participates in the game. 

    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _text (string): The text to display
        _font_size (int): The font size to use.
        _color (Color): The color of the text.
        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._text = ""
        self._font_size = 15
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)

    def get_color(self):
        """Gets the actor's color as a tuple of three ints (r, g, b).

        Returns:
            Color: The actor's text color.
        """
        return self._color

    def get_font_size(self):
        """Gets the actor's font size.

        Returns:
            Point: The actor's font size.
        """
        return self._font_size

    def get_position(self):
        """Gets the actor's position in 2d space.

        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_text(self):
        """Gets the actor's textual representation.

        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.

        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.

        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % constants.MAX_X
        y = (self._position.get_y() + self._velocity.get_y()) % constants.MAX_Y
        self._position = Point(x, y)

    def set_color(self, color):
        """Updates the color to the given one.

        Args:
            color (Color): The given color.
        """
        self._color = color

    def set_position(self, position):
        """Updates the position to the given one.

        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_font_size(self, font_size):
        """Updates the font size to the given one.

        Args:
            font_size (int): The given font size.
        """
        self._font_size = font_size

    def set_text(self, text):
        """Updates the text to the given value.

        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the velocity to the given one.

        Args:
            velocity (Point): The given velocity.
        """
        self._velocity = velocity
class Color:
    """A color.

    The responsibility of Color is to hold and provide information about itself. Color has a few 
    convenience methods for comparing them and converting to a tuple.

    Attributes:
        _red (int): The red value.
        _green (int): The green value.
        _blue (int): The blue value.
        _alpha (int): The alpha or opacity.
    """

    def __init__(self, red, green, blue, alpha = 255):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.

        Args:
            red (int): A red value.
            green (int): A green value.
            blue (int): A blue value.
            alpha (int): An alpha or opacity.
        """
        self._red = red
        self._green = green
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, blue, alpha).

        Returns:
            Tuple(int, int, int, int): The color as a tuple.
        """
        return (self._red, self._green, self._blue, self._alpha)

class Point:
    """A distance from a relative origin (0, 0).

    The responsibility of Point is to hold and provide information about itself. Point has a few 
    convenience methods for adding, scaling, and comparing them.

    Attributes:
        _x (integer): The horizontal distance from the origin.
        _y (integer): The vertical distance from the origin.
    """

    def __init__(self, x, y):
        """Constructs a new Point using the specified x and y values.

        Args:
            x (int): The specified x value.
            y (int): The specified y value.
        """
        self._x = x
        self._y = y

    def add(self, other):
        """Gets a new point that is the sum of this and the given one.

        Args:
            other (Point): The Point to add.

        Returns:
            Point: A new Point that is the sum.
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """Whether or not this Point is equal to the given one.

        Args:
            other (Point): The Point to compare.

        Returns: 
            boolean: True if both x and y are equal; false if otherwise.
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """Gets the horizontal distance.

        Returns:
            integer: The horizontal distance.
        """
        return self._x

    def get_y(self):
        """Gets the vertical distance.

        Returns:
            integer: The vertical distance.
        """
        return self._y

    def reverse(self):
        """Reverses the point by inverting both x and y values.

        Returns:
            Point: A new point that is reversed.
        """
        new_x = self._x * -1
        new_y = self._y * -1
        return Point(new_x, new_y)

    def scale(self, factor):
        """
        Scales the point by the provided factor.

        Args:
            factor (int): The amount to scale.

        Returns:
            Point: A new Point that is scaled.
        """
        return Point(self._x * factor, self._y * factor)

class Score(Actor):
    """
    A record of points made or lost. 

    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, player):
        super().__init__()
        self._points = 0
        self._player = player
        #self._is_playing = True
        self.add_points(0)

    # def get_game_state(self):
    #     return self._is_playing

    def get_text(self):
        return f"{self._player}: {self._points}"

    def get_player(self):
        return self._player

    def get_points(self):
        return self._points

    def add_points(self, points):
        """Adds the given points to the score's total points.

        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")

class Cast:
    """A collection of actors.

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
   
    def add_actor(self, group, actor):
        """Adds an actor to the given group.

        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        if not group in self._actors.keys():
            self._actors[group] = []

        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """Gets the actors in the given group.

        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results

    def get_all_actors(self):
        """Gets all of the actors in the cast.

        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """Gets the first actor in the given group.

        Args:
            group (string): The name of the group.

        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    def remove_actor(self, group, actor):
        """Removes an actor from the given group.

        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)
class Cycle(Actor):
    """
    A long limbless reptile.

    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self, position, colorcycle):
        super().__init__()
        self._segments = []
        self._prepare_body(position, colorcycle)

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self, position, colorcycle):
        x = position.get_x()
        y = position.get_y()

        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
            color=colorcycle

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            color = tail.get_color()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_text("#")
            segment.set_color(color)
            segment.set_velocity(velocity)
            segment.set_position(position)
            self._segments.append(segment)
