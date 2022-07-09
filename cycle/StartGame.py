import constants
from game.casting.casting import *
from game.scripting.action import *
from game.directing.director import Director
from game.services.input_output import KeyboardService, VideoService
from game.shared.point import Point


def main():
    # create positions
    position1 = Point(int(constants.MAX_X/5), int(constants.MAX_Y/2))
    position2 = Point(int(constants.MAX_X*4/5), int(constants.MAX_Y/2))
    colorcycle1 = constants.RED
    colorcycle2 = constants.GREEN

    # create the cast
    cast = Cast()
    cast.add_actor("cycle1", Cycle(position1, colorcycle1))
    cast.add_actor("cycle2", Cycle(position2, colorcycle2))
    cast.add_actor("score1", Score("Player 1"))
    aux_position = Point(constants.MAX_X-7*constants.CELL_SIZE,0)
    score2 = Score("Player 2")
    score2.set_position(aux_position)
    cast.add_actor("score2", score2)

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlCycle1Action(keyboard_service))
    script.add_action("input", ControlCycle2Action(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction(video_service))
    script.add_action("update", TrailGrowthAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()