"""Restaurant rating lister."""


# put your code here

def organize_scores():
    scores = open("./scores.txt")

    ratings_dict = {}
    i = 0
    list = []

    for line in scores:

        line = line.strip()
        line = line.split(":")

        ratings_dict[i] = {"name": line[0],
                           "score": line[1]}
        list.append(f"{line[0]} is rated at {line[1]}.")

        i += 1

    return {"list": list,
            "ratings_dict": ratings_dict}


def add_value():

    name = input("Name a restaurant not on the list: ")
    score = input("From 1-5 what would you rate that restaurant?: ")
    
    return {"name": name,
            "score": score}


def print_scores(x):
    x = sorted(x)
    for index in x:
        print(index)


def main():

    scores_dict = organize_scores()
    list = scores_dict.get("list")
    ratings_dict = scores_dict.get("ratings_dict")

    print_scores(list)

    new_value = add_value()
    name = new_value.get("name")
    score = new_value.get("score")

    if name != None:
        list.append(f"{name} is rated at {score}.")
        ratings_dict[len(ratings_dict)+1] = {"name": name,
                                             "score": score}

    print_scores(list)


main()
