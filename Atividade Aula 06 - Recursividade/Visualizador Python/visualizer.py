import pygame
from threading import Thread
import sys

WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
BLACK    = (  0,   0,   0)
GREEN    = (  0, 204,   0)
BLUE     = (  0,   0, 204)

BLUE_PROB = 0
WHITE_PROB = 1
BOTH = 2
GENERIC = 3

class Puzzle:
    def __init__(self, func):
        self.func = func
        self.problem_size = None
        self.pygame_running = False
        self.queue = []
        self.title = 'Self-Similarity in Algorithms'
        self.win_width = 1100
        self.win_height = 900
        self.start_y = 30
        self.start_x = 30
        self.bgcolor = BLACK
        self.goal_color = GREEN
        self.update_speed = 100
        self.scroll_speed = 200
        self.block_height = 30        
        self.y_offset = self.block_height + 6
        self.line_width_mult = 6
        self.scroll_up = 4
        self.scroll_down = 5
        self.cache = {}
        self.blue_problem = [42,34,30,23,19,15,12,11,8,7,4]
        self.white_problem = [51,50,42,32,30,22,21,20,11,10,8]
        self.both = self.blue_problem + self.white_problem
        self.curr_problem = None

    def __call__(self, gap, blocks, choices=[]):
        if self.problem_size is None:
            self._init_func(gap, blocks)

        if self.pygame_running == False:
            self.pygame_thread = Thread(target=self._run_game)
            self.pygame_thread.start()

        if self.curr_problem == BOTH:
            ret_val = self._memoized(gap, blocks, choices)
        else:
            ret_val = self.func(gap, blocks, choices)

        self._add_to_queue(gap, blocks, ret_val, choices)
        return ret_val

    def _init_func(self, gap, blocks):
        self.problem_size = gap
        self.curr_problem = self._find_curr(blocks)

    def _memoized(self, gap, blocks, choices):
        '''Currently borked - logic is incorrect'''
        key = (gap, tuple(blocks))
        if key in self.cache:
            ret_val = self.cache[key]
        else:
            ret_val = self.func(gap, blocks, choices)
            self.cache[key] = ret_val
        return ret_val

    def _find_curr(self, blocks):
        if blocks == self.blue_problem:
            curr = BLUE_PROB
            self.block_color = BLUE
        elif blocks == self.white_problem:
            curr = WHITE_PROB
            self.block_color = WHITE
        elif blocks == self.both:
            curr = BOTH
            self.block_color = WHITE
        else:
            curr = GENERIC
            self.block_curr = WHITE
        return curr

    def _add_to_queue(self, gap, blocks, ret_val, choices):
        if self.curr_problem == BOTH:
            success_condition = (gap == 0 or ret_val)
        else:
            success_condition = (gap == 0)
        if success_condition:
            self.queue.append((choices, True))
            print 'Success: {}'.format(choices)
        elif len(blocks) == 0 or gap < 0:
            print 'Failure: {}'.format(choices)
            self.queue.append((choices, False))

    def _run_game(self):
        self.pygame_running = True
        pygame.init()
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.win_width, self.win_height))
        self.screen.fill(self.bgcolor)

        to_draw = []
        curr_y = self.start_y
        scroll_unlocked = False

        while True:
            self.screen.fill(self.bgcolor)
            
            for event in pygame.event.get():
                if self._exiting(event):
                    self.pygame_running = False
                    pygame.quit()
                    sys.exit()
                if scroll_unlocked:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == self.scroll_up or event.button == self.scroll_down:
                            to_draw = self._move_blocks(to_draw, event.button, curr_y)


            if self.queue != []:
                next_choice = self.queue.pop(0)
                new_blockset = BlockSet(next_choice, curr_y, self.line_width_mult)
                to_draw.append(new_blockset)

                if curr_y >= self.win_height - self.block_height:
                    for blocks in to_draw:
                        blocks.upper_y -= self.y_offset
                else:
                    curr_y += self.y_offset
            else:
                scroll_unlocked = True

            for choice in to_draw:
                choice.draw(self.screen, self.start_x, self.block_height, self.block_color)

            # The goal line
            goal_x = (self.problem_size * self.line_width_mult) + self.start_x
            goal_pos = (goal_x, 0, 10, self.win_height)
            pygame.draw.rect(self.screen, self.goal_color, goal_pos)

            pygame.display.update()
            pygame.time.Clock().tick(self.update_speed)



    def _exiting(self, event):
        if event.type == pygame.QUIT:
            return True
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                return True
        else:
            return False

    def _move_blocks(self, blocks, button, max_height):
        if button == self.scroll_up:
            if blocks[0].upper_y < 0 + self.block_height:
                for blockset in blocks:
                    blockset.upper_y += self.scroll_speed
        elif button == self.scroll_down:
            if blocks[-1].upper_y > max_height - self.block_height:
                for blockset in blocks:
                    blockset.upper_y -= self.scroll_speed
        return blocks


class BlockSet:
    def __init__(self, blocks, upper_y, mult):
        self.blocks = blocks
        self.upper_y = upper_y
        self.success = GREEN
        self.width = 2 # The border width on the blocks
        self.line_width_mult = mult

    def draw(self, surface, start_x, height, color):
        curr_x = start_x
        if self.blocks[1]:
            color = self.success
        for block in self.blocks[0]:
            pos = (curr_x,
                   self.upper_y,
                   block * self.line_width_mult,
                   height)
            pygame.draw.rect(surface, color, pos)
            pygame.draw.rect(surface, BLACK, pos, self.width)
            curr_x += (block * self.line_width_mult)


# Constants and helper functions for the students

gap = 127
blue_problem = [42,34,30,23,19,15,12,11,8,7,4]
white_problem = [51,50,42,32,30,22,21,20,11,10,8]
both_problems = blue_problem + white_problem

number = len

def currentBlock(l):
    return l[0]

def blocksRemaining(l):
    return l[1:]

def addBlock(blocks, choices):
    return choices + [blocks[0]]
