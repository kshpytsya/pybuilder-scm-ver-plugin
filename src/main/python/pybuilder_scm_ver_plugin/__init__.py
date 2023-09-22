from pybuilder.core import init, task
import setuptools_scm


@init
def initialize_my_plugin(project, logger):
    project.version = "<TO BE EXTRACTED FROM SCM>"
    project.set_property("version", project.version)

@task
def prepare(project, logger):
    # call setuptools_scm.get_version() only with available properties
    scm_kwargs = {}
    for key, prop in (
        ("root", "scm_ver_root"),
        ("relative_to", "scm_ver_relative_to"),
        ("version_scheme", "scm_ver_version_scheme"),
        ("local_scheme", "scm_ver_local_scheme"),
    ):
        if project.has_property(prop):
            scm_kwargs[key] = project.get_property(prop)
    if scm_kwargs:
        logger.debug("pybuilder_scm_ver: getting version with arguments" +
                     ",".join(f"{key}: {prop}" for key, prop in scm_kwargs.items()))
    else:
        logger.debug("pybuilder_scm_ver: getting version with default arguments")
    project.version = setuptools_scm.get_version(**scm_kwargs)
    project.set_property("version", project.version)
    logger.info(f"Version extracted from SCM: {project.version}")
