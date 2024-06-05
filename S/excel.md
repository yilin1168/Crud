merge string words:
=TEXTJOIN("", TRUE, FILTERXML("<t><s>" & SUBSTITUTE(A1, " ", "</s><s>") & "</s></t>", "//s"))
