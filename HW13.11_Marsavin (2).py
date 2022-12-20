SOURCE_CODE_DELIMITER = "# ---<source code delimeter>---"
SOURCE_MARKDOWN_DELIMITER = "<!---source markdown delimeter--->"

def read_data(file_name):
    file = open(file_name)
    content = file.read()
    return content

def prepare_md_title(data):
    splitted = data.split('\n')
    title, description = "", ""
    for line in splitted:
        if line.startswith('# title'):
            title = line.lstrip("# title ")
        elif line.startswith('# description '):
            description = line.lstrip("# description ")
    return title, description
    
def get_md_text_formatted(title, description, code):
    md_link = "-".join(title.lower().split())
    template_title = '+ [{}](#{})\n'
    template_code = '## {}\n\n{}\n\n```python\n{}\n```'
    new_title = template_title.format(title, md_link)
    new_code =  template_code.format(title, description, code.lstrip())
    return new_title, new_code

def prepare_old_md_content(content):
    md_titles, md_code = content.split(SOURCE_MARKDOWN_DELIMITER)
    return md_titles, md_code
    
def convert_to_md(data, old_md_content):
    data = content.split(SOURCE_CODE_DELIMITER)
    headers, source_code = data[0], data[1]
    title, description = prepare_md_title(headers)
    new_title, new_code = get_md_text_formatted(title, description, source_code)
    if old_md_content == "":
        final_template = '{}{}\n\n{}'
        return final_template.format(new_title, SOURCE_MARKDOWN_DELIMITER, new_code)
    else:
        old_md_titles, old_md_code = prepare_old_md_content(old_md_content)
        final_template = '{}{}{}\n\n{}\n{}'
        return final_template.format(new_title, old_md_titles, SOURCE_MARKDOWN_DELIMITER, new_code, old_md_code)
        
def write_data(file_name, data):
    f = open(file_name, "w")
    f.write(data)
    f.close()

content = read_data('solution.py')
old_md_content = read_data('out.txt')
final_md_content = convert_to_md(content, old_md_content)
write_data('out.txt', final_md_content)
