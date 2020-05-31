# Social-Network-Simulator

A man once said:

> If you want to learn a new language start with simple syntax ans then implement Data Structures in that language

Well, that's what I was doing when I dived into python. I started implementing `list, linked list, graph` etc. I wanted to develop a project that will use all these concepts, so that I can develop better understanding of these concepts.  Ever thought how Facebook, Linked-in, Instagram worked? Well, I have and that's what I wanted to develop.

This project simulates a "Social Network", where you can:

- Make friends
- Follow and un-follow people
- Create, like and delete posts

## How to run?
You have to run "SocialSim.py". No additional packages are required, this project only uses features that are present standard python distribution.

![usage](https://user-images.githubusercontent.com/49767636/83347690-18f27a00-a340-11ea-9cde-17562ccc4129.jpg)

As you can see there are two modesin which you can use this program, details are as follow:

### Interactive mode
In this mode, user can interact with the program and will have to provide input at each step as he/she wants, this is how a interactive mode looks like:

![intr](https://user-images.githubusercontent.com/49767636/83347742-89010000-a340-11ea-8fb8-d8914e087ee3.jpg)

#### Load Network
Using this function you can create a network, there are further two more options:

![load](https://user-images.githubusercontent.com/49767636/83347764-bcdc2580-a340-11ea-87f9-183e6325994f.jpg)

#### Load new network
If you want to load a new network from a network file you should use this option. Sample run of loading from text file:

![load new network](https://user-images.githubusercontent.com/49767636/83347859-54da0f00-a341-11ea-9d69-3d369d50ea95.jpg)


As you can see the network is loaded when we print the network it prints as expected. Remember **Format of the network input should be exactly same as the network.txt file that is provided**.

#### Load saved network
If you have created a network and made some changes, saved the network using **Save network**. You can load the graph from the saved pickle file.

![saved](https://user-images.githubusercontent.com/49767636/83347962-36284800-a342-11ea-9536-22d9101e53b0.jpg)

#### Set Probabilities
It is probability in percentage(%), that how much likely a person will follow another person, or much likely a person will like the post. If you think this application as a "Disease spread simulation", this parameter will mean that how much is likely for a healthy person get affected by the disease. 

![pro](https://user-images.githubusercontent.com/49767636/83348049-c1094280-a342-11ea-8aae-32c5f222d335.jpg)

#### Node Operations
As the graph is a linked-list of a linked-lists, so, A node is representing a person in the network. If you want to:

**Sign-up in the network**

![insert](https://user-images.githubusercontent.com/49767636/83348191-a6839900-a343-11ea-9400-038b3fba6532.jpg)


**Get removed from the network**
![delete](https://user-images.githubusercontent.com/49767636/83348171-750acd80-a343-11ea-852d-cc99cbc94ac6.jpg)

**Find a friend in network**

![found](https://user-images.githubusercontent.com/49767636/83348147-412fa800-a343-11ea-8fca-285d8d00d257.jpg)

#### Edge Operations
Edge represent a connection between various persons in the network. If you want to:

**Add a friend**
We will make "Rex" a friend of "Imran khan".
![add](https://user-images.githubusercontent.com/49767636/83348313-d54e3f00-a344-11ea-8313-df63dd6df573.jpg)

**Remove a friend**
We will remove "Rex" as a friend of "Imran khan".
![remov](https://user-images.githubusercontent.com/49767636/83348335-fd3da280-a344-11ea-8553-85be0237e8ad.jpg)

### New Post
Its just like making a new post and publishing it. Now, how many will like this post and how many will follow the person in return, depends on the **Probabilities** we set earlier (remember ???)
![post](https://user-images.githubusercontent.com/49767636/83348411-c4ea9400-a345-11ea-8f58-62c8f3b2e5e4.jpg)

#### Display Network
Should I tell what this option will do ?
![display](https://user-images.githubusercontent.com/49767636/83348435-fbc0aa00-a345-11ea-91fb-53e00394babb.jpg)

#### Display Statistics
This option will display various stats like:

- Number of posts made by a person
- Post ordered by their popularity
- Number of likes, friends, friends of etc

![stata](https://user-images.githubusercontent.com/49767636/83348452-3a566480-a346-11ea-825d-ad2a5e129635.jpg)

#### Update
As we are in simulation mode, we have to update the network manually. What does this **update** means? You have created a post, now people will start liking the post as you update the network. In other terms, it is a mean of progressing through time.
![update](https://user-images.githubusercontent.com/49767636/83348540-0f204500-a347-11ea-8a9a-f559d7cdc66b.jpg)

#### Save Network
You have made changes to your network and wants to save the network for future use, don't worry I got you covered. Use this option to save the network as a pickle file.
![optn 9](https://user-images.githubusercontent.com/49767636/83348571-7211dc00-a347-11ea-9966-9d55feee5d07.jpg)

#### Exit 
Done spending hours and hours on my network and now wants to go to sleep ? Use this option to exit.

### Simulation mode
You don't have time to manually create posts, follow, unfollow people and want to automate things. Use **events.txt** to save all the events and run a simulation on them.
Events file can have events of adding a friend, removing a friend, posting, liking etc. See the  events.txt for more information. Remember **Your events file should be in same format as the given events.txt**

Once you have run the simulation a **Simulation_Log.txt** file will appear that will contains various stats and other logs
![sim](https://user-images.githubusercontent.com/49767636/83348752-b2be2500-a348-11ea-9c71-5b0a64b94f14.jpg)
