**The source code for mapping Google Vision API’s labels to MIMSY (Museum Integrated Management System) approved tags.**

To tag Mead Art Museum’s collection using Vision API, we had to build a common terminology between MIMSY and Vision API. MIMSY tags are pre-defined and fixed, approved by the Five Colleges and Historic Deerfield Museum Consortium, so we had to figure out a way to build a Python dictionary to map Google tags to MIMSY tags. Evidently, the terms used for tagging Mead’s collection differ from those Vision uses to classify and label images:

1. Many Vision terms are semantically the same and can be put under a general tag.
For example, Vision can identify and label an image with a “blackbird”, “bluebird”, “hummingbird”, etc, but all of these can be simply mapped to “birds”, which already exists in MIMSY’s list of approved tags.

2. Vision and MIMSY also have many gender-specific tag terms (e.g., women and actresses). Since gender expressions differ among cultures and time periods, we removed all gender-specific tags from both of these lists. Whenever Vision detected a “person”, we mapped it to MIMSY’s gender-neutral “people” tag (all other gender-specific tags were removed from both sources.)

3. Vision uses singular tag terms, while Mead uses plural nouns.

The generated dictionary needed further cleaning since we used generic substring pattern matching methods. Also, some Google tags are contemporary objects or concepts and can not be effectively used to tag objects in Mead’s database. All the unnecessary words were deleted and polished by Dr. Miloslava Hruba. The output was a Python dictionary of 1,237 distinct Google tags mapped to 630 MIMSY tags.

Other notes and considerations: 

1. Some Vision tags like “Asian food” are listed under two different Mead tags: “food” and “Asian”. For example, in this case, “food” is probably a more suitable tag than “Asian”. “Asian” may be the tag for “Asian” art or culture. If you wish to redefine the terms according to the unique nature of your museum’s database and used terms, feel free to choose the most appropriate and relevant tag and erase the other one. (Or keep both, if it is reasonable.)

2. Some tags may be useful but have to be moved from one category to another. For example, “dog food” is listed under the “food” category, but it is more relevant to animal stuff. So, we can move this word to be listed under “animal” or “dogs” (or both) rather than “food”. Sometimes, some tags have to be erased from one category and added to another, because they were simply matched because of substring patterns, not their semantic meaning or the context they are used. 
