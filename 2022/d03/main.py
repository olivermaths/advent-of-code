## Puzzle Two

def get_lines(path):
    f = open(path)
    lines = f.readlines()
    f.close()
    return lines

def get_groups(list):
    groups = []
    team = []
    for idx, line in enumerate(lines):
        team.append(line.replace('\n', ''))
        if (idx+1)%3 == 0:
            groups.append(team)
            team = []
    return groups

def get_group_badge(group):
    badge = None
    for c in group[0]:
        if c in group[1] and c in group[2]:
            badge = c
    return badge

def get_groups_badge(groups):
    badges = []
    for group in groups:
        badge = get_group_badge(group)
        badges.append(badge)
    return badges

def get_priority(badges):
    priorities = []
    for badge in badges:
        if ord(badge) < 91: priorities.append(ord(badge) - 38)
        else: priorities.append(ord(badge) - 96)
    return priorities



lines = get_lines("d03/input")
groups = get_groups(lines)
badges = get_groups_badge(groups)
prior = get_priority(badges)
print(sum(prior))
