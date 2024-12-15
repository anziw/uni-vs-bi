import csv

def get_mask_positions(mask_filename):
    """
    Reads the MVRR_mask.txt file and extracts the position of [MASK] for each sentence.
    Returns a list of positions.
    """
    mask_positions = []
    with open(mask_filename, "r", encoding="utf-8") as mask_file:
        for line in mask_file:
            words = line.strip().split()
            if "[MASK]" in words:
                mask_positions.append(words.index("[MASK]"))
            else:
                mask_positions.append(-1) 
    return mask_positions

def get_word(sentence, index):
    """
    Function to get a word at a specific position in a sentence.
    """
    words = sentence.split()
    if index < len(words):
        return words[index]
    return ""  

def transform_MVRR_to_tsv(txt_filename, mask_filename, tsv_filename):
    """
    Transforms the MVRR TXT file into a TSV file
    """
    with open(txt_filename, "r", encoding="utf-8") as txt_file:
        sentences = [line.strip() for line in txt_file.readlines() if line.strip()]

    mask_positions = get_mask_positions(mask_filename)
    header = ["sentid", "pairid", "contextid", "lemma", "condition", "comparison", "sentence", "ROI"]
    data = []

    sentid = 0
    pairid = 0
    contextid = 1 
    condition = "MVRR" 

    for i in range(0, len(sentences), 2): 
        pairid += 1
        sentence_unexpected = sentences[i]
        sentence_expected = sentences[i + 1] if i + 1 < len(sentences) else ""

        roi_unexpected = mask_positions[i] if i < len(mask_positions) else -1
        roi_expected = mask_positions[i + 1] if i + 1 < len(mask_positions) else -1

        if roi_unexpected != -1: 
            sentid += 1
            lemma_unexpected = get_word(sentence_unexpected, roi_unexpected)
            data.append([sentid, pairid, contextid, lemma_unexpected, condition, "unexpected", sentence_unexpected, roi_unexpected])

        if sentence_expected and roi_expected != -1: 
            sentid += 1
            lemma_expected = get_word(sentence_expected, roi_expected)
            data.append([sentid, pairid, contextid, lemma_expected, condition, "expected", sentence_expected, roi_expected])

    with open(tsv_filename, "w", newline="", encoding="utf-8") as tsv_file:
        writer = csv.writer(tsv_file, delimiter="\t")
        writer.writerow(header)
        writer.writerows(data)

    print(f"TSV file created successfully: {tsv_filename}")

#txt_filename = "data/MVRR.txt"  # Update with the path to your TXT file
#mask_filename = "data/MVRR_mask.txt"  # Update with the path to your mask file
#tsv_filename = "data/MVRR_formatted.tsv"  # Desired output TSV file name
#transform_MVRR_to_tsv(txt_filename, mask_filename, tsv_filename)


def transform_overt_object_to_tsv(txt_filename, mask_filename, tsv_filename):
    """
    Transform the overt_object TXT file into a TSV file
    """
    mask_positions = get_mask_positions(mask_filename)

    with open(txt_filename, "r", encoding="utf-8") as txt_file:
        sentences = [line.strip() for line in txt_file.readlines() if line.strip()]

    header = ["sentid", "pairid", "contextid", "lemma", "condition", "comparison", "sentence", "ROI"]
    data = []
    sentid = 0
    pairid = 0
    contextid = 1 
    condition = "overt_object" 

    for i in range(0, len(sentences), 2): 
        pairid += 1
        sentence_unexpected = sentences[i]
        sentence_expected = sentences[i + 1] if i + 1 < len(sentences) else ""

        roi_unexpected = mask_positions[i] if i < len(mask_positions) else -1
        roi_expected = mask_positions[i + 1] if i + 1 < len(mask_positions) else -1

        if roi_unexpected != -1:  
            sentid += 1
            lemma_unexpected = get_word(sentence_unexpected, roi_unexpected)
            data.append([sentid, pairid, contextid, lemma_unexpected, condition, "unexpected", sentence_unexpected, roi_unexpected])

        if sentence_expected and roi_expected != -1:
            sentid += 1
            lemma_expected = get_word(sentence_expected, roi_expected)
            data.append([sentid, pairid, contextid, lemma_expected, condition, "expected", sentence_expected, roi_expected])

    with open(tsv_filename, "w", newline="", encoding="utf-8") as tsv_file:
        writer = csv.writer(tsv_file, delimiter="\t")
        writer.writerow(header)
        writer.writerows(data)

    print(f"TSV file created successfully: {tsv_filename}")

#txt_filename = "data/overt_object.txt"  # Update with the path to your TXT file
#mask_filename = "data/overt_object_mask.txt"  # Update with the path to your mask file
#tsv_filename = "data/overt_object_formatted.tsv"  # Desired output TSV file name
#transform_overt_object_to_tsv(txt_filename, mask_filename, tsv_filename)


def transform_verb_transitivity_to_tsv(txt_filename, mask_filename, tsv_filename):
    """
    Transform the verb_transitivity TXT file into a TSV file
    """
    mask_positions = get_mask_positions(mask_filename)

    with open(txt_filename, "r", encoding="utf-8") as txt_file:
        sentences = [line.strip() for line in txt_file.readlines() if line.strip()]

    header = ["sentid", "pairid", "contextid", "lemma", "condition", "comparison", "sentence", "ROI"]
    data = []

    sentid = 0
    pairid = 0
    contextid = 1
    condition = "verb_transitivity"  

    for i in range(0, len(sentences), 2): 
        pairid += 1
        sentence_unexpected = sentences[i]
        sentence_expected = sentences[i + 1] if i + 1 < len(sentences) else ""

        roi_unexpected = mask_positions[i] if i < len(mask_positions) else -1
        roi_expected = mask_positions[i + 1] if i + 1 < len(mask_positions) else -1

        if roi_unexpected != -1: 
            sentid += 1
            lemma_unexpected = get_word(sentence_unexpected, roi_unexpected)
            data.append([sentid, pairid, contextid, lemma_unexpected, condition, "unexpected", sentence_unexpected, roi_unexpected])

        if sentence_expected and roi_expected != -1: 
            sentid += 1
            lemma_expected = get_word(sentence_expected, roi_expected)
            data.append([sentid, pairid, contextid, lemma_expected, condition, "expected", sentence_expected, roi_expected])

    with open(tsv_filename, "w", newline="", encoding="utf-8") as tsv_file:
        writer = csv.writer(tsv_file, delimiter="\t")
        writer.writerow(header)
        writer.writerows(data)

    print(f"TSV file created successfully: {tsv_filename}")

txt_filename = "data/verb_transitivity.txt" 
mask_filename = "data/verb_transitivity_mask.txt" 
tsv_filename = "data/verb_transitivity_formatted.tsv" 
transform_verb_transitivity_to_tsv(txt_filename, mask_filename, tsv_filename)