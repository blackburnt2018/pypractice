story = "once upon a time there was this man named {0} who decided that it would be a good idea to go swimming in a {1} invested lake. see the thing about pirhanas, they are {3} at night, so as the man wanted to go (2} in the invested waters he also made one of his friends join him. his friend's name was {0}. {0} is completely {3} and was convinced that the waters were not {3}. and he also thought that he was going to be safe. what the two also did not know about is that pirhanas are attracted to fresh {1}. so never {2} in the water with an open wound."
name = raw_input("enter a name")
verb = raw_input("enter a verb")
adjective = raw_input("enter a adjective")
noun = raw_input("enter a noun")
adjusted = story.format(name, noun, adjective, verb, adjective)


print(adjusted)
