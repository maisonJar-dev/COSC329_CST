idf fixes the issue for words that occur everywhere and 0's them out

# Maison Gulyas | COSC_O 329 Learning Analytics

## Dendrogram Results
From the dendogram provided in the assingment metadata it suggests that `t6` and `t12`, `k6` and `k14`, `k8` and `t14`, are quite similar. We can see this as the height of their mergers is considerably lower. That being said we can also see that `k2` is the most dissimilar and unique document. This would suggest that after stemming it has the most unique words.

## Personal Results Suggestion
My results showed me that in a normalized environment with distances [0,1] that none of the documents were that similar. The most similar documents were `t12` and `t6`. Furthermore, the least similar was `k2`. My data somewhat persists with the one provided in the assignment. 

## Additional Analysis for Implications
You could reduce the bag of words by stemming more. I used the Porter Stemming algorithm provided from `nltk` which removes common suffixes using predefined rules. This would increase our similarities as there would be a higher chance for more similar preffixes. So to actually determine how similar these documents are I would suggest applying more stemming and then running it again. If the merge lines lowered that would indicate that the documents are actually more similar and that the stemming related to the issue since one round didn't suffice.