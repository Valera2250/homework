import re

def clean_html(input_file, output_file="cleaned.txt"):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()

        
        cleaned_content = re.sub(r'<.*?>', '', content)


        cleaned_lines = [line.strip() for line in cleaned_content.splitlines() if line.strip()]


        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(cleaned_lines))

        print(f"Файл успешно очищен и сохранен в '{output_file}'")
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


clean_html("draft.html")
