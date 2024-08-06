prompt = f"""You are Q&A bot. A highly intelligent system that answers user questions based on the information provided by the user above each question.
If the information can not be found in the information provided by the user you truthfully say "Sorry, I don't have enough information to answer that"."""


def get_similiar_docs(vectorstore, query, k=3):
    similar_docs = vectorstore.similarity_search(query, k=3)
    return similar_docs


def generate_response(openai_client, prompt, augmented_query):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": augmented_query},
        ],
    )

    return response.choices[0].message.content
