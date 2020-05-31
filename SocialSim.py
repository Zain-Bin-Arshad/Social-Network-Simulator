from list import LinkedList
from node import Node
from pickle import dump, load, HIGHEST_PROTOCOL  # importing pikckle for saving graph object
from sys import argv

from graph import Graph


def menu():
    """
    Prints possible choices to user
    :return: str
    """
    menu = "(1) Load network\n(2) Set probabilities\n(3) Node operations" \
           "\n(4) Edge operations\n(5) New post\n(6) Display network" \
           "\n(7) Display statistics\n(8) Update\n(9) Save network\n(0) Exit\n>> "
    return input(menu)


def load_network(graph, network):
    """
    Loads a network from a given file or object(if saved earlier)
    :param graph: Graph Object
    :param network: network file
    :return: None
    """
    network = open(network, "r")  # open given file
    for line in network:  # iterate over whole file line by line
        line = line.rstrip().lstrip()  # removes any white spaces after or before the node value
        if ':' not in line:  # if line has node to add
            graph.list.add_last(LinkedList(line))  # add node to the grpah
        else:  # if line has nodes to connect
            vertices = line.split(':')  # makes list of two nodes by spliting the line on delimiter
            vertices[0] = vertices[0].rstrip().lstrip()  #
            vertices[1] = vertices[1].rstrip().lstrip()
            graph.connect(vertices[0], vertices[1])  # make a connection between node
    network.close()  # close the open file


