import os

import setuptools.build_meta


build_wheel = setuptools.build_meta.build_wheel
build_sdist = setuptools.build_meta.build_sdist
prepare_metadata_for_build_wheel = (
    setuptools.build_meta.prepare_metadata_for_build_wheel
)
get_requires_for_build_sdist = (
    setuptools.build_meta.get_requires_for_build_sdist
)


requirements = {
   'attrs': '',
   'aqtinstall': '',
   'py7zr': '==0.6b6',
   'importlib-metadata': '',
   'hyperlink': '',
   'macholib': '',
   'psutil': '',
   'pylddwrap': '',
   'PyQt-builder': '',
   'requests': '',
   'setuptools': '',
   'sip': '',
   'vcversioner': '',
   'wheel': '',
}


overrides = dict(sorted({
    (5, 14): {
        'PyQt-builder': '==1.3.1',
        'sip': '==5.2.0',
    },
}.items()))


def pick_overrides(version, overrides):
    dicts = []

    for v, d in overrides.items():
        if v == version[:len(v)]:
            dicts.append(d)

    return dicts


def to_list(*dicts):
    merged = {}
    for d in dicts:
        merged.update(d)

    return [
        package + more
        for package, more in merged.items()
    ]


def get_requires_for_build_wheel(config_settings=None):
    # TODO: get this in via config_settings maybe
    version = tuple(int(v) for v in os.environ['PYQT_VERSION'].split('.'))

    dicts = [
        requirements,
        *pick_overrides(version=version, overrides=overrides),
    ]

    return to_list(*dicts)
