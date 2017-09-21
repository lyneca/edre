import sys
def convert_to_markdown(text):
    out = []
    list_level_incrementors = {}
    for paragraph in text['document']['paragraphs']:
        paragraph_style = paragraph['style']
        pre_paragraph = ''
        post_paragraph = ''
        if 'type' in paragraph_style:
            paragraph_type = paragraph_style['type']
            if paragraph_type == 4:
                list_type = paragraph_style['listType'] 
                list_level = paragraph_style['listLevel'] 
                if list_type == 0:
                    pre_paragraph = '    ' * list_level + '* '
                elif list_type == 1:
                    if list_level in list_level_incrementors:
                        list_level_incrementors[list_level] += 1
                        for i in list_level_incrementors:
                            if i > list_level:
                                list_level_incrementors[i] = 0
                    else:
                        list_level_incrementors[list_level] = 1
                        for i in list_level_incrementors:
                            if i > list_level:
                                list_level_incrementors[i] = 0
                    pre_paragraph = '    ' * list_level + str(list_level_incrementors[list_level]) + '. '
            if paragraph_type == 5:
                pre_paragraph = '```\n'
                post_paragraph = '```'
        out.append(pre_paragraph)
        for run in paragraph['runs']:
            had_text = False
            for span in run['spans']:
                style = span['style']
                text = span['text']
                if not text:
                    out.append(' ')
                had_text = True
                if 'bold' in style and style['bold']:
                    text = '**' + text + '**'
                if 'italic' in style and style['italic']:
                    text = '*' + text + '*'
                if 'underline' in style and style['underline']:
                    text = '_' + text + '_'
                if 'type' in style and style['type'] == 1:
                    text = '`' + text + '`'
                out.append(text)
            out.append('\n')
        out.append(post_paragraph)
    return ''.join(out)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(convert_to_markdown(__import__('json').loads(open(sys.argv[1]).read())))
    else:
        print("Not enough arguments; try:\nformatting.py [filename]")
