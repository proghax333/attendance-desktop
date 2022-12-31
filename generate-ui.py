import pyqt5ac

pyqt5ac.main(uicOptions='--from-imports', force=True, initPackage=True, ioPaths=[
        ['gui/*.ui', 'generated/%%FILENAME%%_ui.py'],
        ['resources/*.qrc', 'generated/%%FILENAME%%_rc.py'],
        # ['modules/*/*.ui', '%%DIRNAME%%/generated/%%FILENAME%%_ui.py'],
        # ['modules/*/resources/*.qrc', '%%DIRNAME%%/generated/%%FILENAME%%_rc.py']
    ])