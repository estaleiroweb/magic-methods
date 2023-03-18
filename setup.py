import os
import subprocess
import setuptools

project_name = 'magic-methods'
project_path = project_name.replace('-', '')
licence = 'MIT License'
sDir = os.path.abspath(__file__ + '/..')


def getVersion() -> str:
    assert os.path.isfile(f'{sDir}/{project_path}/version.py')
    try:
        ver = (
            subprocess.run(['git', 'describe', '--tags'], stdout=subprocess.PIPE)
            .stdout.decode('utf-8')
            .strip()
        )
        if '-' in ver:
            # when not on tag, git describe outputs: '1.3.3-22-gdf81228'
            # pip has gotten strict with version numbers
            # so change it to: '1.3.3+22.git.gdf81228'
            # See: https://peps.python.org/pep-0440/#local-version-segments
            v, i, s = ver.split('-')
            ver = v + '+' + i + '.git.' + s

        print(ver)
        assert '-' not in ver
        assert '.' in ver

        with open(f'{sDir}/{project_path}/VERSION', 'w', encoding='utf-8') as fh:
            fh.write('%s\n' % ver)
    except:
        return '0.0.1'
    return ver


def getRequirements() -> list[str]:
    with open(f'{sDir}/requirement.txt', 'r') as file:
        return [line.strip() for line in file]


def getReadme() -> str:
    with open(f'{sDir}/README.md', 'r', encoding='utf-8') as fh:
        return fh.read()


dSetup = {
    'name': project_name,
    'version': getVersion(),
    'license': licence,
    'author': 'Helbert Braga Fernandes',
    'author_email': 'helbertfernandes@gmail.com',
    'description': u'All Magic Methods Implement. You can easyly to implement all magic methods or part of them',
    'long_description': getReadme(),
    'long_description_content_type': 'text/markdown',
    'url': f'https://github.com/HelbertFernandes/{project_name}',
    'include_package_data': True,
    'keywords': 'magic methods class',
    'classifiers': [
        'Development Status :: 1 - Production/Stable',
        f'License :: OSI Approved :: {licence}',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    'python_requires': '>=2.0',
    'install_requires': getRequirements() + [
        # 'dataclasses==0.7;python_version<3.8',
        # 'requests >= 2.25.1',
        # 'apache-libcloud >= 3.3.1',
    ],
    # entry_points={'console_scripts': [f'{project_path} = {project_path}.main:main']},
    'package_dir': {project_path: project_path},
    'packages': [project_path] + setuptools.find_packages(),
    'package_data': {project_path: ['VERSION']},
}

setuptools.setup(**dSetup)
