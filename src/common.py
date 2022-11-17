LANG_MAPPING = {
    ('c++', 'cpp'): 'cpp',
    ('python3', 'python'): 'python3',
    'java': 'java',
    'c': 'c',
    'c#': 'csharp',
    'javascript': 'javascript',
    'ruby': 'ruby',
    'swift': 'swift',
    'Go': 'go',
}


def get_lang(lang: str):
    for k, v in LANG_MAPPING.items():
        if lang.lower() in k:
            return v
    return None
