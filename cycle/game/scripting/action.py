from game.shared.point import Point
from game.casting.casting import Cycle
from game.shared.point import Point
from game.casting.casting import *
import random
import constants
import pyray

class Action:
    """A thing that is done.

    The responsibility of action is to do somthing that is integral or important in the game. Thus,
    it has one method, execute(), which should be overridden by derived classes.
    """

    def execute(self, cast, script):
        """Executes something that is important in the game. This method should be overriden by 
        derived classes.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        pass
 
class ControlCycle1Action(Action):
    """
    An input action that controls the cycles.

    The responsibility of ControlActorsAction is to get the direction and move the cycles.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -constants.CELL_SIZE)
        #self._direction = Point(0, 0)

    def set_direction(self, direction):
        self._direction = direction

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)

        cycle1 = cast.get_first_actor("cycle1")
        cycle1.turn_head(self._direction)


class ControlCycle2Action(Action):
    """
    An input action that controls the cycles.

    The responsibility of ControlActorsAction is to get the direction and move the cycles.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.

        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -constants.CELL_SIZE)
    
    def set_direction(self, direction):
        self._direction = direction

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        # left
        if self._keyboard_service.is_key_down('j'):
            self._direction = Point(-constants.CELL_SIZE, 0)

        # right
        if self._keyboard_service.is_key_down('l'):
            self._direction = Point(constants.CELL_SIZE, 0)

        # up
        if self._keyboard_service.is_key_down('i'):
            self._direction = Point(0, -constants.CELL_SIZE)

        # down
        if self._keyboard_service.is_key_down('k'):
            self._direction = Point(0, constants.CELL_SIZE)

        cycle2 = cast.get_first_actor("cycle2")
        cycle2.turn_head(self._direction)
class DrawActorsAction(Action):
    """
    An output action that draws all the actors.

    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.

        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def reset(self, cast, script):
        """Resets the initial position of the cycles for a new round.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self.execute(cast, script)
        pyray.wait_time(5000)
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        cast.remove_actor("cycle1", cycle1)
        cast.remove_actor("cycle2", cycle2)
        message = cast.get_first_actor("messages")
        cast.remove_actor("messages", message)
        
        # create positions
        position1 = Point(int(constants.MAX_X/5), int(constants.MAX_Y/2))
        position2 = Point(int(constants.MAX_X*4/5), int(constants.MAX_Y/2))
        colorcycle1 = constants.RED
        colorcycle2 = constants.GREEN
        cast.add_actor("cycle1", Cycle(position1, colorcycle1))
        cast.add_actor("cycle2", Cycle(position2, colorcycle2))
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")

        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        
        segments1 = cycle1.get_segments()
        segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
        #set a timer

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        segments1 = cycle1.get_segments()
        segments2 = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)
        self._video_service.draw_actor(score1)
        self._video_service.draw_actor(score2)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()

class MoveActorsAction(Action):
    """
    An update action that moves all the actors.

    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when the cycles collides
    with the each other, or the cycle collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """


    def __init__(self, video_service):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._cycle1_wins = False
        self._cycle2_wins = False
        self._video_service = video_service
    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        if not self._is_game_over:
            self._handle_cycle_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)

    def _handle_cycle_collision(self, cast):
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")

        for segment1 in segments1:
            if head2.get_position().equals(segment1.get_position()):
                self._cycle1_wins = True
                self._is_game_over = True
                score1.add_points(1)

        for segment2 in segments2:
            if head1.get_position().equals(segment2.get_position()):
                self._cycle2_wins = True
                self._is_game_over = True
                score2.add_points(1)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        cycle2 = cast.get_first_actor("cycle2")
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]
        
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        
        for segment1 in segments1:
            if head1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
                self._cycle2_wins = True
                score2.add_points(1)
        for segment2 in segments2:
            if head2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
                self._cycle1_wins = True
                score1.add_points(1)

    def _handle_game_over(self, cast, script):
        """Shows who won this round message and turns the cycles white if it have a winer of this round.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        if self._is_game_over:
            cycle1 = cast.get_first_actor("cycle1")
            segments1 = cycle1.get_segments()
            cycle2 = cast.get_first_actor("cycle2")
            segments2 = cycle2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            if self._cycle1_wins:
                message.set_text(f"{score1.get_player()} wins this round!")
                self._cycle1_wins = False
            else:
                message.set_text(f"{score2.get_player()} wins this round!")
                self._cycle2_wins = False
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment1 in segments1:
                segment1.set_color(constants.WHITE)
            for segment2 in segments2:
                segment2.set_color(constants.WHITE)
            
            my_script = script.get_actions("output")[0]
            control1 = script.get_actions("input")[0]
            control2 = script.get_actions("input")[1]
            control1.set_direction(Point(0, -constants.CELL_SIZE))
            control2.set_direction(Point(0, -constants.CELL_SIZE))
            self._is_game_over = False
            
            my_script.reset(cast, script)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one of its segments.

        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]
        cycle2 = cast.get_first_actor("cycle2")
        head2 = cycle2.get_segments()[0]
        segments2 = cycle2.get_segments()[1:]

        for segment1 in segments1:
            if head1.get_position().equals(segment1.get_position()):
                self._is_game_over = True
        for segment2 in segments2:
            if head2.get_position().equals(segment2.get_position()):
                self._is_game_over = True
class TrailGrowthAction(Action):

    def __init__(self):
        self._counter = 0

    def execute(self, cast, script):
        """Executes the trail growth action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        self._counter += 1
        self._handle_trail_growth(cast)

    def _handle_trail_growth(self, cast):
        """Updates the cycle by adding itself more tails 
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle1 = cast.get_first_actor("cycle1")
        cycle2 = cast.get_first_actor("cycle2")

        rnumber = random.randint(101, 500)
        if self._counter > rnumber:
            cycle1.grow_tail(constants.GROW_TAIL_RATE)
            cycle2.grow_tail(constants.GROW_TAIL_RATE)
            self._counter = 0

class Script:
    """A collection of actions.

    The responsibility of Script is to keep track of a collection of actions. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actions (dict): A dictionary of actions { key: group_name, value: a list of actions }
    """

    def __init__(self):
        """Constructs a new Action."""
        self._actions = {}

    def add_action(self, group, action):
        """Adds an action to the given group.

        Args:
            group (string): The name of the group.
            action (Action): The action to add.
        """
        if not group in self._actions.keys():
            self._actions[group] = []

        if not action in self._actions[group]:
            self._actions[group].append(action)

    def get_actions(self, group):
        """Gets the actions in the given group.

        Args:
            group (string): The name of the group.

        Returns:
            List: The actions in the group.
        """
        results = []
        if group in self._actions.keys():
            results = self._actions[group].copy()
        return results

    def remove_action(self, group, action):
        """Removes an action from the given group.

        Args:
            group (string): The name of the group.
            action (Action): The action to remove.
        """
        if group in self._actions:
            self._actions[group].remove(action)