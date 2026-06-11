# NLP Text Analysis Tool for News Articles
import re
import string
import os

def read_file_content(filename):
    """ Reads the content of a file and returns it as a string.

    Args:
    filename (str): The name of the file to read
    
    Returns:
    str: The content of the file 
    """

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""


def create_sample_article():
    """Creates a sample news article file if none exists"""
    sample_text = """Climate Change Summit Reaches Historic Agreement

World leaders have reached a landmark agreement on climate action at the United Nations Climate Change Conference. The historic deal commits nearly 200 countries to phase out fossil fuels and transition to renewable energy sources by 2050.

The agreement represents a major breakthrough after two weeks of intense negotiations. Developing nations will receive financial support to accelerate their green energy transition. Wealthy countries have pledged 100 billion dollars annually to help poorer nations adapt to climate change impacts.

Environmental groups have praised the deal as a significant step forward. However, some activists argue that the commitments do not go far enough. They point out that current pledges would still allow global temperatures to rise by 1.8 degrees Celsius.

The conference president described the agreement as a victory for multilateralism. He emphasized that this is just the beginning of a long journey. Implementation will require continuous monitoring and increased ambition from all participating nations.

Several countries have already announced new national climate plans. China will peak its carbon emissions by 2030. India aims to achieve net zero by 2070. The European Union has strengthened its renewable energy targets for 2030.

The next conference will take place in Brazil next year. Delegates hope to build on this momentum and secure even stronger commitments. The window for limiting warming to 1.5 degrees is rapidly closing. Urgent action is needed from everyone."""
    
    try:
        with open("article.txt", "w", encoding='utf-8') as file:
            file.write(sample_text)
        print("✓ Sample article.txt has been created for you!")
        return True
    except Exception as e:
        print(f"Error creating sample article: {e}")
        return False


def count_specific_word(text, search_word):
    """ Counts the number of occurrences of a specific word in the given text.

    Args:
    text (str): The text to search through
    search_word (str): The word to count occurrences of

    Returns:
    int: The count of the specified word
    """

    if not text or not search_word:
        return 0
    
    # Convert both to lowercase for case-insensitive matching
    text_lower = text.lower()
    search_word_lower = search_word.lower()

    # Use word boundaries to match whole words only
    pattern = r'\b' + re.escape(search_word_lower) + r'\b'
    matches = re.findall(pattern, text_lower)

    return len(matches)


def identify_most_common_word(text):
    """ Identifies the most common word in the text.

    Args:
    text (str): The text to analyze

    Returns:
    str: The most common word, or None if text is empty
    """

    # Edge case: empty string should return None
    if not text or text.strip() == "":
        return None

    # Remove punctuation but keep apostrophes for contractions
    translator = str.maketrans('', '', string.punctuation.replace("'", ""))
    cleaned_text = text.translate(translator)

    # Split into words and convert to lowercase
    words = cleaned_text.lower().split()

    # Edge case: no words after cleaning
    if not words:
        return None
    
    # Count word frequencies
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Find the most common word
    most_common_word = max(word_counts, key=word_counts.get)
    return most_common_word


def calculate_average_word_length(text):
    """ Calculates the average length of words in the text, excluding punctuation.
    
    Args:
    text (str): The text to analyze
    
    Returns:
    float: The average word length, or 0 if text is empty

    """
    # Edge case: empty string should return 0
    if not text or text.strip() == "":
        return 0.0
    
    # Remove punctuation from the text
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    # Split the cleaned text into words
    words = cleaned_text.split()

    # Edge case: no words after cleaning
    if not words:
        return 0.0
    
    # Calculate total length of all words
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)

    return round(average_length, 2)


def count_paragraphs(text):
    """ Counts the number of paragraphs in the text. A paragraph is defined as a block of text separated by one or more newline characters.

    Args:
    text (str): The text to analyze

    Returns:
    int: The number of paragraphs in the text
    """

    # Edge case: empty string should return 1 (as per requirements)
    if not text or text.strip() == "":
        return 1
    
    # Split the text into paragraphs using one or more newline characters as the delimiter
    paragraphs = re.split(r'\n+', text.strip())
    
    # Filter out empty paragraphs
    paragraphs = [p for p in paragraphs if p.strip() != '']

    # If no paragraphs found but text has content, treat as one paragraph
    if not paragraphs and text.strip():
        return 1
    
    return len(paragraphs)


