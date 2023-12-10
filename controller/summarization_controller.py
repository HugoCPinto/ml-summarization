from service import summarization_service

def controller():
    text = summarization_service.collect_data()
    summarization_service.tokenize_data(text)

if __name__ == '__main__':
    controller()