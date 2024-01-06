import os
import re


def remove_timestamps_and_line_numbers(text):
    # Remove line numbers
    text = re.sub(r'^\d+\n', '', text, flags=re.MULTILINE)

    # Remove timestamps in the format 00:00:00,000 --> 00:00:00,000
    text = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}\n', '', text)

    return text


def remove_spaces_between_lines(text):
    # Remove spaces between lines
    text = re.sub(r'\n\s*\n', '\n', text)

    return text


def process_subtitle_file(file_path):
    with open(file_path, 'r') as file:
        subtitle_text = file.read()
        modified_text = remove_timestamps_and_line_numbers(subtitle_text)
        modified_text = remove_spaces_between_lines(modified_text)

    txt_file_path = os.path.splitext(file_path)[0] + '.txt'
    with open(txt_file_path, 'w') as file:
        file.write(modified_text)


def process_subtitle_files_in_directory(directory):
    subtitle_formats = ['.srt', '.vtt']  # Add more subtitle formats if needed
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file_path)[1]
            if file_extension in subtitle_formats:
                process_subtitle_file(file_path)


# Replace 'directory_path' with your directory containing subtitle files
directory_path = './'

# Process subtitle files in the directory
process_subtitle_files_in_directory(directory_path)
