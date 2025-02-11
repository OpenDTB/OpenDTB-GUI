import setuptools

setuptools.setup(
    name="OpenDTB-gui",
    version="0.0.3",
    description="CASIA's digital twin brain platform",
    author="Brain Netom Group",
    url="https://github.com/OpenDTB/OpenDTB-GUI",
    license="GPL-3.0",
    install_requires=[
        "OpenDTB-main @ https://github.com/OpenDTB/OpenDTB-MAIN/archive/refs/tags/v0.0.2.tar.gz",
        "PyQt-Fluent-Widgets",
        "lmdb",
        "qtconsole",
        "requests",
        "QCustomPlot_PyQt5",
        "pyqtgraph!=0.13.3",
        "PyOpenGL",
        "colorcet",
        "biopython>=1.78",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
)
