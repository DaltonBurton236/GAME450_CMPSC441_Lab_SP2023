Sentence1 = "As an AI language model, I can certainly help you imagine what an alien bird might look like based on what we know about birds on Earth and the various possibilities of life in the universe. An alien bird could have a variety of unique adaptations depending on the environment in which it evolved. For instance, if it lived on a planet with low gravity, it might have large wings to help it fly easily, or if it lived in a harsh environment with high radiation, it could have developed a tough outer layer of feathers to protect it from the radiation. One possibility for an alien bird is that it could have multiple sets of wings that are arranged in a radial pattern around its body, similar to the spokes on a wheel. Each wing could be individually controlled by the bird, allowing it to maneuver through the air with incredible precision. Another possibility is that the alien bird could have a prehensile tail that could be used to grasp objects or to help it balance while perching. It could also have feathers that are bioluminescent, glowing in the dark to help it communicate with other members of its species. Overall, an alien bird could come in a wide variety of shapes, sizes, and colors, and could possess an array of unique adaptations that allow it to thrive in its environment."
Sentence2 = "As an AI language model, I can only imagine an alien bird based on scientific speculation and creative interpretation. So, here's my attempt to describe an alien bird: An alien bird might have evolved in a completely different environment than Earth, and as such, it may look very different from the birds we're used to seeing. It might have a sleek, streamlined body covered in iridescent feathers of all colors of the spectrum. Perhaps, it would have wings that are longer and more narrow than any bird on Earth, allowing it to soar through the thin atmosphere of its home planet with ease. Its beak may also differ from birds on Earth, and it may be equipped with various specialized features for catching prey or extracting nectar from alien plants. It could have incredibly sharp talons, perfect for grasping its food or for self-defense against potential predators. Its eyes may also be larger and more sensitive to light, allowing it to navigate and hunt in dimly lit environments. Perhaps, the alien bird would also have unique abilities like camouflage, the ability to generate electric fields, or to emit sonic waves for communication or navigation. It might even have additional limbs or appendages that help it maneuver through its environment. Ultimately, the appearance and abilities of an alien bird would depend on the specific environment it evolved in and the unique challenges it faced in that environment. But one thing is for sure, an alien bird would be a fascinating and exotic creature to behold!"
from sentence_transformers import SentenceTransformer, util
sentences = [Sentence1, Sentence2]

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings_1 = model.encode(sentences[0], convert_to_tensor=True)
embeddings_2 = model.encode(sentences[1], convert_to_tensor=True)
print(util.pytorch_cos_sim(embeddings_1,embeddings_2))
# I believe a good metric to assess the overall similarity between sentences is to compare the overal structure of the responces instead of the specific details within.
#For example using this method both response can be filter down as such
#I'm an AI, I will try to imagine aliens birds. They would evolve depending on where they live. List of possible alien bird feature. They would evolve depending on where they live.
#With this metric even though they discuss different bird features. Overall, the reponses are quite similar.