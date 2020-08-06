print("Welcome to XMAS TREE 3000 created by Jaroslavm :) ")
tree_height = input("How big should be the tree be?")
tree_height = int(tree_height)
spaces = tree_height
stars = 1


for i in range(tree_height):
    for space in range(spaces):
        print(end=" ")

    for star in range(stars):
        print("*", end="")

    print("")

    stars = stars + 2
    spaces = spaces - 1


def end_of_tree(bottom):
    for final in range(tree_height):
        print(" ", end="")
    for IDK_whatTOputHERE in range(bottom):
        print("*", end="")
    print("")


end_of_tree(1)


tree_height = tree_height - 2
end_of_tree(5)
