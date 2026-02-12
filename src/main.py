from helper import create_rag_chain


def run():

    rag_chain = create_rag_chain()

    print("Medical Assistant Running (type 'exit' to quit)\n")

    while True:
        question = input("Ask: ")
        if question.lower() == "exit":
            break
        response = rag_chain.invoke(question)
        print("\nAnswer:", response)
        print("-" * 50)


if __name__ == "__main__":
    run()
