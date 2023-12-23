import json

from service import summarization_service


def summarization_controller(request, lang):
    if request == '':
        text = summarization_service.collect_data()
    else:
        text = request

    summary = summarization_service.tokenize_data(text, lang)
    print(summary)
    return json.dumps(summary)


if __name__ == '__main__':
    print(summarization_controller(''))
