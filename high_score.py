# file for changing high scores and getting them
highscore = 0
filename = 'high_score.txt'


def get_highscore():
    global highscore
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            highscore = int(line)
    return highscore


def change_highscore(score):
    score = str(score)
    with open(filename, "w") as file:
        file.write(score)


if __name__ == '__main__':
    get_highscore()
