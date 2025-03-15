import re


def separate_pinyin_and_chinese_char(text):
    chinese_chars = re.sub(r'\([^\)]*\)', '', text)  # Remove Pinyin
    pinyin = ' '.join(re.findall(r'\((.*?)\)', text))  # *? as lazy capture to extract Pinyin

    return chinese_chars.strip(), pinyin.strip()


def process_document(input_file):
    result = []
    with open(input_file, "r", encoding="utf-8") as input_file:
        for line in input_file.readlines():
            chinese, pinyin = separate_pinyin_and_chinese_char(line)
            result.append(f"{chinese}\n{pinyin}")

        return result


input_file = "chinese-notes-text"
output_file = "separated-notes"
result = process_document(input_file)
with open(output_file, "w", encoding="utf-8") as output_file:
    for line in result:
        output_file.write(line + "\n")
