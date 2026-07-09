# Import functions from other files
from gemini_api import get_ai_answer
from search_api import search_web


def main():
    # Ask the user a question
    question = input("🔍 Ask me anything: ")

    # Get AI answer
    ai_answer = get_ai_answer(question)

    # Get search results
    websites = search_web(question)

    # Display results
    print("\n==============================")
    print(" SMART SOURCE FINDER ")
    print("==============================")

    print("\n📝 AI Answer:")
    print(ai_answer)

    print("\n🌐 Explore More:")

    for website in websites:
        print(f"- {website}")

    print("\n⚠ Compare multiple sources before deciding.")


# Run the program
if __name__ == "__main__":
    main()
