master_doc = 'index'

extensions = ['releases']

releases_github_path = 'shivam5992/textstat'

html_theme = 'alabaster'

html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}

html_theme_options = {
    'logo': 'textstat.png',
    'github_user': 'shivam5992',
    'github_repo': 'textstat',
    'github_type': 'star',
    'description': 'Calculate statistics from text',
}
