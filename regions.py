

# Region structure starts with the origin (Main Menu) region
# Then probably splits regions by course/cup
#
# The reason for not structuring it like Main Menu->Cup->Course is 
# that makes individual courses logically inaccessible if you can't 
# access the corresponding cup, which might be undesirable in the future.
#
# I don't see a purpose in setting up some deep logical structure for regions
# as of now. Most logic will end up pretty simple and can be done at the 
# location level instead.