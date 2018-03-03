story="Of the seven hundred villages dotting the map of India, in which the majority of India's five hundred\n"+"million live, flourish and die, Kritam was probably the tiniest, indicated on the district survey map by\n"+"a microscopic dot, the map being meant more for the revenue official out to collect tax than for the\n"+"guidance of the motorist, who in any case could not hope to reach it since it sprawled far from the\n"+"highway at the end of a rough track furrowed up by the iron-hooped wheels of bullock carts. But its\n"+"size did not prevent it's giving itself the grandiose name Kritam, which meant in Tamil coronet or\n"+"crown on the brow of the subcontinent.The village consisted of fewer that thirty houses, only one of\n"+"them built from brick and cement. Painted a brilliant yellow and blue all over with gorgeous\n"+"carvings of gods and gargoyles on its balustrade, it was known as the Big House. The other houses,\n"+"distributed in four streets, were generally of bamboo thatch, straw, mud and other unspecified\n"+"material. Muni's was the last house in the fourth street, beyond which stretched the fields. In his\n"+"prosperous days Muni had owned a flock of sheep and goats and sallied forth every morning driving\n"+"the flock to the highway a couple of miles away. There he would sit on a pedestal of a clay statue of a\n"+"horse while his cattle grazed around. He carried a crook at the end of a bamboo pole and snapped\n"+"foliage from the avenue trees to feed his flock; he also gathered faggots and dry sticks, bundled\n"+"them, and carried them gathered for duel at sunset"

newname=input("Enter your name to make a story\n")
story=story.replace("Kritam",newname)
newplace=input("Enter a living place\n")
story=story.replace("house",newplace)
newanimal=input("Enter a animal name\n")
story=story.replace("goat",newanimal+"e")

print("Your personalized story is:\n\n")

print(story)


