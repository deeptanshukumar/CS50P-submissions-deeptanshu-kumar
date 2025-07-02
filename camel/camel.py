def main():
    user_input = input("camelCase: ").strip()
    indexes = [0]+index_returner(user_input)
    words = words_returner(user_input,indexes)
    snake_case_converter(words)


def index_returner(user_input):
    index = []
    for i in user_input:
        if i.isupper():
            index.append(user_input.index(i))
            user_input = user_input.replace(i,i.lower(),1)
    return index

def words_returner(user_input,indexes):
    wordss = []
    for i in range(len(indexes)):
        if i == len(indexes)-1:
            wordss.append(user_input[indexes[i]:].lower())
        else:
            wordss.append(user_input[indexes[i]:indexes[i+1]].lower())
    return wordss

def snake_case_converter(words):
    print(f"snake_case: {"_".join(words)}")


main()


