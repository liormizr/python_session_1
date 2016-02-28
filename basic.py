from __future__ import print_function
import itertools
import functools

team_members = [
    'Gol',
    'Nir',
    'NirC',
    'Dan',
    'Ran',
    'Avia',
    'Noa',
]


def display_team_members():
    # Do not:
    for index in xrange(len(team_members)):
        print('Team Member: {}'.format(team_members[index]))

    # In reverse order
    for index in xrange(len(team_members) - 1, -1, -1):
        print('Team Member: {}'.format(team_members[index]))

    # Do instead:
    for team_member in team_members:
        print('Team Member: {}'.format(team_member))

    # In reverse order
    for team_member in reversed(team_members):
        print('Team Member: {}'.format(team_member))


def display_team_members_in_order():
    for team_member in sorted(team_members):
        print('Team Member: {}'.format(team_member))

    # With reverse order
    for team_member in sorted(team_members, reverse=True):
        print('Team Member: {}'.format(team_member))

    def compare_length(first_member, second_member):
        if len(first_member) < len(second_member):
            return -1
        if len(first_member) > len(second_member):
            return 1
        return 0

    # Do not:
    for team_member in sorted(team_members, cmp=compare_length):
        print('Team Member: {}'.format(team_member))

    # Do instead:
    for team_member in sorted(team_members, key=len):
        print('Team Member: {}'.format(team_member))


def display_team_members_with_index():
    # Do not:
    for index in xrange(len(team_members)):
        print('{index}: Team Member: {name}'.format(
            index=index, name=team_members[index]))

    # Do instead:
    for index, team_member in enumerate(team_members):
        print('{index}: Team Member: {name}'.format(
            index=index, name=team_member))

    # BTW: enumerate have a second argument
    for index, team_member in enumerate(team_members, start=1):
        print('{index}: Team Member: {name}'.format(
            index=index, name=team_member))


def puzzle_for_every_team_member():
    puzzle_games = [
        'PuzzleGame1',
        'PuzzleGame2',
        'PuzzleGame3',
        'PuzzleGame4',
        'PuzzleGame5',
        'PuzzleGame6',
        'PuzzleGame7',
    ]

    # Do not:
    number = min(puzzle_games, team_members)
    for index in xrange(number):
        print('Team Member: {} get: {}'.format(
            team_members[index], puzzle_games[index]))

    # Do instead:
    for puzzle_game, team_member in zip(puzzle_games, team_members):
        print('Team Member: {} get: {}'.format(team_member, puzzle_game))

    # Very Good!!!:
    for puzzle_game, team_member in itertools.izip(puzzle_games, team_members):
        print('Team Member: {} get: {}'.format(team_member, puzzle_game))


def read_from_file(file_obj):
    # Do not
    blocks = []
    while True:
        block = file_obj.read(32)
        if block == '':
            break
        blocks.append(block)

    # 50%
    blocks = []
    for block in iter(functools.partial(file_obj.read, 32), ''):
        blocks.append(block)

    # Do instead
    blocks = [
        block
        for block in iter(functools.partial(file_obj.read, 32), '')
    ]


def find_target_in_sequence(sequence, target):
    # Do not
    found_flag = False
    for index, value in enumerate(sequence):
        if value == target:
            found_flag = True
            break
    if not found_flag:
        result = None
    else:
        result = index

    # Do instead
    for index, value in enumerate(sequence):
        if value == target:
            result = index
            break
    else:
        result = None

