def euclidean_distance(p1, p2):
    ans = 0

    for i in range(len(p1.position)):
        ans += (p1.position[i] - p2.position[i]) ** 2
        return ans


def find_closest(p,population):
    closest = None
    min_dist = None
    for particle in population:
        if particle == p:
            continue
        dist = euclidean_distance(p, particle)

        if min_dist is None or dist < min_dist:
            min_dist = dist
            closest = particle

    return closest
