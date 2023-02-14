import pyqt5ac

pyqt5ac.main(uicOptions='--from-imports', force=True, initPackage=True, ioPaths=[
        ['modules/gui/*.ui', 'modules/generated/%%FILENAME%%_ui.py'],
        ['modules/resources/*.qrc', 'modules/generated/%%FILENAME%%_rc.py'],
        # ['modules/*/*.ui', '%%DIRNAME%%/generated/%%FILENAME%%_ui.py'],
        # ['modules/*/resources/*.qrc', '%%DIRNAME%%/generated/%%FILENAME%%_rc.py']
    ])