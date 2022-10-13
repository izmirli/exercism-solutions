"""Tournament."""
from collections import defaultdict

POINTS = {'win': 3, 'draw': 1, 'loss': 0}


def matches_parsing(matches: list[str]) -> dict[str, int]:
    """Parse matches lines and return their tallied info.

    Example line: "Allegoric Alaskans;Blithering Badgers;win".
    The result of the match refers to the first team listed.

    :param matches: result of the matches list
    :return: foreach team tallied: matches, won, drawn, lost, and points
    """
    teams_data = defaultdict(lambda: {'MP': 0, 'W': 0, 'D': 0, 'L': 0, 'P': 0})
    for match in matches:
        team1, team2, outcome = match.split(';')
        teams_data[team1]['MP'] += 1
        teams_data[team1][outcome[0].upper()] += 1
        teams_data[team1]['P'] += POINTS[outcome]
        if outcome != 'draw':
            outcome = 'loss' if outcome == 'win' else 'win'
        teams_data[team2]['MP'] += 1
        teams_data[team2][outcome[0].upper()] += 1
        teams_data[team2]['P'] += POINTS[outcome]

    return dict(teams_data)


def tally(rows: list[str]) -> list[str]:
    """Return table of tallied information for all given matches.

    :param rows: matches info
    :return: table of tallied information
    """
    teams_data = matches_parsing(rows)
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for team in sorted(
            sorted(teams_data), key=lambda k: teams_data[k]['P'], reverse=True
    ):
        table.append(
            f"{team:<30} | {teams_data[team]['MP']:>2} | {teams_data[team]['W']:>2} | "
            f"{teams_data[team]['D']:>2} | {teams_data[team]['L']:>2} | {teams_data[team]['P']:>2}"
        )

    return table
