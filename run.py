from markov_python.cc_markov import MarkovChain

mc = MarkovChain()

dir = "characters/"
file = "Jerry.txt"

mc.add_file(dir + file)
print " ".join(mc.generate_text())
