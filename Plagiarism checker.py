import difflib

def load_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def check_plagiarism(text1, text2):
    # Use difflib to compare texts
    d = difflib.Differ()
    diff = d.compare(text1.splitlines(), text2.splitlines())

    # Calculate similarity ratio
    similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

    return diff, similarity_ratio

def main():
    # Get file paths for the texts to be compared
    file_path1 = input("Enter the path of the first text file: ")
    file_path2 = input("Enter the path of the second text file: ")

    # Load texts from files
    text1 = load_text(file_path1)
    text2 = load_text(file_path2)

    # Check plagiarism
    diff, similarity_ratio = check_plagiarism(text1, text2)

    # Print results
    print("\nText Comparison:")
    for line in diff:
        print(line)

    print("\nSimilarity Ratio: {:.2%}".format(similarity_ratio))

    # Define a threshold for plagiarism (adjust as needed)
    plagiarism_threshold = 0.75

    if similarity_ratio >= plagiarism_threshold:
        print("Plagiarism detected!")
    else:
        print("No plagiarism detected.")

if __name__ == "__main__":
    main()
