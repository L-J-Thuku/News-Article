# NLP Text Analysis Tool for News Articles
import re
import string

def read_file_content(filename):
    """ Reads the content of a file and returns it as a string."""
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

def count_specific_word(text, search_word):
    """Counts occurrences of a specific word in the text."""
    if not text or not search_word:
        return 0
    
    text_lower = text.lower()
    search_word_lower = search_word.lower()
    
    # Use word boundaries to match whole words only
    pattern = r'\b' + re.escape(search_word_lower) + r'\b'
    matches = re.findall(pattern, text_lower)
    
    return len(matches)

def identify_most_common_word(text):
    """Identifies the most common word in the text."""
    if not text or text.strip() == "":
        return None
    
    # Remove punctuation but keep apostrophes for contractions
    translator = str.maketrans('', '', string.punctuation.replace("'", ""))
    cleaned_text = text.translate(translator)
    
    words = cleaned_text.lower().split()
    
    if not words:
        return None
    
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    
    most_common_word = max(word_counts, key=word_counts.get)
    return most_common_word

def calculate_average_word_length(text):
    """Calculates average length of words, excluding punctuation."""
    if not text or text.strip() == "":
        return 0.0
    
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()
    
    if not words:
        return 0.0
    
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    
    return round(average_length, 2)

def count_paragraphs(text):
    """Counts number of paragraphs separated by empty lines."""
    if not text or text.strip() == "":
        return 1
    
    paragraphs = re.split(r'\n+', text.strip())
    paragraphs = [p for p in paragraphs if p.strip() != '']
    
    if not paragraphs and text.strip():
        return 1
    
    return len(paragraphs)

def count_sentences(text):
    """Counts number of sentences ending with ., !, or ?"""
    if not text or text.strip() == "":
        return 1
    
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    if len(sentences) == 0 and text.strip():
        return 1
    
    return len(sentences)

def display_menu():
    """Displays main menu options."""
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
    """Performs complete analysis of the text."""
    print("\n" + "="*50)
    print("COMPLETE ANALYSIS")
    print("="*50)
    
    common_word = identify_most_common_word(text)
    if common_word:
        print(f"Most Common Word: '{common_word}'")
    else:
        print("Most Common Word: None")
    
    avg_length = calculate_average_word_length(text)
    print(f"Average word length: {avg_length} characters")
    
    para_count = count_paragraphs(text)
    print(f"Number of paragraphs: {para_count}")
    
    sent_count = count_sentences(text)
    print(f"Number of sentences: {sent_count}")
    print("="*50)

def main():
    """Main function orchestrating the program."""
    print("Welcome to the News Article Text Analysis Tool!")
    
    # Using while loop for filename input
    while True:
        filename = input("\nEnter the news article filename (e.g., article.txt): ").strip()
        if filename:
            break
        print("Filename cannot be empty. Please try again.")
    
    text_content = read_file_content(filename)
    
    # Using if/else conditional
    if not text_content:
        print("Exiting program due to file read error.")
        return
    else:
        print(f"\nSuccessfully loaded '{filename}' ({len(text_content)} characters)")
    
    # Using while loop for main menu
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-8): ").strip()
            
            # Using if/elif/else conditional structure
            if choice == '1':
                search_word = input("Enter the word to count: ").strip()
                if search_word:
                    count = count_specific_word(text_content, search_word)
                    print(f"\nThe word '{search_word}' appears {count} time(s) in the article.")
                else:
                    print("Please enter a valid word.")
            
            elif choice == '2':
                most_common = identify_most_common_word(text_content)
                if most_common:
                    print(f"\nThe most common word in the article is: '{most_common}'")
                else:
                    print("\nNo words found in the article.")
            
            elif choice == '3':
                avg_len = calculate_average_word_length(text_content)
                print(f"\nThe average word length in the article is: {avg_len} characters")
            
            elif choice == '4':
                para_count = count_paragraphs(text_content)
                print(f"\nThe article has {para_count} paragraph(s).")
            
            elif choice == '5':
                sent_count = count_sentences(text_content)
                print(f"\nThe article has {sent_count} sentence(s).")
            
            elif choice == '6':
                perform_complete_analysis(text_content)
            
            elif choice == '7':
                new_filename = input("Enter new filename: ").strip()
                new_content = read_file_content(new_filename)
                
                if new_content:
                    text_content = new_content
                    print(f"\nSuccessfully loaded '{new_filename}'")
                    
                    # Using for loop to show preview
                    lines = text_content.split('\n')[:5]
                    print("\nPreview of new article (first 5 lines):")
                    for i, line in enumerate(lines, 1):
                        if line.strip():
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

if __name__ == "__main__":
    main()