def count_sentences(text):
    """ Counts the number of sentences in the text. A sentence is defined as a string of characters ending with a period (.), exclamation mark (!), or question mark (?).

    Args:
    text (str): The text to analyze

    Returns:
    int: The number of sentences in the text
    """

    # Edge case: empty string should return 1 (as per requirements)
    if not text or text.strip() == "":
        return 1

    # Split text into sentences using sentence-ending punctuation
    # This regex handles multiple punctuation marks (e.g., "!!!", "??", "!?")
    sentences = re.split(r'[.!?]+', text)
    
    # Filter out empty strings and strip whitespace
    sentences = [s.strip() for s in sentences if s.strip()]
    
    sentence_count = len(sentences)
    
    # If no sentence delimiters found but text has content, count as one sentence
    if sentence_count == 0 and text.strip():
        return 1
    
    return sentence_count


def display_menu():
    """ Displays the main menu options."""
    
    print("\n" + "="*50)
    print("NEWS ARTICLE ANALYSIS TOOL")
    print("="*50)
    print("1. Count occurrences of a specific word")
    print("2. Identify the most common word")
    print("3. Calculate average word length")
    print("4. Count the number of paragraphs")
    print("5. Count the number of sentences")
    print("6. Perform complete analysis")
    print("7. Load different news article")
    print("8. Exit")
    print("="*50)


def perform_complete_analysis(text):
    """Performs a complete analysis of the text, including all metrics."""
    print("\n" + "="*50)
    print("COMPLETE ANALYSIS")
    print("="*50)

    # Most common word
    common_word = identify_most_common_word(text)
    if common_word:
        print(f"Most Common Word: '{common_word}'")
    else:
        print("Most Common Word: None")

    # Average word length
    avg_length = calculate_average_word_length(text)
    print(f"Average word length: {avg_length} characters")

    # Paragraph count
    para_count = count_paragraphs(text)
    print(f"Number of paragraphs: {para_count}")

    # Sentence count
    sent_count = count_sentences(text)
    print(f"Number of sentences: {sent_count}")
    print("="*50)


def main():
    """
    Main function that orchestrates the text analysis program.
    """
    print("Welcome to the News Article Text Analysis Tool!")
    
    # Check if article.txt exists, if not create it
    if not os.path.exists("article.txt"):
        print("\nNo article file found. Creating a sample article for you...")
        create_sample_article()
    
    # Using a while loop to get valid filename
    while True:
        filename = input("\nEnter the news article filename (e.g., article.txt): ").strip()
        if filename:
            break
        print("Filename cannot be empty. Please try again.")
    
    # Read the file content
    text_content = read_file_content(filename)
    
    # Using if/else conditional structure
    if not text_content:
        print("Exiting program due to file read error.")
        return
    else:
        print(f"\nSuccessfully loaded '{filename}' ({len(text_content)} characters)")
    
    # Main program loop using while loop
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            # Using if/elif/else conditional structure
            if choice == '1':
                # Count specific word
                search_word = input("Enter the word to count: ").strip()
                if search_word:
                    count = count_specific_word(text_content, search_word)
                    print(f"\nThe word '{search_word}' appears {count} time(s) in the article.")
                else:
                    print("Please enter a valid word.")
            
            elif choice == '2':
                # Identify most common word
                most_common = identify_most_common_word(text_content)
                if most_common:
                    print(f"\nThe most common word in the article is: '{most_common}'")
                else:
                    print("\nNo words found in the article.")
            
            elif choice == '3':
                # Calculate average word length
                avg_len = calculate_average_word_length(text_content)
                print(f"\nThe average word length in the article is: {avg_len} characters")
            
            elif choice == '4':
                # Count paragraphs
                para_count = count_paragraphs(text_content)
                print(f"\nThe article has {para_count} paragraph(s).")
            
            elif choice == '5':
                # Count sentences
                sent_count = count_sentences(text_content)
                print(f"\nThe article has {sent_count} sentence(s).")
            
            elif choice == '6':
                # Complete analysis
                perform_complete_analysis(text_content)
            
            elif choice == '7':
                # Load different file - using for loop to display preview
                new_filename = input("Enter new filename: ").strip()
                new_content = read_file_content(new_filename)
                
                # Using if/else conditional
                if new_content:
                    text_content = new_content
                    print(f"\nSuccessfully loaded '{new_filename}'")
                    
                    # Using for loop to show first few lines as preview
                    lines = text_content.split('\n')[:5]
                    print("\nPreview of new article (first 5 lines):")
                    # Using for loop with enumerate for line numbering
                    for i, line in enumerate(lines, 1):
                        if line.strip():
                            # Truncate long lines for display
                            preview_line = line[:100] + "..." if len(line) > 100 else line
                            print(f"  {i}. {preview_line}")
                else:
                    print("Could not load new file. Keeping current article.")
            
            elif choice == '8':
                print("\nThank you for using the News Article Text Analysis Tool. Goodbye!")
                break
            
            else:
                print("\nInvalid choice. Please enter a number between 1 and 8.")
        
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}. Please try again.")


# Entry point of the program
if __name__ == "__main__":
    main()
    
   