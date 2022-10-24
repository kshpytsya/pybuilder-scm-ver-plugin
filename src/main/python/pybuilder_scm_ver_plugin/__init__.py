from pybuilder.core import init, task
import setuptools_scm


@init
def initialize_my_plugin(project, logger):
    project.version = "<TO BE EXTRACTED FROM SCM>"
    project.set_property("version", project.version)

@task
def prepare(project, logger):
    root = project.get_property("scm_ver_root", ".")
    relative_to = project.get_property("scm_ver_relative_to", None)
    version_scheme = project.get_property("scm_ver_version_scheme", setuptools_scm.DEFAULT_VERSION_SCHEME)
    local_scheme = project.get_property("scm_ver_local_scheme", setuptools_scm.DEFAULT_LOCAL_SCHEME)
    logger.debug(f"pybuilder_scm_ver: root: {root}, relative to {relative_to}, local scheme: {local_scheme}, version scheme: {version_scheme}")
    project.version = setuptools_scm.get_version(root=root, relative_to=relative_to, version_scheme=version_scheme, local_scheme=local_scheme)
    project.set_property("version", project.version)
    logger.info(f"Version extracted from SCM: {project.version}")
