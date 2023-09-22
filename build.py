from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "pybuilder-scm-ver-plugin"
authors = [Author("Kyrylo Shpytsya", "kshpitsa@gmail.com")]
license = "MIT"
summary = "pybuilder plugin to set project from SCM"
version = "0.2.1"
url = "https://github.com/kshpytsya/pybuilder-scm-ver-plugin"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on("setuptools_scm<9.0")
    project.set_property("distutils_classifiers", [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Version Control'
    ])
