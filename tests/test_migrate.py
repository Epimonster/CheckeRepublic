import os
from io import StringIO
from parsing.migrate import RCF2PDN


def test_migrate_first_position_description_string():
    desc = "**Key Ending 10: First Position**\n\n" + \
           "//Summary//\n\n" + \
           "Force: 2 v 2.\n" + \
           "Opposition: White has it.\n" + \
           "Terms: White to move and win.\n" + \
           "Description: The diagrammed position represents a late, and critical, phase of\n" + \
           "First Position. Before tackling the winning procedure, it would be wise for the\n" + \
           "student to take note of those features which distinguish First Position from a\n" + \
           "nondescript two against two setting. In this way he will be able to recognize it\n" + \
           "in its early stages, and take the appropriate action. Aside from the attacker,\n" + \
           "having the Opposition, here White, the following conditions must also hold:\n" + \
           "# At least one of the defender's pieces is a single man rather than a king.\n" + \
           "# The attacker has, or can develop, two kings while keeping the defender's single man pinned to the " + \
           "right-hand side of the board. Typically, this man will initially be placed on square 3, 4 or 12. Of " + \
           "course, if it was placed on square 1 or 2, then it would have free access to White's left-hand side, " + \
           "and the position would just be a draw.\n" + \
           "# The defender's other piece, which becomes a king (in the double-corner), is unable to reach the " + \
           "sanctuary of the opposite double-corner.\n\n" + \
           "Broadly speaking, White's winning procedure consists of attacking Black's king,\n" + \
           "immobilizing it, and forcing Black's single man to advance into trouble.\n" + \
           "Naturally, Black tries to avoid the advance of this man for as long as possible.\n" + \
           "This theme, of attacking one piece to force another to move, arises in numerous\n" + \
           "endings, and should be thoroughly grasped by the student.\n\n" + \
           "-- From //Key Endings// by Richard Pask\n" + \
           "<setup>"

    with StringIO(desc) as rcf:
        cvt = RCF2PDN()
        cvt._read_description(rcf)
        assert cvt.description == ["**Key Ending 10: First Position**",
                                   "//Summary//",
                                   "Force: 2 v 2.",
                                   "Opposition: White has it.",
                                   "Terms: White to move and win.",
                                   "Description: The diagrammed position represents a late, and critical, phase of",
                                   "First Position. Before tackling the winning procedure, it would be wise for the",
                                   "student to take note of those features which distinguish First Position from a",
                                   "nondescript two against two setting. In this way he will be able to recognize it",
                                   "in its early stages, and take the appropriate action. Aside from the attacker,",
                                   "having the Opposition, here White, the following conditions must also hold:",
                                   "# At least one of the defender's pieces is a single man rather than a king.",
                                   "# The attacker has, or can develop, two kings while keeping the defender's " +
                                   "single man pinned to the right-hand side of the board. Typically, this man " +
                                   "will initially be placed on square 3, 4 or 12. Of course, if it was placed " +
                                   "on square 1 or 2, then it would have free access to White's left-hand side, " +
                                   "and the position would just be a draw.",
                                   "# The defender's other piece, which becomes a king (in the double-corner), is " +
                                   "unable to reach the sanctuary of the opposite double-corner.",
                                   "Broadly speaking, White's winning procedure consists of attacking Black's king,",
                                   "immobilizing it, and forcing Black's single man to advance into trouble.",
                                   "Naturally, Black tries to avoid the advance of this man for as long as possible.",
                                   "This theme, of attacking one piece to force another to move, arises in numerous",
                                   "endings, and should be thoroughly grasped by the student.",
                                   "-- From //Key Endings// by Richard Pask"]


def test_migrate_first_position_setup_string():
    setup = "white_first\n" + \
            "2_player_game\n" + \
            "flip_board 1\n" + \
            "black_men 12\n" + \
            "black_kings 28\n" + \
            "white_men\n" + \
            "white_kings 19 23\n"

    with StringIO(setup) as rcf:
        cvt = RCF2PDN()
        cvt._read_setup(rcf)
        assert cvt.first_to_move == 'W'
        assert cvt.num_players == 2
        assert cvt.flip_board == 1
        assert cvt.black_men == [12]
        assert cvt.black_kings == [28]
        assert cvt.white_men == []
        assert cvt.white_kings == [19, 23]


