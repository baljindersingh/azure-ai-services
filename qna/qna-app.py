import os

# import namespaces
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def main():
    try:
        # Get Configuration Settings
        ai_endpoint = "https://instancebs1.cognitiveservices.azure.com" #os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = "c0cf3fa5f66e46d8bb33d87c42dcb485" #os.getenv('AI_SERVICE_KEY')
        ai_project_name = "LearnFAQ" #os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = "production" #os.getenv('QA_DEPLOYMENT_NAME')

         # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

         # Submit a question and display the answer
        user_question = ''
        while user_question.lower() != 'quit':
            user_question = input('\nQuestion:\n')
            response = ai_client.get_answers(question=user_question,
                                            project_name=ai_project_name,
                                            deployment_name=ai_deployment_name)
            for candidate in response.answers:
                print(candidate.answer)
                print("Confidence: {}".format(candidate.confidence))
                print("Source: {}".format(candidate.source))


    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