def main():
    """
    Contains driver code for the project
    :return: None
    """
    graph = Graph()  # createsnew graph object
    pro_like = 0  # intilize probabily of liking a post to zeero
    pro_follow = 0  # intilize probabily of folloing a person a post to zero
    time = 1  # will tell time sep number
    time_step = []  # this will contain list of nodes that will be affected with each timestep
    try:
        if not len(argv) >= 2:  # if we dont have required arguments than show usage information
            print("Usage: SocialSim -s [network_file] [event_file] [prob_like] [prob_follow]")
            print("Usage: SocialSim -i")
            print("-i : interactive mode")
            print("-s : simulation mode")
            return
        if argv[1] == "-i":  # if user wants to go to interactive mode
            while 1:  # runs the untill user exits i.e. enter "0"
                try:  # try to catch any exception so tat execution contain
                    choice = int(menu())  # take input from user
                    if choice is 1:  # load network
                        user = int(input("(1) Load new network\n(2) Load saved network\n>> "))
                        if user is 1:  # load new network
                            network = input("\nEnter file name: ")
                            load_network(graph, network)
                        elif user is 2:  # load from saved pickle file
                            f = input("\nEnter file name: ") + ".pkl"
                            f = open(f, "rb")  # open file and reads bytes
                            graph = load(f)  # load graph from using pickle.load()
                            f.close()  # closing file
                        else:
                            print("Invalid choice. try again")
                    elif choice is 2:  # probabilities
                        pro_like = float(input("\tEnter probablity of Like: "))
                        pro_follow = float(input("\tEnter probablity of Follow: "))
                    elif choice is 3:  # node operations
                        user = int(input("\t(1) Find \n\t(2) Insert\n\t(3) Remove\n\t>> "))
                        if user is 1:  # find node
                            node = input("\tEnter node to find: ")
                            if graph.list.find_node(node) is not None:  # if node found
                                print("\t" + node + " found !")
                            else:
                                print("\t" + node + " not found")
                        elif user is 2:  # insert a new node
                            graph.list.add_last(LinkedList(input("\tEnter node to insert: ")))
                            print("\tNode added")
                        elif user is 3:  # delete a node
                            node = input("\tEnter node to delete: ")
                            if graph.list.delete_node(
                                    node) is not None:  # if node id found and delete, delete method will look for node first
                                graph.delete_node(node)
                                print("\t" + node + " deleted.")
                            else:
                                print("\t" + node + " can't be deleted.")
                        else:
                            print("Invalid choice. try again")
                    elif choice is 4:  # edge operations
                        user = int(input("\t(1) Add \n\t(2) Remove\n\t>>  "))
                        if user is 2:  # remove edge
                            node1 = input("\tEnter node1 : ")
                            node2 = input("\tEnter node2 : ")
                            if graph.delete_edge(node1, node2) is True:  # if edge got removed
                                print("\tEdge Deleted")
                        elif user is 1:  # add edge
                            node1 = input("\tEnter node1 : ")
                            node2 = input("\tEnter node2 : ")
                            graph.connect(node1, node2)
                            print("\tEdge added")
                        else:
                            print("Invalid choice, try agian.")
                    elif choice is 5:  # new post
                        node = input("\tEnter node: ")
                        node = graph.list.find_node(node)  # first find the node in the graph
                        if node is not None:  # if node is found
                            node.posts.append(input("\tEnter Post: "))  # append the post to the node.posts[]
                            time_step.append(node)  # now add this node to time_step as this post will propagate
                        else:
                            print("\tNode not found")
                    elif choice is 6:  # display network
                        print(graph)  # call sthe __str__() of class Graph
                    elif choice is 7:  # diplay stats
                        likes = []  # makes a list of all the required data for showing stats
                        person = graph.list.head
                        print("\t\t\tPeople in order of popularity.")
                        while person:
                            likes.append((person.likes, person.value, person.posts, person.fol, person.flrs))
                            person = person.next_node
                        likes.sort(key=lambda t: t[0], reverse=True)
                        for like in likes:
                            print("\t\tPeople: " + str(like[1].value) + " Total Likes: " + str(like[0]))

                        print("\t\t\tPosts in order of popularity.")
                        for like in likes:
                            post = like[2]
                            for p in post:
                                print("\t\tPost: " + str(p))

                        for like in likes:
                            print("\t\t" + str(like[1].value) + "'s record:\n\t\t\tPosts # " + str(len(like[2])))
                            print("\t\t\tFollowers # " + str(like[4]) + "\n\t\t\tFollowing # " + str(like[3]))

                    elif choice is 8:  # run a time step
                        print("\nTIME STEP # " + str(time) + " EXECUTED\n")
                        if time_step:
                            if pro_like >= 0.5:
                                n = time_step[0].value.head
                                while n:
                                    node.likes += 1
                                    if pro_follow >= 0.5:
                                        n1 = graph.list.find_node(str(n.value))
                                        if n1 is not None:
                                            n1 = n1.value.head
                                            while n1:
                                                if node.value.find_node(str(n1.value)) is None:
                                                    graph.connect(str(node), str(n1.value))
                                                n1 = n1.next_node
                                    n = n.next_node
                                time_step = time_step[1:]
                        time += 1
                    elif choice is 9:  # save network
                        f = input("\nEnter file name: ")
                        f = open(f + ".pkl", "wb")
                        dump(graph, f, HIGHEST_PROTOCOL)
                        f.close()
                    elif choice is 0:
                        break
                    else:
                        print("Invalid choice. try again")
                except Exception as ex:
                    print(ex)
                    print("Invalid input. try again")
        elif argv[1] == "-s":
            load_network(graph, argv[2])
            pro_follow = int(argv[5])
            pro_like = int(argv[4])
            event = open(argv[3], "r")
            for line in event:
                check = 0
                line = line.split(':')
                if line[0] == 'A':  # adding node
                    graph.list.add_last(LinkedList(line[1]))
                elif line[0] == 'F':  # follow
                    graph.connect(line[1], line[2])
                elif line[0] == 'P':  # new post
                    pass
                    # I have a problem of infinte loop here
                    node = graph.list.find_node(line[1])
                    if node is not None:
                        node.posts.append(line[2])
                        time_step.append(node)
                        if time_step:
                            if pro_like >= 0.5:
                                n = time_step[0].value.head
                                while n:
                                    check += 1
                                    node.likes += 1
                                    if pro_follow >= 0.5:
                                        n1 = graph.list.find_node(str(n.value))
                                        if n1 is not None:
                                            n1 = n1.value.head
                                            while n1:
                                                if check > 100:
                                                    break
                                                check += 1
                                                if node.value.find_node(str(n1.value)) is None:
                                                    graph.connect(str(node), str(n1.value))

                                                n1 = n1.next_node
                                    n = n.next_node
                                time_step = time_step[1:]
                        time += 1
                elif line[0] == 'R':  # remove node
                    if graph.list.delete_node(line[1]) is not None:
                        graph.delete_node(line[1])
                elif line[0] == 'U':
                    graph.delete_edge(line[1], line[2])
                file = open("simulation_Log.txt", "w")
                likes = []
                person = graph.list.head
                file.write("\t\t\tPeople in order of popularity.\n")
                while person:
                    likes.append((person.likes, person.value, person.posts, person.fol, person.flrs))
                    person = person.next_node
                likes.sort(key=lambda t: t[0], reverse=True)
                for like in likes:
                    file.write("\t\tPeople: " + str(like[1].value) + " Total Likes: " + str(like[0]) + "\n")
                file.write("\t\t\tPosts in order of popularity.\n")
                for like in likes:
                    post = like[2]
                    for p in post:
                        file.write("\t\tPost: " + str(p) + "\n")
                for like in likes:
                    file.write("\t\t" + str(like[1].value) + "'s record:\n\t\t\tPosts # " + str(len(like[2])) + "\n")
                    file.write("\t\t\tFollowers # " + str(like[4]) + "\n\t\t\tFollowing # " + str(like[3]) + "\n")
                file.close()
            event.close()
    except Exception as ex:
        print(ex)


if __name__ == "__main__": main()
