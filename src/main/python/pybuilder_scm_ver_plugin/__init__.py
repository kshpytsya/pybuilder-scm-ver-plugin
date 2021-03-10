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
    logger.debug(f"pybuilder_scm_ver: root: {root}, relative to {relative_to}")
    project.version = setuptools_scm.get_version(root=root, relative_to=relative_to)
    project.set_property("version", project.version)
    logger.info(f"Version extracted from SCM: {project.version}")