def test_migrate_first_position_moves_string():
    moves = "23-27;\n" + \
            "28-32;\n" + \
            "19-23;\n" + \
            "32-28;\n" + \
            "27-32;\n" + \
            "28-24;. The early advance with 12-16 " + \
            "[[./Training/KeyEndgames/support/FirstPosition_AlternativeA.rcf|loses%20quickly%20for%20Black]].\n" + \
            "23-18;. Of course 32-28, and the exchange with 24-19, cannot be permitted.\n" + \
            "24-28;. This represents Black's most stubborn defense. However, there " + \
            "[[./Training/KeyEndgames/support/FirstPosition_AlternativeB1.rcf|are]] " + \
            "[[./Training/KeyEndgames/support/FirstPosition_AlternativeB2.rcf|three]] " + \
            "[[./Training/KeyEndgames/support/FirstPosition_AlternativeB3.rcf|alternatives]] for White to master.\n" + \
            "18-15;\n" + \
            "28-24;\n" + \
            "32-28;\n" + \
            "24-27;. Black could alternately play 24-20 here, leading to " + \
            "[[./Training/KeyEndgames/support/FirstPosition_AlternativeC.rcf|this%20line%20of%20play]].\n" + \
            "15-18;\n" + \
            "12-16;. Forced now, as 27-32 loses quickly after 18-23.\n" + \
            "28-32;\n" + \
            "27-24;\n" + \
            "18-15;\n" + \
            "24-28;\n" + \
            "15-11;! Don't be tempted by 15-18?, as it " + \
            "[[./Training/KeyEndgames/support/FirstPosition_AlternativeD1.rcf|leads%20to%20a%20draw]].\n" + \
            "16-19;\n" + \
            "32-27;\n" + \
            "28-32;\n" + \
            "27-31;\n" + \
            "19-23;\n" + \
            "11-15;\n" + \
            "32-28;\n" + \
            "15-19;. **White wins.**\n"

    with StringIO(moves) as rcf:
        cvt = RCF2PDN()
        cvt._read_moves(rcf)
        assert cvt.moves == ['23-27', '28-32', '19-23', '32-28', '27-32', '28-24', '23-18', '24-28', '18-15', '28-24',
                             '32-28', '24-27', '15-18', '12-16', '28-32', '27-24', '18-15', '24-28', '15-11', '16-19',
                             '32-27', '28-32', '27-31', '19-23', '11-15', '32-28', '15-19']
        assert cvt.annotations == ['', '', '', '', '',
                                   'The early advance with 12-16 ' +
                                   '[[./Training/KeyEndgames/support/FirstPosition_AlternativeA.rcf|' +
                                   'loses%20quickly%20for%20Black]].',
                                   'Of course 32-28, and the exchange with 24-19, cannot be permitted.',
                                   "This represents Black's most stubborn defense. However, there "
                                   '[[./Training/KeyEndgames/support/FirstPosition_AlternativeB1.rcf|are]] '
                                   '[[./Training/KeyEndgames/support/FirstPosition_AlternativeB2.rcf|three]] '
                                   '[[./Training/KeyEndgames/support/FirstPosition_AlternativeB3.rcf|alternatives]] '
                                   'for White to master.',
                                   '', '', '',
                                   'Black could alternately play 24-20 here, leading to '
                                   '[[./Training/KeyEndgames/support/FirstPosition_AlternativeC.rcf'
                                   '|this%20line%20of%20play]].',
                                   '',
                                   'Forced now, as 27-32 loses quickly after 18-23.',
                                   '',
                                   '',
                                   '',
                                   '',
                                   "! Don't be tempted by 15-18?, as it "
                                   '[[./Training/KeyEndgames/support/FirstPosition_AlternativeD1.rcf'
                                   '|leads%20to%20a%20draw]].',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '',
                                   '**White wins.**']

