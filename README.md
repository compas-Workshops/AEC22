# AdvanceAEC Autumm School 2022

[🎦 Slides](https://docs.google.com/presentation/d/1GQQDSC2EjtDbAeaYtclkjn_P3UVJTWcczBzUWe_MUcI/edit) | [📃 COMPAS docs](https://compas.dev)

## Requirements

* Minimum OS: Windows 10 Pro or Mac OS Sierra 10.12
* [Anaconda 3](https://www.anaconda.com/distribution/)
* [Rhino 6/7 & Grasshopper](https://www.rhino3d.com/download)
* [Visual Studio Code](https://code.visualstudio.com/): Any python editor works, but we recommend [VS Code + extensions](https://compas.dev/compas/latest/gettingstarted/vscode.html)

Optional:

* [Docker Desktop](https://www.docker.com/products/docker-desktop) After installation on Windows, it is required to enable "Virtualization" on the BIOS of the computer.

## Help

If you need help with the installation process, please post a note on the workshop Slack channel: [Join AEC22 Slack](https://join.slack.com/t/slack-ck54085/shared_invite/zt-1higgedpw-qpWrnzAAadSEf~hstGnZ_w)

## Installation

> **NOTE**: If you're on Windows, all commands below have to be executed in the *Anaconda Prompt* (NOT the *Command Prompt*)

We use `conda` to make sure we have clean, isolated environment for dependencies.

<details><summary>First time using <code>conda</code>?</summary>
<p>

Make sure you run this at least once:

    (base) conda config --add channels conda-forge

</p>
</details>


    (base) conda env create -f https://raw.githubusercontent.com/compas-Workshops/AEC22/main/environment.yml

### Add to Rhino

    (base)  conda activate aec22
    (aec22) python -m compas_rhino.install -v 7.0

### Get the workshop files

Clone the repository:

    (aec22) cd Documents
    (aec22) git clone https://github.com/compas-Workshops/AEC22.git

### Verify installation

    (aec22) python -m compas

    Yay! COMPAS is installed correctly!

    COMPAS: 1.17.0
    Python: 3.9.13 (CPython)
    Extensions: ['compas-cgal', 'compas-gmsh', 'compas-rrc', 'compas-fab', 'compas-occ', 'compas-view2']

### Update installation

To update your environment:

    (aec22) conda env update -f https://raw.githubusercontent.com/compas-Workshops/AEC22/main/environment.yml
