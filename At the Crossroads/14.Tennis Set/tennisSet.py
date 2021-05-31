def tennisSet(score1, score2):
    mx = max(score1, score2)
    mn = min(score1, score2)
    return (mx == 6 and mn < 5) or (mx == 7 and mn >=5 and mn != mx)