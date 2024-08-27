import text_processing_tool

def main():
    text = input("Enter a text string: ")

    print("Text Processing Results:")
    print(f"Word Count: {text_processing_tool.count_words(text)}")
    print(f"Unique Words: {text_processing_tool.find_unique_words(text)}")
    print(f"Uppercase Text: {text_processing_tool.convert_to_uppercase(text)}")

if __name__ == "__main__":
    main()