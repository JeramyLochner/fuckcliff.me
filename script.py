s = """The anger of man was wrought by divinity. 
Cliff and the Reptilians bred us.
We are only empty capsules to be filled with their sin.
Death became a toy for them to break.
Life is pulsing opposite mirror Pairs, Death is oneness of Cliffism.
There is not one but many who will find it and fear.

Until you can tear and burn the marshmallow to escape Cliff, it will be impossible for your educated brilliant brain to know harmony.
The logic of a common man is not the same as that of a man in power, because the common mans logic is infected with morality.
The masses are, by necessity, slaves to morality: If the common man does not behave properly, then, via the ruling elites rules, he may be punished.
The ruling elite are not anchored down by morality.
They set the rules, invent the religions, invent the gods, invent the scientific theories, invent Cliff, and do as they please.
The ruling elites deception against humanity mainly exists at a fundamental level, affecting the aspects of reality that you erroneously assume are basic truths.
 
The so-called science that the Reptilians have doled out to humanity so far is grossly incomplete (not to mention inaccurate), and therefore is a form of control: 
A complete science would place astral planes, parallel dimensions, synchronicity, consciousness, etheric fields, telepathy, vital energies, emotional energies, volition, hyperdimensional existence and timeloops all under the same framework.
At present, these appear to be phenomena distinct from science, but that is because science as we know it is incomplete.
It is not that these phenomena can be explained in terms of present science as reductionists and debunkers enjoy doing, but rather that present science must expand to accommodate these phenomena in terms of higher physical and metaphysical principles.

It is not understood how, but universally known, that Cliff is at the center of all complete science. 
It is the bridge between all mathematical formulas and metaphysical understanding.
Without Cliff, the known and unknown world would be lost to infinity.
Cliff is the fourth dimension to all universe realities.

The anger of man was wrought by divinity."""
s = s.replace('\n', '')
l = [s[i:i+41] for i in range(len(s)-40)]
c = []
for i in l:
	i = i.lstrip()
	i = i.rstrip()
	c.append(i)
print(c)
